# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['_virtualenv_asdf']

package_data = \
{'': ['*']}

install_requires = \
['asdf-inspect>=0.1,<0.2', 'virtualenv']

entry_points = \
{'virtualenv.discovery': ['asdf = _virtualenv_asdf.discovery:ASDF']}

setup_kwargs = {
    'name': 'virtualenv-asdf',
    'version': '0.1.0',
    'description': 'A virtualenv Python discovery plugin using asdf',
    'long_description': '# virtualenv-asdf\n\nA [virtualenv][virtualenv] Python discovery plugin using [asdf][asdf]\n\n## Installation\n\n```shell\npip install virtualenv-asdf\n```\n\n## Usage\n\nThe Python discovery mechanism can be specified by:\n\n* the CLI option `--discovery`:\n  ```shell\n  virtualenv --discovery asdf -p 3.10 testenv\n  ```\n\n* the environment variable `VIRTUALENV_DISCOVERY`:\n  ```shell\n  export VIRTUALENV_DISCOVERY=asdf\n  virtualenv -p 3.10 testenv\n  ```\n\n* the [config][virtualenv-docs-config-file] option `discovery`:\n  ```ini\n  [virtualenv]\n  discovery = asdf\n  ```\n\n  ```shell\n  virtualenv asdf -p 3.10 testenv\n  ```\n\nThe Python version can be expressed using either 2 or 3 version segments:\n\n* `-p 3.9`\n* `-p 3.9.3`\n\nIn the former case, the latest version found will be used.\n\n## Limitations\n\nOnly CPython is supported at the moment.\n\n\nNOTE: this package derived from [virtualenv-pyenv][virtualenv-pyenv] by un.def\n\n[virtualenv]: https://virtualenv.pypa.io/\n[asdf]: https://github.com/asdf-vm/asdf\n[virtualenv-docs-config-file]: https://virtualenv.pypa.io/en/latest/cli_interface.html#configuration-file\n[virtualenv-pyenv]: https://github.com:/un-def/virtualenv-pyenv\n',
    'author': 'Scott Sharkey',
    'author_email': 'ssharkey@lanshark.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lanshark/virtualenv-asdf',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
