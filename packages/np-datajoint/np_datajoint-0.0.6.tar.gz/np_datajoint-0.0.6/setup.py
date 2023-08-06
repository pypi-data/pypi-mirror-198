# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['np_datajoint', 'np_datajoint.hpc']

package_data = \
{'': ['*']}

install_requires = \
['datajoint',
 'djsciops>=1.5',
 'fabric>=2,<3',
 'ipywidgets',
 'np_logging',
 'np_session',
 'numpy>=1,<2',
 'pandas>=1,<2',
 'requests',
 'seaborn',
 'setuptools>=67.4.0,<68.0.0']

setup_kwargs = {
    'name': 'np-datajoint',
    'version': '0.0.6',
    'description': 'Tools for spike-sorting Mindscope neuropixels ecephys sessions on DataJoint, retrieving results and comparing with locally-sorted equivalents.',
    'long_description': 'Tools for spike-sorting Mindscope neuropixels ecephys sessions on DataJoint, retrieving results and comparing with locally-sorted equivalents.',
    'author': 'Ben Hardcastle',
    'author_email': 'ben.hardcastle@alleninstitute.org',
    'maintainer': 'Ben Hardcastle',
    'maintainer_email': 'ben.hardcastle@alleninstitute.org',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
