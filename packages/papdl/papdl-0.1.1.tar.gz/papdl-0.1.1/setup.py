# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['papdl',
 'papdl.backend',
 'papdl.backend.containers.Benchmarker.app',
 'papdl.backend.containers.Orchestrator.app',
 'papdl.backend.containers.Orchestrator.app.proto',
 'papdl.backend.containers.Slice.app',
 'papdl.backend.containers.Slice.app.proto',
 'papdl.benchmark',
 'papdl.clean',
 'papdl.configure',
 'papdl.deploy',
 'papdl.slice']

package_data = \
{'': ['*'],
 'papdl.backend': ['certificates/.stub',
                   'containers/Benchmarker/*',
                   'containers/Orchestrator/*',
                   'containers/Slice/*',
                   'registry_volume/*']}

install_requires = \
['aiohttp>=3.8.4,<4.0.0',
 'asynchttp>=0.0.4,<0.0.5',
 'asyncio>=3.4.3,<4.0.0',
 'asyncstdlib>=3.10.5,<4.0.0',
 'autopep8>=2.0.1,<3.0.0',
 'click>=8.1.3,<9.0.0',
 'colorama>=0.4.6,<0.5.0',
 'coloredlogs>=15.0.1,<16.0.0',
 'crossplane>=0.5.8,<0.6.0',
 'dill>=0.3.6,<0.4.0',
 'docker>=6.0.1,<7.0.0',
 'filprofiler>=2023.3.0,<2024.0.0',
 'iperf3>=0.1.11,<0.2.0',
 'ipykernel>=6.21.3,<7.0.0',
 'jsonpickle>=3.0.1,<4.0.0',
 'keras>=2.11.0,<3.0.0',
 'matplotlib>=3.7.1,<4.0.0',
 'memory-profiler>=0.61.0,<0.62.0',
 'notebook>=6.5.3,<7.0.0',
 'numpy>=1.24.1,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'psutil>=5.9.4,<6.0.0',
 'pympler>=1.0.1,<2.0.0',
 'pyopenssl>=23.0.0,<24.0.0',
 'pythonping>=1.1.4,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'random-word>=1.0.11,<2.0.0',
 'sanic>=22.12.0,<23.0.0',
 'tabulate>=0.9.0,<0.10.0',
 'tensorflow>=2.11.0,<3.0.0',
 'termcolor>=2.1.1,<3.0.0',
 'tqdm>=4.64.1,<5.0.0',
 'uproot>=5.0.4,<6.0.0',
 'websockets>=10.4,<11.0']

entry_points = \
{'console_scripts': ['papdl = papdl.cli:main']}

setup_kwargs = {
    'name': 'papdl',
    'version': '0.1.1',
    'description': '',
    'long_description': '',
    'author': 'Tamim Azmain',
    'author_email': 'maat1@st-andrews.ac.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
