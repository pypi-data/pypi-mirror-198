# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['telemetry_wire']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'telemetry-wire',
    'version': '0.1.0',
    'description': 'An SDK for accessing Telemetry Wire',
    'long_description': '# Telemetry Wire\n\nComing soon.\n',
    'author': 'Chris Moyer',
    'author_email': 'chris@telemetry.fm',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
