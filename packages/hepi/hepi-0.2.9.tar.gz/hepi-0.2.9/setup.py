# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hepi',
 'hepi.data',
 'hepi.plot',
 'hepi.run',
 'hepi.run.madgraph',
 'hepi.run.nllfast',
 'hepi.run.prospino2',
 'hepi.run.resummino',
 'hepi.run.spheno']

package_data = \
{'': ['*'], 'hepi.data': ['json/*']}

install_requires = \
['matplotlib',
 'numpy',
 'pandas>=1.0.0',
 'particle',
 'pqdm',
 'pyslha',
 'scipy>=1.7.0',
 'smpl>=0.0.152',
 'sympy',
 'uncertainties',
 'validators']

extras_require = \
{'lhapdf': ['lhapdf>=6,<7']}

entry_points = \
{'console_scripts': ['hepi-fast = hepi.fast:main']}

setup_kwargs = {
    'name': 'hepi',
    'version': '0.2.9',
    'description': 'Interface to High Energy Physics tools.',
    'long_description': '# HEPi\n\nPython interface for gluing together several HEP programs (e.g. from HEPForge <https://www.hepforge.org/>).\n\n[![PyPI version][pypi image]][pypi link] ![downloads](https://img.shields.io/pypi/dm/hepi.svg) \n\n| [Stable][doc stable]        | [Unstable][doc test]           |\n| ------------- |:-------------:|\n| [![workflow][a s image]][a s link]      | [![test][a t image]][a t link]     |\n| [![Coverage Status][c s i]][c s l] | [![Coverage Status][c t i]][c t l] |\n| [![Codacy Badge][cc s c i]][cc s c l]      |[![Codacy Badge][cc c i]][cc c l] | \n| [![Codacy Badge][cc s q i]][cc s q l]      |[![Codacy Badge][cc q i]][cc q l] | \n| [![Documentation][rtd s i]][rtd s l] | [![Documentation][rtd t i]][rtd t l]  | \n\n## Documentation\n\n-   <https://hepi.readthedocs.io/en/stable/>\n-   <https://apn-pucky.github.io/HEPi/index.html>\n\n## Versions\n\n### Stable\n\n```sh\npip install hepi[opt] [--user] [--upgrade]\n```\n\n### Dev\n\n```sh\npip install --index-url https://test.pypi.org/simple/ hepi[opt]\n```\n\n`[opt]` can be omitted to avoid optional dependencies (ie. lhapdf).\n\n[doc stable]: https://apn-pucky.github.io/HEPi/index.html\n[doc test]: https://apn-pucky.github.io/HEPi/test/index.html\n\n[pypi image]: https://badge.fury.io/py/hepi.svg\n[pypi link]: https://pypi.org/project/hepi/\n\n[a s image]: https://github.com/APN-Pucky/HEPi/actions/workflows/stable.yml/badge.svg\n[a s link]: https://github.com/APN-Pucky/HEPi/actions/workflows/stable.yml\n[a t link]: https://github.com/APN-Pucky/HEPi/actions/workflows/unstable.yml\n[a t image]: https://github.com/APN-Pucky/HEPi/actions/workflows/unstable.yml/badge.svg\n\n[cc s q i]: https://app.codacy.com/project/badge/Grade/ef07b792a0f84f2eb1d7ebe07ae9e639?branch=stable\n[cc s q l]: https://www.codacy.com/gh/APN-Pucky/HEPi/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=APN-Pucky/HEPi&amp;utm_campaign=Badge_Grade?branch=stable\n[cc s c i]: https://app.codacy.com/project/badge/Coverage/ef07b792a0f84f2eb1d7ebe07ae9e639?branch=stable\n[cc s c l]: https://www.codacy.com/gh/APN-Pucky/HEPi/dashboard?utm_source=github.com&utm_medium=referral&utm_content=APN-Pucky/HEPi&utm_campaign=Badge_Coverage?branch=stable\n\n[cc q i]: https://app.codacy.com/project/badge/Grade/ef07b792a0f84f2eb1d7ebe07ae9e639\n[cc q l]: https://www.codacy.com/gh/APN-Pucky/HEPi/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=APN-Pucky/HEPi&amp;utm_campaign=Badge_Grade\n[cc c i]: https://app.codacy.com/project/badge/Coverage/ef07b792a0f84f2eb1d7ebe07ae9e639\n[cc c l]: https://www.codacy.com/gh/APN-Pucky/HEPi/dashboard?utm_source=github.com&utm_medium=referral&utm_content=APN-Pucky/HEPi&utm_campaign=Badge_Coverage\n\n[c s i]: https://coveralls.io/repos/github/APN-Pucky/HEPi/badge.svg?branch=stable\n[c s l]: https://coveralls.io/github/APN-Pucky/HEPi?branch=stable\n[c t l]: https://coveralls.io/github/APN-Pucky/HEPi?branch=master\n[c t i]: https://coveralls.io/repos/github/APN-Pucky/HEPi/badge.svg?branch=master\n\n[rtd s i]: https://readthedocs.org/projects/hepi/badge/?version=stable\n[rtd s l]: https://hepi.readthedocs.io/en/stable/?badge=stable\n[rtd t i]: https://readthedocs.org/projects/hepi/badge/?version=latest\n[rtd t l]: https://hepi.readthedocs.io/en/latest/?badge=latest\n',
    'author': 'Alexander Puck Neuwirth',
    'author_email': 'alexander@neuwirth-informatik.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/APN-Pucky/HEPi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
