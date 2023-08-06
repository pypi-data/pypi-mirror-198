# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['packages',
 'packages.testplus',
 'packages.testplus.cli',
 'packages.testplus.cli.cmdtree',
 'packages.testplus.cli.cmdtree.testing',
 'packages.testplus.registration']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'debugpy>=1.6.5,<2.0.0', 'mojo-runtime>=0.0.14,<0.0.15']

setup_kwargs = {
    'name': 'mojo-testplus',
    'version': '0.0.2',
    'description': 'Automation Mojo TestPlus Test Framework',
    'long_description': "# Automation Mojo - Testplus \nThis is preliminary release of the 'testplus' automation framework in a separate package from\nthe AutomationKit.  This release is not ready for public consumption.\n\n",
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
