# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'source/packages'}

packages = \
['mojo',
 'mojo.taskplus',
 'mojo.taskplus.cli',
 'mojo.taskplus.cli.cmdtree',
 'mojo.taskplus.tasks']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'mojo-runtime>=0.0.14,<0.0.15']

setup_kwargs = {
    'name': 'mojo-taskplus',
    'version': '0.0.1',
    'description': 'Automation Mojo Task Plus Library',
    'long_description': '# Automation Mojo - TaskPlus Package\nThis is a preliminary release of the TaskPlus job engine.  This is a very preliminary release and is not intended for public consumption yet.\n',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
