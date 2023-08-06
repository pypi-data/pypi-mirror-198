# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scrapse', 'scrapse.leggitalia', 'scrapse.leggitalia.commands']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.2,<5.0.0',
 'numpy>=1.24.2,<2.0.0',
 'requests>=2.28.2,<3.0.0',
 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['scrapse = scrapse.main:app']}

setup_kwargs = {
    'name': 'scrapse',
    'version': '0.3.6',
    'description': 'Package to download and manage judgments',
    'long_description': "# ScrapSE\n\n## Package description\n\nScrapSE downloads and manage the judgments.\n\nCurrently supported platforms: LEGGI D'ITALIA PA.\n\n### Install scrapse\n```\npip install scrapse\n```\nThe package creates the `scrapse` folder in `/Users/your_username`, where it will save all judgments in the  \nappropriate subfolders.\n\n### How to use\n\n#### Saving cookies - important!\n```\nscrapse leggitalia save-cookie 'your_cokies'\n```\nThis command saves session cookies in a special file, containing  `your_cookie`.\n\n#### Show filter values\n```\nscrapse leggitalia show-filters\n```\nThis command shows the possible values to be assigned to sentence search filters.\n\n#### Download the judgments\nMake sure you have **saved** platform-related cookies before downloading the judgments!.\n```\nscrapse leggitalia scrap-judgments -l torino -s 'Sez. lavoro, Sez. V'\n```\nThis command creates a folder in `/Users/your_username/scrapse` named `sez.lavoro&sez.v_torino` containing the judgments.\n\n#### Dump judgments to json format\n```\nscrapse leggitalia dump-judgments -d 'folder_path'\n```\nThis command creates the json files by saving them in the `/Users/your_username/scrapse/judgments_dump` folder.\n\n#### For more help\nFor more information for each command.\n```\ncommand-name --help\n```\n",
    'author': 'zaharia laurentiu jr marius',
    'author_email': 'zaharialorenzo@gmail.com',
    'maintainer': 'zaharia laurentiu jr marius',
    'maintainer_email': 'zaharialorenzo@gmail.com',
    'url': 'https://gitlab.di.unito.it/ngupp/ngupp-scrapse',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
