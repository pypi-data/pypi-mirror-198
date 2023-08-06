# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['_tox_asdf_redux']

package_data = \
{'': ['*']}

install_requires = \
['asdf-inspect>=0.1,<0.2', 'tox']

entry_points = \
{'tox': ['asdf-redux = _tox_asdf_redux.plugin']}

setup_kwargs = {
    'name': 'tox-asdf-redux',
    'version': '0.1.0',
    'description': 'A tox plugin using asdf to find Python executables',
    'long_description': '# tox-asdf-redux\n\nA [tox][tox] plugin using [asdf][asdf] to find Python executables\n\nTo install a plugin, you install it in the same environment where the tox host is installed.\n\n```bash\n    $ pip install tox-asdf-redux\n```\n\nNOTE: Adapted from [tox-pyenv-redux][tox-pyenv-redux].\n\n[tox]: https://tox.wiki/\n[asdf]: https://github.com/asdf-vm/asdf\n[tox-pyenv-redux]: https://github.com/un-def/tox-pyenv-redux\n',
    'author': 'Scott Sharkey',
    'author_email': 'ssharkey@lanshark.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lanshark/tox-asdf-redux',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
