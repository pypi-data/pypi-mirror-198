# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['powerchat']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.27.2,<0.28.0', 'pyperclip>=1.8.2,<2.0.0']

entry_points = \
{'console_scripts': ['powerchat = powerchat.main:App.main']}

setup_kwargs = {
    'name': 'powerchat',
    'version': '0.1.0',
    'description': '',
    'long_description': '## Powerchat\nPowerchat is a Python command-line tool that allows you to list and view the contents of all `.py` and `.md` files in a directory and its subdirectories. It also provides other useful features, such as generating pull request descriptions and suggesting updates to a README.md file based on Git diff or full file contents.\n\n## Installation\nTo install Powerchat, clone the repository and install the dependencies using Poetry:\n\n```bash\ngit clone https://github.com/yourusername/powerchat.git\ncd powerchat\npoetry install\n```\n\nThis will install all the required dependencies and create a virtual environment for Powerchat.\n\nTo activate the virtual environment, run:\n```\npoetry shell\n```\n\nNow you can run Powerchat from the command line with the `python src/main.py` command.\n\n## Usage\n\nPowerchat can be run from the command line with the `python src/main.py` command. Powerchat accepts several command-line arguments:\n\ndirectory: The directory to search for .py and .md files. Required.\n--refactor: Prompt for refactoring suggestions.\n--documentation: Suggest README.md updates based on Git diff or full contents.\n--features: Prompt for new feature suggestions.\n--pull_request: Prompt for a pull request description based on the changed code.\n--copy_code: Copy the code of the directory and its subdirectories to the clipboard.\n--include: Pattern to filter included files (e.g. *.py or *_test.py).\n--exclude: Pattern to filter excluded files (e.g. *_test.py).\n--recursive: Search for files recursively in subdirectories.\n\nFor more information on how to use Powerchat, run `python main.py --help`.\n\n## License\n\nPowerchat is released under the MIT License. See LICENSE for more information.\n',
    'author': 'Björn van Dijkman',
    'author_email': 'bjornvandijkman@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
