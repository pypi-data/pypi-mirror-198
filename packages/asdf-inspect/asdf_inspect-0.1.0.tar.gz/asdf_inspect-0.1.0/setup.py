# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['asdf_inspect']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'asdf-inspect',
    'version': '0.1.0',
    'description': 'An auxiliary library for the virtualenv-asdf and tox-asdf-redux plugins',
    'long_description': '# asdf-inspect\n\nAn auxiliary library for the [virtualenv-asdf][virtualenv-asdf] and [tox-asdf-redux][tox-asdf-redux] plugins.\n\n## Limitations\n\nOnly CPython is supported at the moment.\n\n\nNOTE: this is modified from [pyenv-inspect][pyenv-inspect] by un-def.\n\n[pyenv-inspect]: https://github.com/un-def/pyenv-inspect\n[virtualenv-asdf]: https://github.com/lanshark/virtualenv-asdf\n[tox-asdf-redux]: https://github.com/lanshark/tox-asdf-redux\n',
    'author': 'Scott Sharkey',
    'author_email': 'me@undef.im',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lanshark/asdf-inspect',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
