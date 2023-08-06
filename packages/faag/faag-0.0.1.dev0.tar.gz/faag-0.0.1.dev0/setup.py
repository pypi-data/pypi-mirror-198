# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['faag', 'faag.constants', 'faag.core', 'faag.utils']

package_data = \
{'': ['*'],
 'faag': ['templates/*',
          'templates/base/*',
          'templates/config/*',
          'templates/connection/*',
          'templates/controller/*',
          'templates/dao/*',
          'templates/model/*',
          'templates/schemas/*',
          'templates/schemas/response/*',
          'templates/service/*',
          'templates/utils/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0', 'typer[all]>=0.6.1,<0.8.0']

entry_points = \
{'console_scripts': ['faag = faag_cli.faag:typer_app']}

setup_kwargs = {
    'name': 'faag',
    'version': '0.0.1.dev0',
    'description': 'Flask/FastAPI Architecture Application Generator',
    'long_description': "# Faag-CLI\n\n**FastAPI/Flask project generator with the best folder structure.** (Fast/Flask Architecture App Generator)\nFlask / FastAPI app generator with a maintainable architecture and sample codes for the best practices.\nCurrently, supports generation of FastAPI apps only. Flask support is coming soon. Currently, in `pre-release`. Feel\nfree\nto raise suggestions and issues. This package is made with [Typer](https://typer.tiangolo.com/).\n\n## Installation\n\n```bash\npoetry add faag-cli\n```\n\n```bash\npip install faag-cli\n```\n\n# Usage\n\nCurrently we support generation of apps only. Adding support for other features like adding models, routes, etc. is\ncoming soon.\n\n## To generate a FastAPI/Flask app\n\nFaag generate will automatically generate a FastAPI by default. You can also specify the type of app you want to\ngenerate with the `--type` flag. Default app will be generated with 'sample_app' as the name. You can also specify the\nname of the app with the `--name` flag.\n\n```bash\nUsage: faag generate --help\n\n  FastAPI/Flask project generator with the best folder structure. Generate a new FastAPI/Flask project\n \n╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮\n│ --type                 -t      TEXT  Type of that should be generated. Default type is fast_api. Valid Options are: [fast_api, flask] [default: fast_api        |\n│ --name                 -n      TEXT  Name of the app [default: sampel_app]                                                                                      |\n│ --install-completion                 Install completion for the current shell.                                                                                  |\n│ --show-completion                    Show completion for the current shell, to copy it or customize the installation.                                           |\n│ --help                               Show this message and exit.                                                                                                |\n╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\n```\n\n1. Help\n    ```bash\n    faag --help\n    ```\n\n2. Generate a FastAPI app \n    ```bash\n   faag generate\n    ```\n\n3. Generate a FastAPI/Flask App with custom app name\n    ```bash\n   faag --name myapp\n   faag -n myapp\n    ```\n\n# Setup for development\n\n> ## Virtual environment setup with Poetry\n> 1. Create a fork of the repository\n> 2. Clone the repository to your local machine\n     `git clone git@github.com:<username>/PyNotion.git`\n> 3. Install poetry with `pip install poetry` or `pip3 install poetry`\n> 4. Navigate to the root of the project and run `poetry install`\n\n> ## Setup Pre-commit hooks\n> 1. Install pre-commit hooks `pre-commit install`\n> 2. Migrate pre-commit configs `pre-commit migrate-config`\n> 3. In case of error run `git config --global --unset-all core.hooksPath` or `git config --unset-all core.hooksPath`\n\n## Contribution Guidelines\n\nThank your for taking your valuable time to contribute to Faag-CLI.\nPull requests are welcome. For major changes, please open an issue\nfirst to discuss what you would like to change.\n",
    'author': 'Vetrichelvan',
    'author_email': 'pythonhubdev@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/DevzoneCommunity/faag_cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
