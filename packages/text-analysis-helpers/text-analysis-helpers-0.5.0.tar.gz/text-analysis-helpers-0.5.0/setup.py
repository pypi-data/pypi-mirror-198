# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['text_analysis_helpers',
 'text_analysis_helpers.keywords',
 'text_analysis_helpers.processors']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=0.15.5,<1.0.0',
 'article-extraction>=0.3.0,<0.4.0',
 'extruct>=0.13.0,<1.0.0',
 'nltk>=3.3,<4.0',
 'numpy>=1.15.2,<2.0.0',
 'requests>=2.26.0,<3.0.0',
 'sumy>=0.11.0,<1.0.0',
 'textstat>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['text-analysis-helpers-cli = '
                     'text_analysis_helpers.cli:main']}

setup_kwargs = {
    'name': 'text-analysis-helpers',
    'version': '0.5.0',
    'description': 'Collection of classes and functions for text analysis',
    'long_description': '# Introduction\n\nText-analysis-helpers is a collection of classes and functions for text analysis.\n\n# Installation\n\nA Python 3 interpreter is required. It is recommended to install the package in\na virtual environment in order to avoid corrupting the system\'s Python interpreter\npackages.\n\nInstall the package using pip.\n\n```bash\npip install text-analysis-helpers\n\npython -m nltk.downloader "punkt"\npython -m nltk.downloader "averaged_perceptron_tagger"\npython -m nltk.downloader "maxent_ne_chunker"\npython -m nltk.downloader "words"\npython -m nltk.downloader "stopwords"\n```\n\n# Usage\n\nYou can use the HtmlAnalyser object to analyse the contents of a url.\n\n```python\nfrom text_analysis_helpers.html import HtmlAnalyser\n\nanalyser = HtmlAnalyser()\nanalysis_result = analyser.analyse_url("https://www.bbc.com/sport/formula1/64983451")\n\nanalysis_result.save("analysis_result.json")\n```\n\nYou can see the scripts in the `examples` folder for some usage examples.\n\nThere is also an cli utility that can be used to analyse a url. For example to\nanalyse a url and save the analysis result to a json encoded file execute the\nfollowing command in the terminal.\n\n```bash\ntext-analysis-helpers-cli analyse-url --output analysis_result.json https://www.bbc.com/sport/formula1/64983451\n```\n',
    'author': 'Matigakis Panagiotis',
    'author_email': 'pmatigakis@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pmatigakis/text-analysis-helpers',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
