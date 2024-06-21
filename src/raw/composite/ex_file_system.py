"""
Composite Design Pattern

Example: Working with files and directories through a composite structure.
"""
from typing import Protocol, List
import os


class FileSystemEntry(Protocol):
    """
    Protocol defining the interface for file system entries.
    """

    def get_size(self) -> int:
        """
        Gets the size of the file system entry.
        """
        ...

class File(FileSystemEntry):
    """
    Leaf component representing a file.

    Attributes:
        path (str): The path of the file.
    """

    def __init__(self, path: str):
        """
        Initializes a new File instance.
        """
        self.path = path

    def get_size(self) -> int:
        """
        Gets the size of the file.
        """
        return os.path.getsize(self.path)


class Directory(FileSystemEntry):
    """
    Composite component representing a directory.

    Attributes:
        path (str): The path of the directory.
        children (List[FileSystemEntry]): The child entries of the directory.
    """

    def __init__(self, path: str):
        """
        Initializes a new Directory instance and populates its children.
        """
        self.path = path
        self.children: List[FileSystemEntry] = []
        self._populate_children()

    def _populate_children(self) -> None:
        """
        Populates the directory with its contents.
        """
        for entry in os.listdir(self.path):
            full_path = os.path.join(self.path, entry)
            if os.path.isdir(full_path):
                print(f"Adding directory: {full_path}")
                self.children.append(Directory(full_path))
            else:
                print(f"Adding file: {full_path}")
                self.children.append(File(full_path))

    def get_size(self) -> int:
        """
        Gets the total size of the directory, including its contents.
        """
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size


def client_code(entry: FileSystemEntry) -> None:
    """
    Client code that uses the file system entry.

    Args:
        entry (FileSystemEntry): The file system entry to process.
    """
    print(f"Total size of '{entry.path}' is {entry.get_size()} bytes")


if __name__ == "__main__":
    """
    Example usage of the composite pattern with file system entries.
    """
    # get one directory above the current directory
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = Directory(cur_dir[:cur_dir.rfind(os.sep)])
    client_code(root_dir)
