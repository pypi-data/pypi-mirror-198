# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['markpickle']

package_data = \
{'': ['*']}

install_requires = \
['mdformat', 'mistune']

setup_kwargs = {
    'name': 'markpickle',
    'version': '0.2.0',
    'description': 'Lossy python to markdown serializer',
    'long_description': '# markpickle\n\nLossy serialization of markdown to simple python data types and back. It will create predictable markdown from a python object, but can\'t turn all markdown files into sensible python objects (for that use a markdown library that creates an AST). I created this because I wanted a way to turn json into Markdown.\n\nFor example this\n\n```markdown\n- 1\n- 2\n```\n\nbecomes the python list `[1, 2]`\n\n![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/markpickle) [![Downloads](https://pepy.tech/badge/markpickle/month)](https://pepy.tech/project/markpickle/month)\n\n## Installation\n\n```shell\npip install openmock\n```\n\n## Capabilities\nThis is a lossy serialization. Markdown is missing too many concepts to make a high fidelity representation of a python data structure. If you want an object model that faithfully represents each object in a Markdown document, use the AST of mistune or one of the other markdown parsers.\n\nSupported types\n\n- Scalar values\n- Lists of scalar values\n- Dictionaries with scalar values\n- Lists of dictionaries of scalar values\n- Dictionaries with list values\n- Partial support for blanks/string with leading/trailing whitespace\n\nNot supported\n\n- Things not ordinarily serializable\n- Markdown that uses more than headers, lists, tables\n\n# Serializing\n\nAlmost all markdown libraries use it as intended, as a way to generate HTML fragments from untrusted sources for insertion into some other HTML template.\n\n# Deserializing\n\nMarkdown is deserialized by parsing the document to an abstract syntax tree. This is done by `mistune`. If the markdown file has the same structure that markpickle uses, then it will create a sensible object. Deserializing a random README.md file is not expected to always work. For that you should use mistune\'s AST.\n\n# Round Tripping\n\nSome but not all data structures will be round-trippable. The goal is that the sort of dicts you get from loading JSON will be round-trippable, provided everything is a string.\n\n\n## Prior Art\n\nPeople normally want to convert json to markdown. Json looks like python dict, so if you can do that you can probably do both.\n\n### Serializing to Markdown\n[json2md](https://github.com/IonicaBizau/json2md), a node package, will turn json that looks like the HTML document object model into markdown, e.g.\n```python\n{"h1": "Some Header",\n "p": "Some Text"}\n```\n\n[tomark](https://pypi.org/project/tomark/) will turn dict into a markdown table. Unmaintained.\n\n[pytablewriter](https://pytablewriter.readthedocs.io/en/latest/pages/reference/writers/text/markup/md.html) also, dict to table, but supports many tabular formats.\n\n### Deserializing to Python \n\nI don\'t know of any libraries that turn markdown into basic python types. At the moment, they all turn markdown into document object model.\n\n[mistune](https://pypi.org/project/mistune/) will turn markdown into an Abstract Syntax Tree. The AST is faithful representation of the Markdown, including concepts that have no semantic equivalent to python datatypes. \n\n[beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) will let you navigate the HTML DOM. So you can turn the markdown into HTML, then parse with Beautiful Soup. \n\n# Documentation\n\n- [Examples](https://github.com/matthewdeanmartin/markpickle/blob/main/docs/examples.md)\n- [TODO](https://github.com/matthewdeanmartin/markpickle/blob/main/docs/TODO.md)\n\n\n',
    'author': 'Matthew Martin',
    'author_email': 'matthewdeanmartin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/matthewdeanmartin/markpickle',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
