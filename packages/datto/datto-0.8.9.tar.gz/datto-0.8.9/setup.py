# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datto', 'datto.data']

package_data = \
{'': ['*']}

install_requires = \
['catboost>=1.1.1,<2.0.0',
 'gensim==3.7.3',
 'hypothesis>=6.70.0,<7.0.0',
 'jupytext>=1.14.5,<2.0.0',
 'lime>=0.2.0,<0.3.0',
 'nbconvert>=7.2.10,<8.0.0',
 'nltk>=3.8.1,<4.0.0',
 'numpy==1.23.5',
 'pandas>=1.5.3,<2.0.0',
 'progressbar>=2.5,<3.0',
 'psycopg2-binary>=2.9.5,<3.0.0',
 'pytest>=7.2.2,<8.0.0',
 'python-json-logger>=2.0.7,<3.0.0',
 's3fs>=2023.3.0,<2024.0.0',
 'scikit-learn==1.1.3',
 'seaborn>=0.12.2,<0.13.0',
 'slack-client>=0.3.0,<0.4.0',
 'slack-sdk>=3.20.2,<4.0.0',
 'spacy>=3.5.1,<4.0.0',
 'sphinx-rtd-theme>=1.2.0,<2.0.0',
 'statsmodels>=0.13.5,<0.14.0',
 'tabulate>=0.9.0,<0.10.0',
 'xgboost>=1.7.4,<2.0.0']

extras_require = \
{'docs': ['sphinx>=4.3.0,<5.0.0']}

setup_kwargs = {
    'name': 'datto',
    'version': '0.8.9',
    'description': 'Data Tools (Dat To)',
    'long_description': None,
    'author': 'kristiewirth',
    'author_email': 'kristie.ann.wirth@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
