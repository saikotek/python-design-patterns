"""
Python Function Decorators Example: Logging Decorator
"""
import functools
import logging

# Setting up basic configuration for logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def log_function_call(func):
    """
    Decorator to log function calls and their results.

    Args:
        func (function): The function to be wrapped with logging.

    Returns:
        function: The wrapped function with logging.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        logging.debug(f"{func.__name__} returned {result}")
        return result
    return wrapper


@log_function_call
def add(a: int, b: int, extra: int = 0) -> int:
    """
    Adds two numbers with an optional extra value.

    Args:
        a (int): The first number.
        b (int): The second number.
        extra (int, optional): An optional extra value to add. Defaults to 0.

    Returns:
        int: The sum of a, b, and extra.
    """
    return a + b + extra


if __name__ == "__main__":
    """
    Example usage of the add function with logging.
    """
    add(2, 3, extra=5)
