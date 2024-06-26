"""Virtual Proxy Pattern Example

Also known as Lazy Initialization, a virtual proxy delays the creation/evaluation
of an expensive object/operation until it is actually needed.
"""


class ExpensiveObject:
    """Class representing an expensive object that is costly to create."""

    def __init__(self) -> None:
        print("ExpensiveObject created!")

    def process(self) -> None:
        print("Processing done by ExpensiveObject.")

class VirtualProxy:
    """Virtual proxy that delays the creation of an expensive object until it is actually needed."""

    def __init__(self) -> None:
        self._expensive_object = None

    @property
    def expensive_object(self) -> ExpensiveObject:
        """Lazy-initializes and returns the expensive object."""
        if self._expensive_object is None:
            self._expensive_object = ExpensiveObject()
        return self._expensive_object

    def process(self) -> None:
        """Delegates the processing task to the expensive object."""
        self.expensive_object.process()


# Client code
if __name__ == "__main__":
    proxy = VirtualProxy()
    proxy.process()  # ExpensiveObject is created and processed
    proxy.process()  # ExpensiveObject is reused and processed
