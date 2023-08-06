# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['libsimba', 'libsimba.auth']

package_data = \
{'': ['*']}

install_requires = \
['httpx==0.23.0', 'pydantic[dotenv]==1.10.2']

setup_kwargs = {
    'name': 'libsimba',
    'version': '0.1.16',
    'description': 'libsimba is a library simplifying the use of SIMBAChain Blocks APIs.',
    'long_description': 'None',
    'author': 'SIMBA Chain Inc.',
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
