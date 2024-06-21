# A smart reference proxy manages the lifecycle of an object, ensuring it is created and destroyed as needed.

class HeavyObject:
    def __init__(self):
        print("HeavyObject created!")

    def perform_task(self):
        print("Task performed by HeavyObject.")

    def dispose(self):
        print("HeavyObject disposed!")

class SmartReferenceProxy:
    def __init__(self):
        self._heavy_object = None
        self._references = 0

    def acquire(self):
        if self._references == 0:
            self._heavy_object = HeavyObject()
        self._references += 1
        return self._heavy_object

    def release(self):
        if self._references > 0:
            self._references -= 1
            if self._references == 0:
                self._heavy_object.dispose()
                self._heavy_object = None

# Client code
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
