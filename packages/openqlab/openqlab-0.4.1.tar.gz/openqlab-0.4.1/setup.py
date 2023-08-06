# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['openqlab',
 'openqlab.analysis',
 'openqlab.conversion',
 'openqlab.io',
 'openqlab.io.importers',
 'openqlab.io.importers._old_importers',
 'openqlab.plots']

package_data = \
{'': ['*']}

install_requires = \
['importlib-metadata>=4.0,<5.0',
 'matplotlib>=3.2.1,<4.0.0',
 'numpy>=1.18,<2.0',
 'pandas>=1.3,<2.0',
 'pyserial>=3.5,<4.0',
 'scipy>=1.5,<2.0',
 'tabulate>=0.8.9,<0.9.0',
 'typeguard>=2.9.1,<3.0.0',
 'wcwidth>=0.2.5,<0.3.0']

extras_require = \
{'hdf': ['tables>=3.6.1,<4.0.0'],
 'visa': ['pyvisa-py>=0.5.1,<0.6.0', 'PyVISA>=1.11.1,<2.0.0']}

setup_kwargs = {
    'name': 'openqlab',
    'version': '0.4.1',
    'description': 'An open-source collection of tools for quantum-optics experiments',
    'long_description': '# openqlab\n\n[![pipeline status](https://gitlab.com/las-nq/openqlab/badges/master/pipeline.svg)](https://gitlab.com/las-nq/openqlab/commits/master)\n[![coverage report](https://gitlab.com/las-nq/openqlab/badges/master/coverage.svg)](https://gitlab.com/las-nq/openqlab/commits/master)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n\n`openqlab` provides a collection of useful tools and helpers for the\nanalysis of lab data in the Nonlinear Quantum Optics Group at the University\nof Hamburg.\n\nPart of the content in this package was written during the PhD theses of\nSebastian Steinlechner and Tobias Gehring. It is currently maintained by\nSebastian Steinlechner, Christian Darsow-Fromm, Jan Petermann and is looking for more\nvolunteers who would like to contribute.\n\nRead the latest changes in our [changelog](CHANGELOG.md).\n\n## Documentation\n\n* Current documentation of the [latest release](https://las-nq-serv.physnet.uni-hamburg.de/python/openqlab)\n* Current documentation of the [latest development version](https://las-nq-serv.physnet.uni-hamburg.de/python/openqlab-stage)\n\n## Features\n\n* Importers for various file formats:\n  * Agilent/Keysight scopes (binary and CSV)\n  * Rohde & Schwarz spectrum analyzers\n  * Tektronix spectrum analyzer\n  * plain ascii\n  * and a few more...\n* easily create standard plots from measurement data\n* design control loops\n* analyze beam profiler data\n* generate covariance matrices for N partite systems\n* several postprocessing functions for entanglement data\n* analyse and automatically plot squeezing data\n* tools for working with dB units\n\n## Installation\n\nFor a detailed installation instruction see the main [documentation](https://las-nq-serv.physnet.uni-hamburg.de/python/openqlab/).\n\n## Usage\n\nYou will need an up-to-date Python 3 environment to use this package, e.g.\nthe Anaconda Python distribution will work just fine. Please refer to the\n`requirements.txt` for a list of prerequisites (although these should be\ninstalled automatically, if necessary).\n\nFor examples and details on how to use this package, please refer to the\ndocumentation.\n\n## Contributing\nAll contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.\n\nA detailed overview on how to contribute can be found in the [contributing guide](CONTRIBUTING.md).\n\n## License\nThe code is licensed under the [GNU GENERAL PUBLIC LICENSE](https://www.gnu.org/licenses/gpl-3.0.html). See [LICENSE](LICENSE).\n\n## Changelog\nChanges to the code are documented in the [changelog](CHANGELOG.md).\n',
    'author': 'Jan Petermann',
    'author_email': 'jpeterma@physnet.uni-hamburg.de',
    'maintainer': 'Christian Darsow-Fromm',
    'maintainer_email': 'cdarsowf@physnet.uni-hamburg.de',
    'url': 'https://gitlab.com/las-nq/openqlab',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
