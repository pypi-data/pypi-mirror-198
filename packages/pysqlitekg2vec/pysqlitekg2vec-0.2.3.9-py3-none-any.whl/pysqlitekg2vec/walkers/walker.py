import multiprocessing
import random
import warnings
from abc import ABC, abstractmethod
from multiprocessing import Queue
from threading import Thread
from typing import List, Optional, Set, Sequence, Tuple

import attr
import numpy as np
import progressbar as pb

from pysqlitekg2vec.graphs import KG, Vertex
from pysqlitekg2vec.samplers import Sampler, UniformSampler
from pysqlitekg2vec.typings import Entities, EntityWalks, SWalk

from pysqlitekg2vec.utils.validation import (  # isort: skip
    _check_max_depth,
    _check_jobs,
    _check_max_walks,
)
from pysqlitekg2vec.walkers.vault.vault import WalkImporter


class WalkerNotSupported(Exception):
    """Base exception class for the lack of support of a walking strategy for
    the extraction of walks via a SPARQL endpoint server.

    """

    pass


@attr.s
class Walker(ABC):
    """Base class of the walking strategies.

    Attributes:
        _is_support_remote: True if the walking strategy can be used with a
            remote Knowledge Graph, False Otherwise
            Defaults to True.
        kg: The global KG used later on for the worker process.
            Defaults to None.
        max_depth: The maximum depth of one walk.
        max_walks: The maximum number of walks per entity.
            Defaults to None.
        random_state: The random state to use to keep random determinism with
            the walking strategy.
            Defaults to None.
        sampler: The sampling strategy.
            Defaults to UniformSampler.
        with_reverse: True to extracts parents and children hops from an
            entity, creating (max_walks * max_walks) walks of 2 * depth,
            allowing also to centralize this entity in the walks. False
            otherwise. This doesn't work with NGramWalker and WLWalker.
            Defaults to False.

    """

    kg = attr.ib(init=False, repr=False, type=Optional[KG], default=None)

    max_depth = attr.ib(
        type=int,
        validator=[attr.validators.instance_of(int), _check_max_depth],
    )

    max_walks = attr.ib(  # type: ignore
        default=None,
        type=Optional[int],
        validator=[
            attr.validators.optional(attr.validators.instance_of(int)),
            _check_max_walks,
        ],
    )

    sampler = attr.ib(
        factory=lambda: UniformSampler(),
        type=Sampler,
        validator=attr.validators.instance_of(Sampler),  # type: ignore
    )

    n_jobs = attr.ib(  # type: ignore
        default=None,
        type=Optional[int],
        validator=[
            attr.validators.optional(attr.validators.instance_of(int)),
            _check_jobs,
        ],
    )

    with_reverse = attr.ib(
        kw_only=True,
        type=Optional[bool],
        default=False,
        validator=attr.validators.instance_of(bool),
    )

    random_state = attr.ib(
        kw_only=True,
        type=Optional[int],
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
    )

    _is_support_remote = attr.ib(
        init=False, repr=False, type=bool, default=True
    )

    _entities = attr.ib(init=False, repr=False, type=Set[str], default=set())

    def __attrs_post_init__(self):
        if self.n_jobs == -1:
            self.n_jobs = multiprocessing.cpu_count()
        self.sampler.random_state = self.random_state

    def extract(
        self, kg: KG, importer: WalkImporter, entities: Entities,
        verbose: int = 0
    ) -> None:
        """Fits the provided sampling strategy and then calls the
        private _extract method that is implemented for each of the
        walking strategies.

        Args:
            kg: The Knowledge Graph.
            vault: The vault of stored generated walks.
            entities: The entities to be extracted from the Knowledge Graph.
            verbose: The verbosity level.
                0: does not display anything;
                1: display of the progress of extraction and training of walks;
                2: debugging.
                Defaults to 0.

        Returns:
            The 2D matrix with its number of rows equal to the number of
            provided entities; number of column equal to the embedding size.

        Raises:
            WalkerNotSupported: If there is an attempt to use an invalid
                walking strategy to a remote Knowledge Graph.

        """
        if kg._is_remote and not self._is_support_remote:
            raise WalkerNotSupported(
                "Invalid walking strategy. Please, choose a walking strategy "
                + "that can fetch walks via a SPARQL endpoint server."
            )

        process = self.n_jobs if self.n_jobs is not None else 1
        if (kg._is_remote and kg.mul_req) and process >= 2:
            warnings.warn(
                "Using 'mul_req=True' and/or 'n_jobs>=2' speed up the "
                + "extraction of entity's walks, but may violate the policy "
                + "of some SPARQL endpoint servers.",
                category=RuntimeWarning,
                stacklevel=2,
            )

        if kg._is_remote and kg.mul_req:
            kg._fill_hops(entities)

        self.sampler.fit(kg)
        self._entities |= set(entities)

        r_queue = Queue()

        with pb.ProgressBar(max_value=len(entities)) as bar:

            with multiprocessing.Pool(process, self._init_worker,
                                      [kg, r_queue]) as pool:
                random.shuffle(entities)
                splits = np.array_split(entities, process)

                ps = []
                for split in splits:
                    ps.append(pool.apply_async(self._proc, args=(split,)))

                n = 0
                while n < len(entities):
                    res = r_queue.get()
                    for entity_id in res.keys():
                        importer.add_walks(entity_id, res[entity_id])
                        n += 1
                    bar.update(n)

                for p in ps:
                    success, error_str = p.get()
                    if not success:
                        raise ValueError(
                            'corpus generation failed: %s' % error_str)

    @abstractmethod
    def _extract(self, kg: KG, entity: Vertex) -> EntityWalks:
        """Extracts random walks for an entity based on a Knowledge Graph.

        Args:
            kg: The Knowledge Graph.
            entity: The root node to extract walks.

        Returns:
            A dictionary having the entity as key and a list of tuples as value
            corresponding to the extracted walks.

        Raises:
            NotImplementedError: If this method is called, without having
                provided an implementation.

        """
        raise NotImplementedError("This must be implemented!")

    def _init_worker(self, init_kg: KG, init_result_queue: Queue) -> None:
        """Initializes each worker process.

        Args:
            init_kg: The Knowledge Graph to provide to each worker process.

        """
        global kg
        kg = init_kg  # type: ignore
        global result_queue
        result_queue = init_result_queue

    def _post_extract(self, res: List[EntityWalks]) -> List[List[SWalk]]:
        """Post processed walks.

        Args:
            res: the result of the walks extracted with multiprocessing.

        Returns:
            The 2D matrix with its number of rows equal to the number of
            provided entities; number of column equal to the embedding size.

        """
        return list(
            walks
            for entity_to_walks in res
            for walks in entity_to_walks.values()
        )

    def _proc(self, entities: Sequence[str]) -> Tuple[bool, str]:
        """Executed by each process.

        Args:
            entities: list of entities to be extracted from the Knowledge
            Graph.

        Returns:
            The extraction of walk by the process.

        """
        global kg
        global result_queue

        try:
            for entity in entities:
                result_queue.put(
                    self._extract(kg, Vertex(entity)))  # type: ignore
            return True, ""
        except Exception as e:
            return False, str(e)
