from typing import Protocol, Tuple
import zlib
import hashlib

# Define the Visitor and Elements
class File(Protocol):
    def accept(self, visitor: 'FileVisitor') -> None:
        pass

class TextFile:
    def __init__(self, name: str, content: str, byte_size: int) -> None:
        self.name = name
        self.content = content
        self.byte_size = byte_size

    def accept(self, visitor: 'FileVisitor') -> None:
        visitor.visit_text_file(self)

    # Existing behavior
    def print(self) -> None:
        print(f"TextFile '{self.name}': {self.content}")

class ImageFile:
    def __init__(self, name: str, resolution: Tuple[int, int]) -> None:
        self.name = name
        self.resolution = resolution
        self.data = [[x+y for x in range(resolution[0])] for y in range(resolution[1])]
        
    def accept(self, visitor: 'FileVisitor') -> None:
        visitor.visit_image_file(self)
    
    # Existing behavior
    def print(self) -> None:
        print(f"ImageFile '{self.name}' resolution: {self.resolution}. Data: {self.data}")

class FileVisitor(Protocol):
    def visit_text_file(self, file: TextFile) -> None:
        pass

    def visit_image_file(self, file: ImageFile) -> None:
        pass

# Implement Specific Visitors
class FileSizeVisitor:
    def visit_text_file(self, file: TextFile) -> None:
        print(f"Text file '{file.name}' size: {len(file.content)*file.byte_size} bytes")

    def visit_image_file(self, file: ImageFile) -> None:
        print(f"Image file '{file.name}' size: {file.resolution[0]*file.resolution[1]} pixels")

class MetadataGeneratorVisitor:
    def visit_text_file(self, file: TextFile) -> None:
        content_hash = hashlib.md5(file.content.encode()).hexdigest()
        print(f"Metadata for text file '{file.name}': content length = {len(file.content)}, MD5 hash = {content_hash}")

    def visit_image_file(self, file: ImageFile) -> None:
        resolution = file.resolution
        # flatten the 2D data array
        data = [x for row in file.data for x in row]
        content_hash = hashlib.md5(bytes(data)).hexdigest()
        print(f"Metadata for image file '{file.name}': resolution = {resolution}, MD5 hash = {content_hash}")


# Client Code
def process_files(files: list[File], visitor: FileVisitor) -> None:
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

    print("\nNew Behavior:")
    process_files(files, FileSizeVisitor())

    print("\nMetadata Generator Visitor:")
    process_files(files, MetadataGeneratorVisitor())
