# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['refuge']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'refuge',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Refuge\n',
    'author': 'Alex Carpenter',
    'author_email': 'alex@refuge.au',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
