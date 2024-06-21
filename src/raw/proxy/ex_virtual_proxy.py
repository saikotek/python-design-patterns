# Lazy initialization, also known as virtual proxy, 
# delays the creation of an expensive object until it is actually needed.

class ExpensiveObject:
    def __init__(self):
        print("ExpensiveObject created!")

    def process(self):
        print("Processing done by ExpensiveObject.")

class VirtualProxy:
    def __init__(self):
        self._expensive_object = None

    @property
    def expensive_object(self):
        if self._expensive_object is None:
            self._expensive_object = ExpensiveObject()
        return self._expensive_object

    def process(self):
        self.expensive_object.process()

# Client code
proxy = VirtualProxy()
proxy.process()  # ExpensiveObject is created and processed
proxy.process()  # ExpensiveObject is reused and processed
