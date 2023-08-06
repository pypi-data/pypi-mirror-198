# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['envless']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'envless',
    'version': '0.1.0',
    'description': 'Declare your python dependencies inside your scripts',
    'long_description': None,
    'author': 'Colin Fuller',
    'author_email': 'colin@cjf.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
