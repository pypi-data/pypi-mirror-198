import os
import fnmatch
import re
from typing import List


class FileUtils:
    @staticmethod
    def list_directory_files(
        directory: str,
        include_pattern: str = "*",
        exclude_pattern: str = None,
        recursive: bool = False,
        ignore_directories: List[str] = None,
    ) -> List[str]:
        if ignore_directories is None:
            ignore_directories = []

        file_list = []

        for root, dirnames, filenames in os.walk(directory):
            # Ignore specified directories
            dirnames[:] = [d for d in dirnames if d not in ignore_directories]

            for filename in filenames:
                if not filename.endswith((".py", ".md", ".yml", ".yaml")):
                    continue

                if not fnmatch.fnmatch(filename, include_pattern):
                    continue

                if exclude_pattern and fnmatch.fnmatch(filename, exclude_pattern):
                    continue

                file_list.append(os.path.join(root, filename))

            if not recursive:
                break

        return file_list

    @staticmethod
    def read_file_contents(filepath: str) -> str:
        with open(filepath) as file:
            return file.read()

    @staticmethod
    def contains_sensitive_information(content: str) -> bool:
        sensitive_patterns = [
            r'password\s*=\s*[\'"].+[\'"]',
            r'apikey\s*=\s*[\'"].+[\'"]',
            r'secret\s*=\s*[\'"].+[\'"]',
        ]

        for pattern in sensitive_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return True

        return False

    @staticmethod
    def get_all_files_contents(
        directory: str,
        include_pattern: str,
        exclude_pattern: str,
        recursive: bool,
        ignore_directories: List[str],
    ) -> str:

        file_list = FileUtils.list_directory_files(
            directory, include_pattern, exclude_pattern, recursive, ignore_directories
        )

        output = ""

        if len(file_list) == 0:
            return "No files found."

        tree_structure = FileUtils.build_tree_structure(file_list, directory)
        output += tree_structure
        output += "\n"

        for i, filename in enumerate(file_list):
            content = FileUtils.read_file_contents(filename)

            if FileUtils.contains_sensitive_information(content):
                output += f"=== {os.path.relpath(filename)} ===\n"
                output += "This file contains sensitive information and has been excluded from the output.\n"
            else:
                output += f"=== {os.path.relpath(filename)} ===\n"
                output += content

            if i < len(file_list) - 1:
                output += "---\n"

        return output

    @staticmethod
    def build_tree_structure(file_list: list, root_directory: str) -> str:
        tree_structure = ""
        root_directory = os.path.abspath(root_directory)
        file_paths = [os.path.relpath(file, root_directory) for file in file_list]

        path_parts = [path.split(os.path.sep) for path in file_paths]
        tree_dict = {}

        for parts in path_parts:
            current_level = tree_dict
            for part in parts:
                if part not in current_level:
                    current_level[part] = {}
                current_level = current_level[part]

        def generate_tree_level(tree, level):
            nonlocal tree_structure
            for name, subtree in tree.items():
                tree_structure += "  " * level + "|-- " + name + "\n"
                if subtree:
                    generate_tree_level(subtree, level + 1)

        generate_tree_level(tree_dict, 0)
        return tree_structure
