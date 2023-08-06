## Powerchat
Powerchat is a Python command-line tool that allows you to list and view the contents of all `.py` and `.md` files in a directory and its subdirectories. It also provides other useful features, such as generating pull request descriptions and suggesting updates to a README.md file based on Git diff or full file contents.

## Installation
To install Powerchat, clone the repository and install the dependencies using Poetry:

```bash
git clone https://github.com/yourusername/powerchat.git
cd powerchat
poetry install
```

This will install all the required dependencies and create a virtual environment for Powerchat.

To activate the virtual environment, run:
```
poetry shell
```

Now you can run Powerchat from the command line with the `python src/main.py` command.

## Usage

Powerchat can be run from the command line with the `python src/main.py` command. Powerchat accepts several command-line arguments:

directory: The directory to search for .py and .md files. Required.
--refactor: Prompt for refactoring suggestions.
--documentation: Suggest README.md updates based on Git diff or full contents.
--features: Prompt for new feature suggestions.
--pull_request: Prompt for a pull request description based on the changed code.
--copy_code: Copy the code of the directory and its subdirectories to the clipboard.
--include: Pattern to filter included files (e.g. *.py or *_test.py).
--exclude: Pattern to filter excluded files (e.g. *_test.py).
--recursive: Search for files recursively in subdirectories.

For more information on how to use Powerchat, run `python main.py --help`.

## License

Powerchat is released under the MIT License. See LICENSE for more information.
