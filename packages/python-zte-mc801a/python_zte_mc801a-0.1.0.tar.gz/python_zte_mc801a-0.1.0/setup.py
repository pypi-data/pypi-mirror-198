# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_zte_mc801a', 'python_zte_mc801a.client', 'python_zte_mc801a.lib']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=6.0,<7.0',
 'requests>=2.28.2,<3.0.0',
 'retry>=0.9.2,<0.10.0',
 'termplotlib>=0.3.9,<0.4.0',
 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['python-zte-mc801a = python_zte_mc801a.main:app']}

setup_kwargs = {
    'name': 'python-zte-mc801a',
    'version': '0.1.0',
    'description': '',
    'long_description': '# python-zte-mc801a\n\n## What is this?\n\nThis is a library and a simple CLI client application to interact with the ZTE MC801A router. The idea is to provide read access to the data made available by the firmware and, in the future, provide functionality to carry out actions such as cell or band locking.\n\nOriginal idea and inspiration for this project was the very helpful Javascript code provided by [Miononno](https://miononno.it/).\n\n## ⚠️ Warning\n\nThis is not an official client for the router. While most READ operations are likely to be safe, WRITE operations such as cell locking could lead to router malfunction or, in extreme cases, render the device inoperable.\n\n## Features\n\nThe table below summarizes the features currently implemented and those being worked on.\n\n| Feature                    | Type  | Status |\n| -------------------------- | ----- | ------ |\n| Cell information           | READ  | ✅     |\n| Network information        | READ  | ✅     |\n| 4G signal data             | READ  | ✅     |\n| 5G signal data             | READ  | ✅     |\n| Carrier Aggregation status | READ  | ✅     |\n| SMS view                   | READ  | ✅     |\n| 4G band locking            | WRITE | WIP    |\n| 5G band locking            | WRITE | ✅     |\n| Cell locking               | WRITE | WIP    |\n\n## Compatibility\n\n| Firmware                | Operator | Status               |\n| ----------------------- | -------- | -------------------- |\n| BD_UKH3GMC801AV1.0.0B15 | Three UK | All features working |\n\n## Getting Started\n\n### Installation\n\n## Install Poetry\n\nCOMING SOON\n',
    'author': 'Nicolas Jaccard',
    'author_email': 'nicolas.jaccard@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nicjac/python-zte-mc801a',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
