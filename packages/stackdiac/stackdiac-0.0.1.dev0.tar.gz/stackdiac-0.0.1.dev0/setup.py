# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stackdiac', 'stackdiac.cli', 'stackdiac.models']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'coloredlogs>=15.0.1,<16.0.0',
 'deepmerge>=1.1.0,<2.0.0',
 'gitpython>=3.1.31,<4.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'pydantic>=1.10.6,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'requests>=2.28.2,<3.0.0']

entry_points = \
{'console_scripts': ['stackd = stackdiac.cli:cli']}

setup_kwargs = {
    'name': 'stackdiac',
    'version': '0.0.1.dev0',
    'description': '',
    'long_description': '# Stackd IAC\n\nIAC organizer\n\n## Usage\n\n### initializing project\n\n~~~\n$ stackd init\n~~~\n\nAdd --help for usage message. Initalizes new project in current directory. Clones core specifications,\nterraform provider versions, setups vault. \n\n\n\n#### AWS S3 + KMS storage -- uses your own resources\n\n- S3 buckets for terraform states and vault data files\n- AWS KMS encryption key for vault unsealing and S3 server-side encryption\n\nalso, stackd can create this objects automatically, when initial credentials are provided\n\n## Building infrastructure code\n\n~~~\n$ stackd build -c all\n~~~\n\nBuilds IAC specifications for all configured clusters',
    'author': 'sysr9',
    'author_email': '38893296+sysr9@users.noreply.github.com',
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
