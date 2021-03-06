# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['imdbscraper', 'imdbscraper.imdb', 'imdbscraper.tests']

package_data = \
{'': ['*']}

install_requires = \
['DateTime>=4.3,<5.0',
 'beautifulsoup4>=4.9.3,<5.0.0',
 'html5lib>=1.1,<2.0',
 'lxml>=4.6.3,<5.0.0',
 'numpy>=1.21.0,<2.0.0',
 'pandas>=1.2.5,<2.0.0',
 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'imdbscraper',
    'version': '0.1.1',
    'description': 'A web scraper to extract data from IMDb',
    'long_description': None,
    'author': 'Federico GarcÝa',
    'author_email': 'garciafedericoagustin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)

