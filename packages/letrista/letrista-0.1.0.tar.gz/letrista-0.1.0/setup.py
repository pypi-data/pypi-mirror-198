# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['letrista']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'letrista',
    'version': '0.1.0',
    'description': 'Python3 package for lyrics writing and formating.',
    'long_description': '====================================================\nLetrista |pipy-version| |build-status| |docs-status|\n====================================================\n\n\nLetrista is a markup syntax and parser system for lyrics writing, written in `Python 3 <https://www.python.org/>`_. It allows the use of comments and useful notes for lyrics drafts, such as rhyme scheme and syllable count.\n\nThe output of this parser is in `marke37 <https://github.com/ramoscarlos/marke37>`_ format, which is a modified version of the Markdown syntax. This output can be processed further if needed into a more common and visual format (mainly HTML).\n\nThe primary goal of this package is to aid the lyricists/songwriters (mainly myself) to concentrate on the actual content that will remain on the lyrics, while also leaving the options available within the same file (for if those are needed to compare or restore).\n\nThe ideal usage of this package is with a real-time editing tool, like within the Sublime Text editor, with the `Letrista Sublime <https://github.com/ramoscarlos/letrista_sublime>`_ plugin, but the module is provided for inclusion in other projects.\n\nA demo editor is provided at `quick-draft.letrista.app <https://quick-draft.letrista.app/>`_, with an already populated `example in English <https://quick-draft.letrista.app/example>`_ and `one in Spanish <https://quick-draft.letrista.app/ejemplo>`_.\n\nThe module is released under the MIT license, so you can pretty much what you want with it. For the full documentation, visit `Read The Docs <https://letrista.readthedocs.io>`_.\n\n\n.. ###\n.. Substitutions\n.. ################\n\n.. |pipy-version| image:: https://img.shields.io/pypi/v/letrista.svg\n   :target: https://pypi.python.org/pypi/letrista\n   :alt: PiPy Version\n\n.. |build-status| image:: https://img.shields.io/travis/ramoscarlos/letrista.svg\n   :target: https://travis-ci.com/ramoscarlos/letrista\n   :alt: Build Status\n\n.. |docs-status| image:: https://readthedocs.org/projects/letrista/badge/?version=latest\n   :target: https://letrista.readthedocs.io/en/latest/?version=latest\n   :alt: Documentation Status\n',
    'author': 'Carlos Ramos',
    'author_email': 'carlos@ramoscarlos.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
