# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['letloopit']
install_requires = \
['requests>=2.28.2,<3.0.0']

entry_points = \
{'console_scripts': ['letloop.py = letloopit:main']}

setup_kwargs = {
    'name': 'letloop.py',
    'version': '0.1.2',
    'description': 'A cloud for the parenthetical leaning doers',
    'long_description': None,
    'author': 'Amir',
    'author_email': 'amirouche@hyper.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/letloop/letloop.cloud/',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
