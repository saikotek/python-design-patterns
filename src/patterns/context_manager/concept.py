"""
Python Context Managers
While similar in concept to decorators, context managers in Python provide a way to
allocate and release resources precisely when you want to. The most familiar example
is opening and closing files, but context managers can be used for much more.

Context managers implement a protocol that consists of __enter__ and __exit__ methods.
When a context is entered using the 'with' statement, the __enter__ method is called.
When the block inside the 'with' statement is exited, the __exit__ method is called,
regardless of whether an exception was raised or not.

This ensures proper resource cleanup even in the face of exceptions, making context
managers perfect for managing database connections, file handles, locks, and other
resources that need explicit setup and teardown.
"""

class MyContextManager:
    """Context manager class."""
    def __init__(self, name):
        self.name = name
        
    def __enter__(self):
        print(f"Entering the context: {self.name}")
        # The value returned here is assigned to the variable after 'as'
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting the context: {self.name}")
        # If this method returns True, exceptions in the block are suppressed
        # Return False or None to let exceptions propagate
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
        return False  # Let exceptions propagate
    
    def do_something(self):
        print(f"Doing something in {self.name}")

if __name__ == "__main__":
    # Basic usage of a context manager
    with MyContextManager("Example") as context:
        context.do_something()
        print("Inside the with block")
    
    print("\nDemonstrating exception handling:")
    try:
        with MyContextManager("Exception Demo"):
            print("About to raise an exception...")
            raise ValueError("Deliberate error")
            print("This line won't execute")
    except ValueError:
        print("Exception was caught outside the context manager")