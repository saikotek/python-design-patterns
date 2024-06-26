"""
Smart Reference Proxy Example
"""


class HeavyObject:
    """Class representing a heavy object that is expensive to create and destroy."""

    def __init__(self) -> None:
        print("HeavyObject created!")

    def perform_task(self) -> None:
        print("Task performed by HeavyObject.")

    def dispose(self) -> None:
        print("HeavyObject disposed!")

class SmartReferenceProxy:
    """Smart reference proxy that manages the lifecycle of a HeavyObject."""

    def __init__(self) -> None:
        self._heavy_object = None
        self._references = 0

    def acquire(self) -> HeavyObject:
        """Acquires a reference to the heavy object, creating it if necessary."""
        if self._references == 0:
            self._heavy_object = HeavyObject()
        self._references += 1
        return self._heavy_object

    def release(self) -> None:
        """Releases a reference to the heavy object, disposing of it if no references remain."""
        if self._references > 0:
            self._references -= 1
            if self._references == 0:
                self._heavy_object.dispose()
                self._heavy_object = None


# Client code
if __name__ == "__main__":
    proxy = SmartReferenceProxy()

    # Acquire the heavy object
    obj1 = proxy.acquire()
    obj1.perform_task()  # HeavyObject created! Task performed by HeavyObject.

    # Release the heavy object
    proxy.release()  # HeavyObject disposed!

    # Re-acquire the heavy object
    obj2 = proxy.acquire()
    obj2.perform_task()  # HeavyObject created! Task performed by HeavyObject.

    # Release the heavy object
    proxy.release()  # HeavyObject disposed!
