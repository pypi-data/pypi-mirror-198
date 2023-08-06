# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['katia',
 'katia.interpreter',
 'katia.logger_manager',
 'katia.message_manager',
 'katia.recognizer',
 'katia.speaker']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML==6.0',
 'boto3==1.26.90',
 'confluent-kafka==2.0.2',
 'googletrans==3.1.0a0',
 'openai==0.27.2',
 'pyaudio==0.2.13',
 'pygame==2.2.0',
 'python-dotenv==1.0.0',
 'speechrecognition==3.9.0']

setup_kwargs = {
    'name': 'katia',
    'version': '0.0.1',
    'description': 'Katia is a wonderfull assistant created for help people to iteract with the digital world',
    'long_description': None,
    'author': 'martingaldeca',
    'author_email': 'martingaldeca@gmail.com',
    'maintainer': 'martingaldeca',
    'maintainer_email': 'martingaldeca@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.0,<4.0.0',
}


setup(**setup_kwargs)
