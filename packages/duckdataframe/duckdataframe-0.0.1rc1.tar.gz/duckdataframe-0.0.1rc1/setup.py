# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['duckdataframe']

package_data = \
{'': ['*']}

install_requires = \
['duckdb>=0.7.1,<0.8.0', 'numpy>=1.24.2,<2.0.0', 'pandas>=1.5.3,<2.0.0']

setup_kwargs = {
    'name': 'duckdataframe',
    'version': '0.0.1rc1',
    'description': '',
    'long_description': '',
    'author': 'code-mc',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
