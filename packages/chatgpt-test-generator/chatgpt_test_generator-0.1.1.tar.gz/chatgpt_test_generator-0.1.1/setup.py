# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chatgpt_test_generator']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.27.2,<0.28.0',
 'pytest>=7.2.2,<8.0.0',
 'setuptools>=67.6.0,<68.0.0',
 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'chatgpt-test-generator',
    'version': '0.1.1',
    'description': 'AI based test generation tool.',
    'long_description': '## CHATGPT TEST GENERATOR\n',
    'author': 'Furkan Melih Ercan',
    'author_email': 'furkan.ercan@b2metric.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
