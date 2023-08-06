# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['xtracture']

package_data = \
{'': ['*']}

install_requires = \
['google-cloud-vision>=3.4.0,<4.0.0',
 'langchain>=0.0.117,<0.0.118',
 'openai>=0.27.2,<0.28.0']

setup_kwargs = {
    'name': 'xtracture',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Extracture\n',
    'author': 'ryo.ishii',
    'author_email': 'ryoishii1101@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
