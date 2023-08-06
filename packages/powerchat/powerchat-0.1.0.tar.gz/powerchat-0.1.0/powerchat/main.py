import argparse
import pyperclip
from powerchat.file_utils import FileUtils
from powerchat.openai_utils import OpenAIUtils

import logging


class App:
    @staticmethod
    def main_with_args(
        directory: str,
        copy_code: bool,
        include_pattern: str,
        exclude_pattern: str,
        recursive: bool,
        question: str,
    ):
        output = ""
        if question:
            output += f"Question: {question}\n\n"

        ignore_directories = [
            ".venv",
            "__pycache__",
            "dist",
            ".pytest_cache",
            "build",
            "venv",
            "node_modules",
            ".git",
            ".idea",
            ".vscode",
            "data",
            "logs",
            "output",
            "tmp",
            "cache",
            "docs",
            "docs_build",
        ]

        output += FileUtils.get_all_files_contents(
            directory, include_pattern, exclude_pattern, recursive, ignore_directories
        )

        if question:
            response = OpenAIUtils.send_to_openai_api(output)
            print("OpenAI API response:")
            print(response)
        elif copy_code:
            code_output = FileUtils.get_all_files_contents(
                directory,
                include_pattern,
                exclude_pattern,
                recursive,
                ignore_directories,
            )
            pyperclip.copy(code_output)
            print("The code has been copied to the clipboard.")
        else:
            pyperclip.copy(output)
            print("The output has been copied to the clipboard.")

    @staticmethod
    def main():
        parser = argparse.ArgumentParser(
            description="Print contents of all .py and .md files in a directory."
        )

        parser.add_argument(
            "-c", "--copy_code",
            action="store_true",
            help="copy the code of the directory and its subdirectories to the clipboard",
        )
        parser.add_argument(
            "-i", "--include",
            default="*",
            help='pattern to filter included files (e.g. "*.py" or "*_test.py")',
        )
        parser.add_argument(
            "-e", "--exclude",
            help='pattern to filter excluded files (e.g. "*_test.py")'
        )
        parser.add_argument(
            "-r", "--recursive",
            action="store_true",
            help="search for files recursively in subdirectories",
        )

        parser.add_argument(
            "-d", "--directory",
            nargs="?",
            default=".",
            help="the directory to search for .py and .md files",
        )

        parser.add_argument(
            "-q", "--question",
            help="prompt for a question to answer (e.g. What is the purpose of this code?)",
        )

        args = parser.parse_args()
        App.main_with_args(
            args.directory,
            args.copy_code,
            args.include,
            args.exclude,
            args.recursive,
            args.question,
        )


if __name__ == "__main__":
    try:
        App.main()
    except Exception as e:
        logging.exception(e)
