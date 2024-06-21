"""
Python Function Decorators

While it is not exactly the same concept as the Decorator pattern from the
GoF book, Python function decorators can be used to modify
the behavior of functions or methods.

Python decorators are functions that accept a function object and return a new
function object that wraps the original function. The new function can perform
some actions before and after calling the original function.
"""

def print_text(text: str) -> None:
    """
    Prints the provided text.

    Args:
        text (str): The text to print.
    """
    print(text)

def bold_decorator(func):
    """
    Decorator that wraps text with HTML bold tags.

    Args:
        func (function): The function to wrap.

    Returns:
        function: The wrapped function.
    """
    def wrapper(text: str) -> None:
        return func(f"<b>{text}</b>")
    return wrapper

def italic_decorator(func):
    """
    Decorator that wraps text with HTML italic tags.

    Args:
        func (function): The function to wrap.

    Returns:
        function: The wrapped function.
    """
    def wrapper(text: str) -> None:
        return func(f"<i>{text}</i>")
    return wrapper

def log_decorator(func):
    """
    Decorator that logs the text before printing.

    Args:
        func (function): The function to wrap.

    Returns:
        function: The wrapped function.
    """
    def wrapper(text: str) -> None:
        print(f"Logging: {text}")
        return func(text)
    return wrapper

@log_decorator
@bold_decorator
@italic_decorator
def print_text(text: str) -> None:
    """
    Prints the provided text with applied decorators.

    Args:
        text (str): The text to print.
    """
    print(text)


if __name__ == "__main__":
    """
    Example usage of the decorated print_text function.
    """
    print_text("Hello, world!")
