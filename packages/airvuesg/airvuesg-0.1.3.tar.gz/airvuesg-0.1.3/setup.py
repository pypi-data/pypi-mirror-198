# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['airvue_sg']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.12.0,<5.0.0',
 'boto3>=1.26.96,<2.0.0',
 'google-api-python-client>=2.82.0,<3.0.0',
 'lxml>=4.9.2,<5.0.0',
 'oauth2client>=4.1.3,<5.0.0',
 'python-dateutil>=2.8.2,<3.0.0']

setup_kwargs = {
    'name': 'airvuesg',
    'version': '0.1.3',
    'description': 'Library to access Gmail using credentials stored in S3, using boto3',
    'long_description': 'airvue_sg',
    'author': 'Airvue',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
