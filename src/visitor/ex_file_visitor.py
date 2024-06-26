"""Visitor Pattern Example: File system visitor that can
perform different operations on files.

We implement two concrete visitors: FileSizeVisitor and MetadataGeneratorVisitor.
FileSizeVisitor calculates the size of text and image files, while MetadataGeneratorVisitor
generates metadata for text and image files.
"""
from __future__ import annotations
from typing import Protocol, Tuple, List
import hashlib


class File(Protocol):
    """Protocol that defines the accept method for file visitors."""

    def accept(self, visitor: FileVisitor) -> None:
        """Accepts a visitor."""
        ...

class TextFile:
    """Concrete implementation of a text file."""

    def __init__(self, name: str, content: str, byte_size: int) -> None:
        """Initializes a TextFile with a name, content, and byte size."""
        self.name = name
        self.content = content
        self.byte_size = byte_size

    def accept(self, visitor: FileVisitor) -> None:
        visitor.visit_text_file(self)

    def print(self) -> None:
        print(f"TextFile '{self.name}': {self.content}")

class ImageFile:
    """Concrete implementation of an image file."""

    def __init__(self, name: str, resolution: Tuple[int, int]) -> None:
        """Initializes an ImageFile with a name and resolution."""
        self.name = name
        self.resolution = resolution
        self.data = [[x + y for x in range(resolution[0])] for y in range(resolution[1])]

    def accept(self, visitor: FileVisitor) -> None:
        visitor.visit_image_file(self)

    def print(self) -> None:
        print(f"ImageFile '{self.name}' resolution: {self.resolution}. Data: {self.data}")

class FileVisitor(Protocol):
    """Protocol that defines visit methods for different file types."""

    def visit_text_file(self, file: TextFile) -> None:
        """Visit method for TextFile."""
        ...

    def visit_image_file(self, file: ImageFile) -> None:
        """Visit method for ImageFile."""
        ...

class FileSizeVisitor:
    """Concrete visitor that calculates the size of files."""

    def visit_text_file(self, file: TextFile) -> None:
        """Calculates and prints the size of a text file."""
        print(f"Text file '{file.name}' size: {len(file.content) * file.byte_size} bytes")

    def visit_image_file(self, file: ImageFile) -> None:
        """Calculates and prints the size of an image file."""
        print(f"Image file '{file.name}' size: {file.resolution[0] * file.resolution[1]} pixels")

class MetadataGeneratorVisitor:
    """Concrete visitor that generates metadata for files."""

    def visit_text_file(self, file: TextFile) -> None:
        """Generates and prints metadata for a text file."""
        content_hash = hashlib.md5(file.content.encode()).hexdigest()
        print(f"Metadata for text file '{file.name}': content length = {
              len(file.content)}, MD5 hash = {content_hash}")

    def visit_image_file(self, file: ImageFile) -> None:
        """Generates and prints metadata for an image file."""
        resolution = file.resolution
        # flatten the 2D data array
        data = [x for row in file.data for x in row]
        content_hash = hashlib.md5(bytes(data)).hexdigest()
        print(f"Metadata for image file '{file.name}': resolution = {
              resolution}, MD5 hash = {content_hash}")


def client_code(files: List[File], visitor: FileVisitor) -> None:
    """Processes a list of files with a given visitor."""
    for file in files:
        file.accept(visitor)


if __name__ == "__main__":
    # Usage
    files = [
        TextFile(name="example.txt", content="Hello world!", byte_size=2),
        ImageFile(name="photo.jpg", resolution=(4, 4))
    ]

    print("Existing Behavior:")
    for file in files:
        file.print()

    print("\nFile Size Visitor:")
    client_code(files, FileSizeVisitor())

    print("\nMetadata Generator Visitor:")
    client_code(files, MetadataGeneratorVisitor())
