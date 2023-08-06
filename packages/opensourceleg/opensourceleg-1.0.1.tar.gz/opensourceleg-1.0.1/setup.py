# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['opensourceleg']

package_data = \
{'': ['*']}

install_requires = \
['flexsea>=8.0.1,<9.0.0',
 'numpy>=1.22.3,<2.0.0',
 'pyserial>=3.5,<4.0',
 'pytermtk>=0.22.0a4,<0.23.0',
 'smbus2>=0.4.2,<0.5.0',
 'sphinx>=6.1.3,<7.0.0']

setup_kwargs = {
    'name': 'opensourceleg',
    'version': '1.0.1',
    'description': 'An open-source software library for numerical computation, data acquisition, and control of lower-limb robotic prosthesis.',
    'long_description': '# opensourceleg\n\n<div align="center">\n\n[![Build status](https://github.com/imsenthur/opensourceleg/workflows/build/badge.svg?branch=master&event=push)](https://github.com/imsenthur/opensourceleg/actions?query=workflow%3Abuild)\n[![Documentation Status](https://readthedocs.org/projects/opensourceleg/badge/?version=latest)](https://opensourceleg.readthedocs.io/en/latest/?badge=latest)\n[![Python Version](https://img.shields.io/pypi/pyversions/opensourceleg.svg)](https://pypi.org/project/opensourceleg/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/imsenthur/opensourceleg/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/imsenthur/opensourceleg/blob/master/.pre-commit-config.yaml)\n[![License](https://img.shields.io/github/license/imsenthur/opensourceleg)](https://github.com/imsenthur/opensourceleg/blob/master/LICENSE)\n![Coverage Report](assets/images/coverage.svg)\n\nAn open-source software library for numerical computation, data acquisition, and control of lower-limb robotic prosthesis.\n',
    'author': 'Open-source Leg',
    'author_email': 'opensourceleg@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/neurobionics/opensourceleg',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0.0',
}


setup(**setup_kwargs)
