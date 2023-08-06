# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['license_seeker',
 'license_seeker.apis',
 'license_seeker.apis.converters',
 'license_seeker.apis.parsers']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0']

entry_points = \
{'console_scripts': ['license-seeker = license_seeker.main:main']}

setup_kwargs = {
    'name': 'license-seeker',
    'version': '0.3.1',
    'description': '',
    'long_description': 'license-seeker\n==============\n\nlicense-seeker is the application that will help you to find licenses of\nthe projects, libraries, …\n\nAuthor\n======\n\nKostiantyn Klochko (c) 2023\n\nLicense\n=======\n\nUnder GNU GPL v3 license\n',
    'author': 'KKlochko',
    'author_email': 'kostya_klochko@ukr.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/KKlochko/license-seeker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
