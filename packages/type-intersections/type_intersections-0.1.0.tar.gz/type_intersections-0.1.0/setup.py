# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['type_intersections']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'type-intersections',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Stanislav Zmiev',
    'author_email': 'szmiev2000@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
