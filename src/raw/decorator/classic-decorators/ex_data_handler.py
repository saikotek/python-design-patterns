"""
Decorator Design Pattern

Example: Data Handler with Encryption and Compression Decorators
"""

class DataHandler:
    def handle(self, data):
        return f"Handling data: {data}"

class EncryptionDecorator(DataHandler):
    def __init__(self, handler):
        self._handler = handler

    def handle(self, data):
        encrypted_data = f"Encrypted({data})"
        return self._handler.handle(encrypted_data)

class CompressionDecorator(DataHandler):
    def __init__(self, handler):
        self._handler = handler

    def handle(self, data):
        compressed_data = f"Compressed({data})"
        return self._handler.handle(compressed_data)


if __name__ == "__main__":
    # Client code
    handler = DataHandler()
    secure_handler = EncryptionDecorator(CompressionDecorator(handler))
    # Output: Handling data: Encrypted(Compressed(Sensitive Data))
    print(secure_handler.handle("Sensitive Data"))
