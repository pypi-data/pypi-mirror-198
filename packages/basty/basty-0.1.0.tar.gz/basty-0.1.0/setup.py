# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['basty',
 'basty.behavior_mapping',
 'basty.experiment_processing',
 'basty.feature_extraction',
 'basty.project',
 'basty.utils']

package_data = \
{'': ['*']}

install_requires = \
['PyWavelets>=1.2.0,<2.0.0',
 'PyYAML==6.0',
 'filterpy==1.4.5',
 'hdbscan==0.8.28',
 'joblib==1.1.0',
 'numpy==1.21.5',
 'pandas==1.3.5',
 'scikit-learn==1.1.1',
 'scipy==1.8.0',
 'tqdm==4.63.0',
 'umap-learn==0.5.2']

setup_kwargs = {
    'name': 'basty',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Ali Osman Berk Şapcı',
    'author_email': 'aliosmanberk@sabanciuniv.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.9.0',
}


setup(**setup_kwargs)
