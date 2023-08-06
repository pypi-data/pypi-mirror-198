# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['respace']

package_data = \
{'': ['*']}

install_requires = \
['xarray>=2023.01.0']

setup_kwargs = {
    'name': 'respace',
    'version': '0.1.1',
    'description': 'ReSpace',
    'long_description': '<div align="center">\n\n# ReSpace\n\n[![PyPI](https://img.shields.io/pypi/v/respace.svg)][pypi status]\n[![Status](https://img.shields.io/pypi/status/respace.svg)][pypi status]\n[![Python Version](https://img.shields.io/pypi/pyversions/respace)][pypi status]\n[![License](https://img.shields.io/pypi/l/respace)][license file]\n\n[![Read the documentation at https://respace.readthedocs.io/](https://img.shields.io/readthedocs/respace/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/TLouf/respace/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/TLouf/respace/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)][ruff]\n\n[pypi status]: https://pypi.org/project/respace/\n[license file]: https://github.com/TLouf/respace/blob/main/LICENSE\n[read the docs]: https://respace.readthedocs.io/\n[tests]: https://github.com/TLouf/respace/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/TLouf/respace\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n[ruff]: https://github.com/charliermarsh/ruff\n\n</div>\n\nReSpace is a Python package that allows you to keep track of the results of different\ncomputations along with the parameter values that generated them. You specify their\nnames, the function that generates them, the name and default values of the parameters\nthey depend on and you\'re good to go: no more trying to remember what parameters this\nvalue was computed for, building dictionaries of dictionaries (of dictionaries) to\nstore them, or generally worrying about these things.\n\n\n## Features\n\n- Compute and store some result, indexing it based on the values of the parameters\n  it was computed for.\n- Compute results that depend on others reliably and easily.\n- Retrieve a previously computed result for a set of parameters.\n- Add new parameters seemlessly.\n- Handle parameter defaults.\n- Save your results at different paths depending on the set of parameters they were\n  computed for, with little to no effort.\n- Track how long each computation takes to identify bottlenecks in your pipeline.\n\n\n## Installation\n\nYou can install the latest release of ReSpace via [pip] from [PyPI]:\n\n```console\n$ pip install respace\n```\n\nOr, if you want the latest development version from GitHub with [git]:\n\n```console\n$ pip install git+https://github.com/TLouf/respace\n```\n\nReSpace requires Python 3.8+ and depends on the [xarray] library.\n\n[git]: https://git-scm.com/\n[pip]: https://pip.pypa.io/\n[pypi]: https://pypi.org/\n[xarray]: https://docs.xarray.dev/en/stable/\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license page],\n_ReSpace_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from a fork of [@cjolowicz]\'s [Hypermodern Python Cookiecutter] template.\n\n<!-- urls -->\n[@cjolowicz]: https://github.com/cjolowicz\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/TLouf/respace/issues\n\n<!-- github-only -->\n[license page]: https://github.com/TLouf/respace/blob/main/LICENSE\n[contributor guide]: https://github.com/TLouf/respace/blob/main/CONTRIBUTING.md\n',
    'author': 'Thomas Louf',
    'author_email': 'tlouf+pro@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/TLouf/respace',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
