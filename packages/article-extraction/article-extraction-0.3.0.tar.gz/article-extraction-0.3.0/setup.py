# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['articles', 'articles.mss']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.7.1']

setup_kwargs = {
    'name': 'article-extraction',
    'version': '0.3.0',
    'description': 'Article text extraction library',
    'long_description': '# Article extraction library.\n\narticle-extraction is a package that can be used to extract the article content\nfrom an HTML page.\n\n# Installation\n\nUse poetry to install the library from GitHub.\n\n```bash\npoetry add "git+https://github.com/pmatigakis/article-extraction.git"\n```\n\n# Usage\n\nExtract the content of an article using article-extraction.\n\n```python\nfrom urllib.request import urlopen\n\nfrom articles.mss.extractors import MSSArticleExtractor\n\ndocument = urlopen("https://www.bbc.com/sport/formula1/64983451").read()\narticle_extractor = MSSArticleExtractor()\narticle = article_extractor.extract_article(document)\nprint(article)\n```\n',
    'author': 'Matigakis Panagiotis',
    'author_email': 'pmatigakis@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pmatigakis/article-extraction',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
