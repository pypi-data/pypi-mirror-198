# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['archimedes_config', 'archimedes_config.utils', 'archimedes_config.workflows']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'cryptography>=39.0.1,<40.0.0', 'toml>=0.10.2,<0.11.0']

extras_require = \
{'azure-keyvault': ['azure-keyvault-secrets', 'azure-identity']}

entry_points = \
{'console_scripts': ['arckeyl = archimedes_config.arckeyl:cli']}

setup_kwargs = {
    'name': 'archimedes-config',
    'version': '0.1.6',
    'description': '',
    'long_description': 'None',
    'author': 'BigyaPradhan',
    'author_email': 'bigya.pradhan@optimeering.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<3.12',
}


setup(**setup_kwargs)
