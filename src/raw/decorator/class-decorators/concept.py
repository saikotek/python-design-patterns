"""
Python Class Decorators

While it is not exactly the same concept as the Decorator pattern from the
GoF book, Python decorators can be used to modify
the behavior of functions or methods.

In this example, a decorator is a class that is callable (meaning it can be
used as a function). It accepts a function object and returns a new function
object that wraps the original function. The new function can perform some
actions before and after calling the original function.
"""

class MyDecorator:
    """Decorator class."""

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before calling the function")
        result = self.func(*args, **kwargs)  # Call the original function
        print("After calling the function")
        return result

@MyDecorator
def say_hello(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    say_hello("Alice")
