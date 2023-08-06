# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_konf', 'py_konf.sources', 'py_konf.test', 'py_konf.test.sources']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py-konf',
    'version': '0.1.2',
    'description': 'Simple lib for loading run configurations',
    'long_description': '# py-konf\n\nA pure python library for gathering program run configuration\nfrom the user/environment\n',
    'author': 'Jordan Paoletti',
    'author_email': 'jordanspaoletti@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
