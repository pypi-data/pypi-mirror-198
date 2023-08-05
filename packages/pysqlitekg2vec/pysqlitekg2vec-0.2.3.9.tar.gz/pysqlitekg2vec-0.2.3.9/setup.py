# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysqlitekg2vec',
 'pysqlitekg2vec.embedders',
 'pysqlitekg2vec.graphs',
 'pysqlitekg2vec.graphs.lmdb',
 'pysqlitekg2vec.graphs.sqlite',
 'pysqlitekg2vec.samplers',
 'pysqlitekg2vec.utils',
 'pysqlitekg2vec.walkers',
 'pysqlitekg2vec.walkers.vault']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.2,<23.0',
 'cachetools>=5.0.0,<6.0.0',
 'matplotlib>=3.4.2,<4.0.0',
 'networkx>=2.8,<3.0',
 'python-Levenshtein>=0.12.2,<0.13.0',
 'python-louvain>=0.16,<0.17',
 'sortedcontainers>=2.4.0,<3.0.0',
 'torch>=1.8.1,<2.0.0']

extras_require = \
{':extra == "docs"': ['scikit-learn>=1.0.2,<2.0.0', 'toml>=0.10.2,<0.11.0'],
 ':extra == "docs" or extra == "tests"': ['gensim>=4.0.1,<5.0.0',
                                          'rdflib>=6.1.1,<7.0.0'],
 ':extra == "tests"': ['nest_asyncio>=1.5.4,<2.0.0',
                       'nest-asyncio>=1.5.1,<2.0.0',
                       'numpy>=1.22.3,<2.0.0',
                       'pandas>=1.4.2,<2.0.0',
                       'aiohttp>=3.8.1,<4.0.0']}

setup_kwargs = {
    'name': 'pysqlitekg2vec',
    'version': '0.2.3.9',
    'description': 'Python implementation and extension of RDF2Vec',
    'long_description': '# What is SQLiteKG2Vec?\n\nSQLitKG2Vec is an experimental extension of the popular pyRDF2Vec\nlibrary for training RDF2Vec embeddings. It might in the future be\nmerged into the main project. This experimental extension stores the\nstatements of the KG as well as the generated walks into a simple SQLite\ndatabase. Hence, it is possible to train embeddings for huge knowledge\ngraphs without running into memory issues.\n\nRDF2Vec is an unsupervised technique that builds further on\n[Word2Vec](https://en.wikipedia.org/wiki/Word2vec), where an embedding\nis learned per word, in two ways:\n\n1.  **the word based on its context**: Continuous Bag-of-Words (CBOW);\n2.  **the context based on a word**: Skip-Gram (SG).\n\nTo create this embedding, RDF2Vec first creates "sentences" which can be\nfed to Word2Vec by extracting walks of a certain depth from a Knowledge\nGraph.\n\nThis repository contains an implementation of the algorithm in "RDF2Vec:\nRDF Graph Embeddings and Their Applications" by Petar Ristoski, Jessica\nRosati, Tommaso Di Noia, Renato De Leone, Heiko Paulheim\n([\\[paper\\]](http://semantic-web-journal.net/content/rdf2vec-rdf-graph-embeddings-and-their-applications-0)\n[\\[original\ncode\\]](http://data.dws.informatik.uni-mannheim.de/rdf2vec/)).\n\n# Getting Started\n\nFor most uses-cases, here is how `pySQLiteKG2Vec` should be used to\ngenerate embeddings and get literals from a given Knowledge Graph (KG)\nand entities:\n\n``` python\nfrom pyrdf2vec import RDF2VecTransformer\nfrom pyrdf2vec.embedders import Word2Vec\nfrom pyrdf2vec.graphs.io import open_from_pykeen_dataset\nfrom pyrdf2vec.walkers import RandomWalker\nfrom pyrdf2vec.walkers.vault.sqlitevault import SQLiteCorpusVaultFactory\n\nwith open_from_pykeen_dataset(\'dbpedia50\') as kg:\n    transformer = RDF2VecTransformer(\n        Word2Vec(epochs=10),\n        walkers=[RandomWalker(max_walks=200,\n                              max_depth=4,\n                              random_state=133,\n                              with_reverse=False,\n                              n_jobs=1)],\n        vault_factory=SQLiteCorpusVaultFactory(\'corpus.db\'),\n        verbose=1\n    )\n    # train RDF2Vec\n    ent = kg.entities()\n    embeddings, _ = transformer.fit_transform(kg, ent)\n    with open(\'embeddings.tsv\', \'w\') as f:\n        writer = csv.writer(f, delimiter=\'\\t\')\n        for name, vector in kg.pack(ent, embeddings):\n            writer.writerow([name] + [x for x in vector])\n```\n\n## Create from PyKeen dataset\n\n[PyKeen](https://github.com/pykeen/pykeen) is a popular library for\nknowledge graph embeddings, and it specifies a number of datasets that\nare commonly referenced in scientific literature. An SQLite KG can be\nconstructed from a PyKeen dataset by specifying the name of the dataset\nor passing the dataset instance.\n\nIn the following code snippet, the <span class="title-ref">db100k</span>\ndataset, which is a subsampling of DBpedia, is used to construct an\nSQLite KG.\n\n``` python\nfrom pyrdf2vec.graphs.io import open_from_pykeen_dataset\n\nwith open_from_pykeen_dataset(\'db100k\', combined=True) as kg:\n    # ...\n    pass\n```\n\n**Parameters:**\n\n-   *combined* - <span class="title-ref">False</span> if only the\n    training set of a dataset shall be used for the training of RDF2Vec.\n    <span class="title-ref">True</span> if all the sets (training,\n    testing and validation) shall be used. It is <span\n    class="title-ref">False</span> by default.\n\n## Create from TSV file\n\nIn order to save memory for big knowledge graphs, it might be a good\nidea to load the statements of such a knowledge graph from a TSV file\ninto a SQLite KG. All the rows in the TSV file must have three columns,\nwhere the first column is the subject, the second is the predicate, and\nthe last column is the object.\n\nThe following code snippet creates a new SQLite KG instance from the\nstatements of the specified TSV file, which has been compressed using\nGZIP.\n\n``` python\nfrom pyrdf2vec.graphs.io import open_from_tsv_file\n\nwith open_from_tsv_file(\'statements.tsv.gz\', compression=\'gzip\') as kg:\n    # ...\n    pass\n```\n\n**Parameters:**\n\n-   *skip_header* - <span class="title-ref">True</span> if the first row\n    shall be skipped, because it is a header row for example. <span\n    class="title-ref">False</span> if it shouldn\'t be skipped. It is\n    <span class="title-ref">False</span> by default.\n-   *compression* - specifies the compression type of source TSV file.\n    The default value is <span class="title-ref">None</span>, which\n    means that the source isn\'t compressed. At the moment, only <span\n    class="title-ref">\'gzip\'</span> is supported as compression type.\n\n## Create from Pandas dataframe\n\nA knowledge graph can be represented in a Pandas dataframe, and this\nmethod allows to create an SQLite KG from a dataframe. While the\ndataframe can have more than three columns, the three columns\nrepresenting the subject, predicate and object must be specified in this\nparticular order.\n\nThe following code snippet creates a new SQLite KG instance from a\ndataframe.\n\n``` python\nfrom pyrdf2vec.graphs.io import open_from_dataframe\n\nwith open_from_dataframe(df, column_names=(\'subj\', \'pred\', \'obj\')) as kg:\n    # ...\n    pass\n```\n\n**Parameters:**\n\n-   *column_names* - a tuple of three indices for the dataframe, which\n    can be an integer or string. The first entry of the tuple shall\n    point to the subject, the second to the predicate, and the third one\n    to the object. <span class="title-ref">(0, 1, 2)</span> are the\n    default indices.\n\n## Limitations\n\nThis extension has three limitations in contrast to the original\nimplementation.\n\n1)  **Literals** are ignored by this implementation for now.\n2)  **Samplers** (besides the default one) might not work properly.\n\n## Installation\n\n`pySQLiteKG2Vec` can be installed in three ways:\n\n1.  from [PyPI](https://pypi.org/project/pySQLiteKG2Vec) using `pip`:\n\n``` bash\npip install pySQLiteKG2Vec\n```\n\n2.  from any compatible Python dependency manager (e.g., `poetry`):\n\n``` bash\npoetry add pyRDF2vec\n```\n\n3.  from source:\n\n``` bash\ngit clone https://github.com/IBCNServices/pyRDF2Vec.git\npip install .\n```\n\n# Documentation\n\nFor more information on how to use `pyRDF2Vec`, [visit our online\ndocumentation](https://pyrdf2vec.readthedocs.io/en/latest/) which is\nautomatically updated with the latest version of the `main` branch.\n\nFrom then on, you will be able to learn more about the use of the\nmodules as well as their functions available to you.\n\n# Contributions\n\nYour help in the development of `pyRDF2Vec` is more than welcome.\n\n<p align="center">\n  <img width="85%" src="./assets/architecture.png" alt="architecture">\n</p>\n\nThe architecture of `pyRDF2Vec` makes it easy to create new extraction\nand sampling strategies, new embedding techniques. In order to better\nunderstand how you can help either through pull requests and/or issues,\nplease take a look at the\n[CONTRIBUTING](https://github.com/IBCNServices/pyRDF2Vec/blob/main/CONTRIBUTING.rst)\nfile.\n\n# FAQ\n\n## How to Ensure the Generation of Similar Embeddings?\n\n`pySQLiteKG2Vec`\'s walking strategies, sampling strategies and Word2Vec\nwork with randomness. To get reproducible embeddings, you firstly need\nto **use a seed** to ensure determinism:\n\n``` bash\nPYTHONHASHSEED=42 python foo.py\n```\n\nAdded to this, you must **also specify a random state** to the walking\nstrategy which will implicitly use it for the sampling strategy:\n\n``` python\nfrom pyrdf2vec.walkers import RandomWalker\n\nRandomWalker(2, None, random_state=42)\n```\n\n**NOTE:** the `PYTHONHASHSEED` (e.g., 42) is to ensure determinism.\n\nFinally, to ensure random determinism for Word2Vec, you must **specify a\nsingle worker**:\n\n``` python\nfrom pyrdf2vec.embedders import Word2Vec\n\nWord2Vec(workers=1)\n```\n\n**NOTE:** using the `n_jobs` and `mul_req` parameters does not affect\nthe random determinism.\n\n## Why the Extraction Time of Walks is Faster if `max_walks=None`?\n\nCurrently, **the BFS function** (using the Breadth-first search\nalgorithm) is used when `max_walks=None` which is significantly\n**faster** than the DFS function (using the Depth-first search\nalgorithm) **and extract more walks**.\n\nWe hope that this algorithmic complexity issue will be solved for the\nnext release of `pyRDf2Vec`\n\n## How to Silence the tcmalloc Warning When Using FastText With Mediums/Large KGs?\n\nSets the `TCMALLOC_LARGE_ALLOC_REPORT_THRESHOLD` environment variable to\na high value.\n\n# Referencing\n\nIf you use `pyRDF2Vec` in a scholarly article, we would appreciate a\ncitation:\n\n``` bibtex\n@article{pyrdf2vec,\n  title        = {pyRDF2Vec: A Python Implementation and Extension of RDF2Vec},\n  author       = {Vandewiele, Gilles and Steenwinckel, Bram and Agozzino, Terencio and Ongenae, Femke},\n  year         = 2022,\n  publisher    = {arXiv},\n  doi          = {10.48550/ARXIV.2205.02283},\n  url          = {https://arxiv.org/abs/2205.02283},\n  copyright    = {Creative Commons Attribution 4.0 International},\n  organization = {IDLab},\n  keywords     = {Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences}\n}\n```\n',
    'author': 'Gilles Vandewiele',
    'author_email': 'gilles.vandewiele@ugent.be',
    'maintainer': 'Kevin Haller',
    'maintainer_email': 'contact@kevinhaller.dev',
    'url': 'https://github.com/khaller93/pySQLiteKG2Vec',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
