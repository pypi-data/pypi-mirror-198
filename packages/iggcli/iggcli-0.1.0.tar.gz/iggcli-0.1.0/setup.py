# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iggcli', 'iggcli.calls', 'iggcli.core', 'iggcli.values']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.12.0,<5.0.0',
 'python-slugify>=8.0.1,<9.0.0',
 'requests>=2.28.2,<3.0.0',
 'rich>=13.3.2,<14.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['iggcli = iggcli.main:main']}

setup_kwargs = {
    'name': 'iggcli',
    'version': '0.1.0',
    'description': 'Download your games from Igg Games more easily.',
    'long_description': '# IggCli\n\nIn development\n',
    'author': 'Alekyo4',
    'author_email': 'alexsandergomes4742@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
