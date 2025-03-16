"""
Python Function Decorators Example: Timing Decorator
"""
import functools
import time

def measure_time(func):
    """
    Decorator to measure the execution time of function calls.
    Args:
        func (function): The function to be timed.
    Returns:
        function: The wrapped function with timing functionality.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.6f} seconds to execute with args: {args}")
        return result
    return wrapper

"""
Python Function Decorators Example: Timing Decorator
"""
import functools
import time

def measure_time(func):
    """
    Decorator to measure the execution time of function calls.
    Args:
        func (function): The function to be timed.
    Returns:
        function: The wrapped function with timing functionality.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.6f} seconds to execute with args: {args}")
        return result
    return wrapper

@measure_time
def fibonacci_recursive(n: int) -> int:
    def get_nth_fibonacci(n: int) -> int:
        """
        Computes the nth Fibonacci number using recursion without memoization.
        This is deliberately inefficient to demonstrate the timing decorator.
        
        Args:
            n (int): The position in the Fibonacci sequence to compute.
        Returns:
            int: The nth Fibonacci number.
        """
        if n <= 1:
            return n
        else:
            return get_nth_fibonacci(n - 1) + get_nth_fibonacci(n - 2)
    return get_nth_fibonacci(n)


if __name__ == "__main__":
    """
    Example usage of timed functions with measurable performance differences.
    """
    # Recursive Fibonacci - gets exponentially slower as n increases
    print(f"Result: {fibonacci_recursive(20)}")  # Will be noticeably slow
    print(f"Result: {fibonacci_recursive(25)}")  # Will be significantly slower
    
    # Demonstrating with a function that takes a predictable amount of time
    @measure_time
    def slow_function(n: int) -> None:
        """A deliberately slow function for demonstration purposes."""
        time.sleep(n)
        
    slow_function(1)  # Will take approximately 1 second
