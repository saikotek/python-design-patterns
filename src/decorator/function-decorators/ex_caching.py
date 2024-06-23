"""
Python Function Decorators

Example: Caching Decorator
"""
import functools


def memoize(func):
    """
    Decorator to cache the results of function calls to optimize performance.

    Args:
        func (function): The function to be memoized.

    Returns:
        function: The wrapped function with caching.
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print("Returning cached result for", args)
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@memoize
def fibonacci(n: int) -> int:
    """
    Computes the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence to compute.

    Returns:
        int: The nth Fibonacci number.
    """
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    """
    Example usage of the memoized fibonacci function.
    """
    print(fibonacci(10))  # First call, calculates and caches the results
    print(fibonacci(10))  # Subsequent call, returns the cached result
