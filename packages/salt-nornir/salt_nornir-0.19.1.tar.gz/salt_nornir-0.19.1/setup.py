# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['salt_nornir',
 'salt_nornir.modules',
 'salt_nornir.pillar',
 'salt_nornir.proxy',
 'salt_nornir.runners',
 'salt_nornir.states']

package_data = \
{'': ['*']}

install_requires = \
['nornir==3.3.0',
 'nornir_salt>=0.19.0,<0.20.0',
 'psutil>=5.8,<=5.9',
 'pydantic==1.10.2']

extras_require = \
{'dataprocessor': ['cerberus==1.3.4',
                   'jmespath==1.0.1',
                   'ntc-templates>=3.0.0,<4.0.0',
                   'pyyaml==6.0',
                   'tabulate==0.9.0',
                   'ttp>=0.9.0,<0.10.0',
                   'ttp-templates>=0.3.0,<0.4.0',
                   'xmltodict==0.13.0',
                   'lxml==4.9.2'],
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
 'netbox': ['pynetbox==7.0.0'],
 'netconf': ['ncclient==0.6.13', 'scrapli-netconf==2022.07.30'],
 'netmiko': ['netmiko==4.1.2', 'nornir-netmiko==0.2.0'],
 'prodmax': ['cerberus==1.3.4',
             'jmespath==1.0.1',
             'napalm==4.0.0',
             'ncclient==0.6.13',
             'netmiko==4.1.2',
             'nornir-napalm==0.3.0',
             'nornir-netmiko==0.2.0',
             'nornir-scrapli==2022.07.30',
             'ntc-templates>=3.0.0,<4.0.0',
             'paramiko==2.12.0',
             'pygnmi==0.8.9',
             'pynetbox==7.0.0',
             'pyyaml==6.0',
             'puresnmp[crypto]==2.0.0',
             'requests==2.28.1',
             'scrapli==2022.07.30',
             'scrapli-community==2022.07.30',
             'scrapli-netconf==2022.07.30',
             'tabulate==0.9.0',
             'ttp>=0.9.0,<0.10.0',
             'ttp-templates>=0.3.0,<0.4.0',
             'xmltodict==0.13.0',
             'textfsm==1.1.2',
             'jinja2==3.1.2',
             'rich==12.6.0',
             'N2G>=0.3.0,<0.4.0',
             'robotframework==6.0.2',
             'dnspython==2.3.0'],
 'prodmax:sys_platform != "win32"': ['genie[full]==22.1', 'pyats[full]==22.1'],
 'prodmin': ['ncclient==0.6.13',
             'netmiko==4.1.2',
             'nornir-netmiko==0.2.0',
             'paramiko==2.12.0',
             'requests==2.28.1',
             'tabulate==0.9.0',
             'ttp>=0.9.0,<0.10.0',
             'ttp-templates>=0.3.0,<0.4.0',
             'xmltodict==0.13.0',
             'textfsm==1.1.2',
             'jinja2==3.1.2',
             'rich==12.6.0'],
 'pyats:sys_platform != "win32"': ['genie[full]==22.1', 'pyats[full]==22.1'],
 'restconf': ['requests==2.28.1'],
 'scrapli': ['scrapli==2022.07.30', 'scrapli-community==2022.07.30']}

entry_points = \
{'salt.loader': ['module_dirs = salt_nornir.loader:module_dirs',
                 'pillar_dirs = salt_nornir.loader:pillar_dirs',
                 'proxy_dirs = salt_nornir.loader:proxy_dirs',
                 'runner_dirs = salt_nornir.loader:runner_dirs',
                 'states_dirs = salt_nornir.loader:states_dirs']}

setup_kwargs = {
    'name': 'salt-nornir',
    'version': '0.19.1',
    'description': 'Salt-Nornir Proxy Minion SaltStack Modules',
    'long_description': '[![Downloads][pepy-downloads-badge]][pepy-downloads-link]\n[![PyPI][pypi-latest-release-badge]][pypi-latest-release-link]\n[![PyPI versions][pypi-versions-badge]][pypi-versions-link]\n[![GitHub Discussion][github-discussions-badge]][github-discussions-link]\n[![Code style: black][black-badge]][black-link]\n[![Documentation status][readthedocs-badge]][readthedocs-link]\n\n![logo][logo]\n\n# Salt Nornir\n\nNornir centered SaltStack modules:\n\n- salt-nornir proxy minion module\n- salt-nornir execution module\n- salt-nornir state module\n- salt-nornir runner module\n- salt-nornir Netbox pillar module\n\nNornir Proxy Minion helps to manage network devices at scale, refer to\n[documentation](https://salt-nornir.readthedocs.io/en/latest/index.html)\nfor details.\n\n# Architecture\n\nPython and Plugins.\n\n![architecture][architecture]\n\nNornir Proxy acts as a bridge between SaltStack and a wide set of open\nsource network automation libraries.\n\n# Features\n\n- **CLI** management of devices over SSH or Telnet using Netmiko, Scrapli, Cisco Genie/PyATS or NAPALM\n- **NETCONF** management of network devices using Ncclient or Scrapli-Netconf\n- **HTTP API**/**RESTCONF** interact with devices using Python requests library\n- **gNMI** device management supported thanks to integration with PyGNMI library\n- **SNMPv1/2/3** support to manage device using puresnmp library\n- **Data Processing** using NTC-Templates, TTP, Jmespath, lxml, xmltodict libraries\n- **Network Testing** of state and configuration via SSH, Netconf, gNMI, HTTP or SNMP\n- **Python** is a first class citizen - write plugins, modules, scripts, codify work flows\n- **API** integrate with anything using SaltStack and Nornir Python API or SaltStack HTTP API\n- **Netbox** Source of Truth inventory integration for infrastructure management\n\n# Communication and discussion\n\nNetwork To Code [salt-nornir Slack Channel](https://app.slack.com/client/T09LQ7E9E/C02MPR34DGF)\n\nOpen an [issue](https://github.com/dmulyalin/salt-nornir/issues)\n\nStart a [discussion](https://github.com/dmulyalin/salt-nornir/discussions)\n\n# Contributing\n\nIssues, bug reports and feature requests are welcomed. Feedback is a gift and we truly value it.\n\n# Developers Motto\n\n- if it is not in the docs it does not exist\n- if it is not tested it is broken\n- done is better than perfect\n- keep it stupid simple\n\n[logo]:                        docs/source/_images/SaltNornirLogo.png "salt nornir logo"\n[architecture]:                docs/source/_images/Nornir_proxy_minion_architecture_v2.png "salt nornir architecture"\n[pepy-downloads-badge]:        https://pepy.tech/badge/salt-nornir\n[pepy-downloads-link]:         https://pepy.tech/project/salt-nornir\n[pypi-versions-badge]:         https://img.shields.io/pypi/pyversions/salt-nornir.svg\n[pypi-versions-link]:          https://pypi.python.org/pypi/salt-nornir/\n[readthedocs-badge]:           https://readthedocs.org/projects/salt-nornir/badge/?version=latest\n[readthedocs-link]:            http://salt-nornir.readthedocs.io/?badge=latest\n[pypi-latest-release-badge]:   https://img.shields.io/pypi/v/salt-nornir.svg\n[pypi-latest-release-link]:    https://pypi.python.org/pypi/salt-nornir\n[github-discussions-link]:     https://github.com/dmulyalin/salt-nornir/discussions\n[github-discussions-badge]:    https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github\n[black-badge]:                 https://img.shields.io/badge/code%20style-black-000000.svg\n[black-link]:                  https://github.com/psf/black\n[github-tests-badge]:          https://github.com/dmulyalin/salt-nornir/actions/workflows/main.yml/badge.svg\n[github-tests-link]:           https://github.com/dmulyalin/salt-nornir/actions\n',
    'author': 'Denis Mulyalin',
    'author_email': 'd.mulyalin@gmail.com',
    'maintainer': 'Denis Mulyalin',
    'maintainer_email': 'd.mulyalin@gmail.com',
    'url': 'https://github.com/dmulyalin/salt-nornir',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
