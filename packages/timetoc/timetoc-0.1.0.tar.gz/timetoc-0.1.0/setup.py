# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['timetoc']

package_data = \
{'': ['*']}

install_requires = \
['holidays>=0.21.13,<0.22.0',
 'pandas>=1.5.3,<2.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'requests>=2.28.2,<3.0.0',
 'selenium-wire>=5.1.0,<6.0.0',
 'typer[all]>=0.7.0,<0.8.0',
 'webdriver-manager>=3.8.5,<4.0.0']

entry_points = \
{'console_scripts': ['timetoc = timetoc.cli:app']}

setup_kwargs = {
    'name': 'timetoc',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Guilherme Prokisch',
    'author_email': 'guilherme.prokisch@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
