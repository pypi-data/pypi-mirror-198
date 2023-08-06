# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytotp_client']

package_data = \
{'': ['*']}

install_requires = \
['pykeychain>=1.1.0,<2.0.0', 'pyotp>=2.7.0,<3.0.0']

entry_points = \
{'console_scripts': ['totp = pytotp_client:entrypoint']}

setup_kwargs = {
    'name': 'pytotp-client',
    'version': '0.4.0',
    'description': 'TOTP client for macOS',
    'long_description': '# TOTP client for macOS\n\n- Written in Python\n- Secrets are stored in macOS keychain.\n\n## How to work with pytotp_client\n\nAdd secret to keychain\n\n```shell\ntotp add google.com BBBBDDDD\n```\n\nGet one time password\n\n```shell\ntotp get google.com\n```\n\nRemove secret from keychain\n\n```shell\ntotp delete google.com\n```\n\n## Where is my secrets stored?\n\nIn macOS default keychain.\n - Name: pytotp_client\n - Type: application password',
    'author': 'Elisei',
    'author_email': 'elisey.rav@gmail.comp',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/elisey/pytotp_client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
