import os
import re

def camel_to_kebab(name):
    # Convert CamelCase to kebab-case
    return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()

def rename_folders_recursively(path):
    for dir_path, dirs, files in os.walk(path, topdown=False):
        for dir_name in dirs:
            print(f'Processing: {os.path.join(dir_path, dir_name)}')
            old_path = os.path.join(dir_path, dir_name)
            new_name = camel_to_kebab(dir_name)
            new_path = os.path.join(dir_path, new_name)
            os.rename(old_path, new_path)
            print(f'Renamed: {old_path} to {new_path}')


# Example usage
base_path = '.\\src\\'
rename_folders_recursively(base_path)
