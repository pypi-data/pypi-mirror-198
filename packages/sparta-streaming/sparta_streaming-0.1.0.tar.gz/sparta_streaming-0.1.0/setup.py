# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sparta_streaming']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'sparta-streaming',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'alexander.rembridge',
    'author_email': 'alexander.rembridge@spartacommodities.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
