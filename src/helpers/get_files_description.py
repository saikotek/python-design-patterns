import os
import sys
from pathlib import Path


def get_files_description(base_path: str):
    """
    For all files in the given directory, return a dictionary with the relative filepath as a key and
    as a value return first comment in the file that is marked between triple quotes.
    """

    files_description = {}
    for path in Path(base_path).rglob("*.py"):
        with open(path) as file:
            lines = file.readlines()
            description = ""
            # find the first comment in the file that is marked between triple
            if '"""' not in lines[0]:
                continue
            for i, line in enumerate(lines):
                if i == 0 and line.strip() == '"""':
                    continue
                if i > 0 and '"""' in line:
                    break
                if i > 0 and line == '\n':
                    description += "-"
                description += line.strip().replace('"""', "") + "\n"

            description = description.strip().replace("\n", " ")
            # get path without filename relative to the base path
            dir_path = os.path.relpath(os.path.dirname(path), base_path)
            filename = os.path.basename(path)
            if dir_path not in files_description:
                files_description[dir_path] = []
            files_description[dir_path].append((filename, description))

    return files_description


def convert_to_title_case(snake_str):
    return ' '.join(word.capitalize() for word in snake_str.split('_'))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_files_description.py <path>")
        sys.exit(1)

    path = sys.argv[1]

    if not Path(path).is_dir():
        print("Please provide a valid directory path.")
        sys.exit(1)

    files_description = get_files_description(path)

    for path, files in sorted(files_description.items(), key=lambda x: x[0]):
        print(f"- **{convert_to_title_case(path)}**")
        for (filename, description) in files:
            print(f"  - `{filename}` - {description}")