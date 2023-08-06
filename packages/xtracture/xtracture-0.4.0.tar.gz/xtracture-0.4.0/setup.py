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
 'openai>=0.27.2,<0.28.0',
 'pyocr>=0.8.3,<0.9.0']

setup_kwargs = {
    'name': 'xtracture',
    'version': '0.4.0',
    'description': 'Xtracture is an open source library designed to efficiently extract arbitrary elements from documents.',
    'long_description': '# Xtracture: Open Source Document Content Extractuion Library\n\nXtracture is an open source library designed to efficiently extract arbitrary elements from documents.\n\n## Features\n\n- Natural language rule creation using LLMs\n- Switchable OCR engines for optimized perfomance and accuracy\n\n## prerequirements\n\n- OpenAI API Key (for LLM rule creation)\n\n## Installation\n\n```\npip install -U xtracture\n```\n\n## Usage\n\n### Use Google Cloud Vision API\n\nGoogle CLoud Vision Credentials must be correctly configured.\n\nsee `examples/google_cloud_vision_example.py`.\n\n### Use Tesseract\n\nTesseract must be installed beforehand.\n\nsee `examples/tesseract_example.py`.\n\n### Use only GPT Extractor\n\nYou can input OCR-processed text file.\nsee `examples/lambda_example.py`.\n\n## License\n\nXtracture is released under the MIT License.\n',
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
