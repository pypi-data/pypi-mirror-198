# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['algokit_utils']

package_data = \
{'': ['*']}

install_requires = \
['py-algorand-sdk>=2.0.0,<3.0.0', 'pyteal>=0.23.0,<0.24.0']

setup_kwargs = {
    'name': 'algokit-utils',
    'version': '0.0.0',
    'description': 'Utilities for Algorand development for use by AlgoKit',
    'long_description': '# algokit-utils-py',
    'author': 'Algorand Foundation',
    'author_email': 'contact@algorand.foundation',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
