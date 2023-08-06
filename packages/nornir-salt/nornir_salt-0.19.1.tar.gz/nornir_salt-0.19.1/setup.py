# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nornir_salt',
 'nornir_salt.plugins',
 'nornir_salt.plugins.connections',
 'nornir_salt.plugins.functions',
 'nornir_salt.plugins.inventory',
 'nornir_salt.plugins.processors',
 'nornir_salt.plugins.runners',
 'nornir_salt.plugins.tasks',
 'nornir_salt.utils']

package_data = \
{'': ['*']}

install_requires = \
['nornir==3.3.0', 'pydantic==1.10.2']

extras_require = \
{'dataprocessor': ['cerberus==1.3.4',
                   'jmespath==1.0.1',
                   'ntc-templates>=3.0.0,<4.0.0',
                   'pyyaml==6.0',
                   'tabulate==0.8.10',
                   'ttp>=0.9.0,<0.10.0',
                   'ttp-templates>=0.3.0,<0.4.0',
                   'xmltodict==0.13.0',
                   'lxml==4.9.1'],
 'docs': ['readthedocs-sphinx-search==0.1.1',
          'Sphinx==4.3.0',
          'sphinx_rtd_theme==1.0.0',
          'sphinxcontrib-applehelp==1.0.1',
          'sphinxcontrib-devhelp==1.0.1',
          'sphinxcontrib-htmlhelp==2.0.0',
          'sphinxcontrib-jsmath==1.0.1',
          'sphinxcontrib-napoleon==0.7',
          'sphinxcontrib-qthelp==1.0.2',
          'sphinxcontrib-serializinghtml==1.1.5',
          'sphinxcontrib-spelling==7.2.1'],
 'gnmi': ['pygnmi==0.8.9'],
 'napalm': ['napalm==4.0.0', 'nornir-napalm==0.3.0'],
 'netconf': ['ncclient==0.6.13', 'scrapli-netconf==2022.07.30'],
 'netmiko': ['netmiko==4.1.1', 'nornir-netmiko==0.2.0'],
 'prodmax': ['cerberus==1.3.4',
             'jmespath==1.0.1',
             'napalm==4.0.0',
             'ncclient==0.6.13',
             'netmiko==4.1.1',
             'nornir-napalm==0.3.0',
             'nornir-netmiko==0.2.0',
             'nornir-scrapli==2022.07.30',
             'ntc-templates>=3.0.0,<4.0.0',
             'paramiko==2.11.0',
             'pygnmi==0.8.9',
             'pyyaml==6.0',
             'puresnmp[crypto]==2.0.0',
             'requests==2.28.1',
             'scrapli==2022.07.30',
             'scrapli-community==2022.07.30',
             'scrapli-netconf==2022.07.30',
             'tabulate==0.8.10',
             'ttp>=0.9.0,<0.10.0',
             'ttp-templates>=0.3.0,<0.4.0',
             'xmltodict==0.13.0',
             'textfsm==1.1.2',
             'jinja2==3.1.2',
             'dnspython==2.3.0'],
 'prodmax:sys_platform != "win32"': ['genie[full]==22.1', 'pyats[full]==22.1'],
 'prodmin': ['ncclient==0.6.13',
             'netmiko==4.1.1',
             'nornir-netmiko==0.2.0',
             'paramiko==2.11.0',
             'requests==2.28.1',
             'tabulate==0.8.10',
             'ttp>=0.9.0,<0.10.0',
             'ttp-templates>=0.3.0,<0.4.0',
             'xmltodict==0.13.0',
             'textfsm==1.1.2',
             'jinja2==3.1.2'],
 'pyats:sys_platform != "win32"': ['genie[full]==22.1', 'pyats[full]==22.1'],
 'restconf': ['requests==2.28.1'],
 'scrapli': ['scrapli==2022.07.30', 'scrapli-community==2022.07.30']}

entry_points = \
{'nornir.plugins.connections': ['ConnectionsPool = '
                                'nornir_salt.plugins.connections:ConnectionsPool',
                                'http = '
                                'nornir_salt.plugins.connections:HTTPPlugin',
                                'ncclient = '
                                'nornir_salt.plugins.connections:NcclientPlugin',
                                'puresnmp = '
                                'nornir_salt.plugins.connections:PureSNMPPlugin',
                                'pyats = '
                                'nornir_salt.plugins.connections:PyATSUnicon',
                                'pygnmi = '
                                'nornir_salt.plugins.connections:PyGNMIPlugin'],
 'nornir.plugins.inventory': ['DictInventory = '
                              'nornir_salt.plugins.inventory:DictInventory'],
 'nornir.plugins.runners': ['QueueRunner = '
                            'nornir_salt.plugins.runners:QueueRunner',
                            'RetryRunner = '
                            'nornir_salt.plugins.runners:RetryRunner']}

setup_kwargs = {
    'name': 'nornir-salt',
    'version': '0.19.1',
    'description': 'Nornir plugins used with SaltStack Salt-Nornir Proxy Minion',
    'long_description': '[![Downloads][pepy-downloads-badge]][pepy-downloads-link]\n[![PyPI][pypi-latest-release-badge]][pypi-latest-release-link]\n[![PyPI versions][pypi-pyversion-badge]][pypi-pyversion-link]\n[![GitHub Discussion][github-discussions-badge]][github-discussions-link]\n[![Code style: black][black-badge]][black-link]\n[![Documentation status][readthedocs-badge]][readthedocs-link]\n[![Tests][github-tests-badge]][github-tests-link]\n\n# nornir-salt\n\nCollection of Nornir plugins for [SALTSTACK Nornir Proxy Minion modules](https://github.com/dmulyalin/salt-nornir).\n\nAll plugins and functions can be used with Nornir directly unless stated otherwise.\n\nRefer to [documentation](https://nornir-salt.readthedocs.io/en/latest/) for additional information.\n\n# Contributing\n\nIssues, bug reports and feature requests are welcomed.\n\n[github-discussions-link]:     https://github.com/dmulyalin/nornir-salt/discussions\n[github-discussions-badge]:    https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github\n[black-badge]:                 https://img.shields.io/badge/code%20style-black-000000.svg\n[black-link]:                  https://github.com/psf/black\n[pypi-pyversion-link]:         https://pypi.python.org/pypi/nornir-salt/\n[pypi-pyversion-badge]:        https://img.shields.io/pypi/pyversions/nornir-salt.svg\n[pepy-downloads-link]:         https://pepy.tech/project/nornir-salt\n[pepy-downloads-badge]:        https://pepy.tech/badge/nornir-salt\n[readthedocs-link]:            http://nornir-salt.readthedocs.io/?badge=latest\n[readthedocs-badge]:           https://readthedocs.org/projects/nornir-salt/badge/?version=latest\n[github-tests-badge]:          https://github.com/dmulyalin/nornir-salt/actions/workflows/main.yml/badge.svg?branch=master\n[github-tests-link]:           https://github.com/dmulyalin/nornir-salt/actions\n[pypi-latest-release-badge]:   https://img.shields.io/pypi/v/nornir-salt.svg\n[pypi-latest-release-link]:    https://pypi.python.org/pypi/nornir-salt\n',
    'author': 'Denis Mulyalin',
    'author_email': 'd.mulyalin@gmail.com',
    'maintainer': 'Denis Mulyalin',
    'maintainer_email': 'd.mulyalin@gmail.com',
    'url': 'https://github.com/dmulyalin/nornir-salt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
