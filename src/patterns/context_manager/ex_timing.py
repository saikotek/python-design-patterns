"""
Python Context Manager Example: Timing with contextlib
"""
import time
import contextlib
from typing import Generator

@contextlib.contextmanager
def measure_time(description: str = "Operation") -> Generator[None, None, None]:
    """
    Context manager to measure the execution time of code blocks.
    
    Args:
        description (str): Description of the operation being timed.
        
    Yields:
        None: This context manager doesn't yield any value.
    """
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{description} took {execution_time:.6f} seconds to execute")


def fibonacci_recursive(n: int) -> int:
    """
    Computes the nth Fibonacci number using recursion without memoization.
    This is deliberately inefficient for demonstration purposes.
    
    Args:
        n (int): The position in the Fibonacci sequence to compute.
    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":
    # Using the context manager with fibonacci function
    with measure_time(f"Fibonacci(20)"):
        result = fibonacci_recursive(20)
        print(f"Result: {result}")
    
    with measure_time(f"Fibonacci(25)"):
        result = fibonacci_recursive(25)
        print(f"Result: {result}")
    
    # Nested usage of context manager
    with measure_time("Outer operation"):
        print("Doing some initial work...")
        time.sleep(0.5)
        
        with measure_time("Inner operation"):
            print("Doing some nested work...")
            time.sleep(0.3)
        
        print("Finishing outer work...")
        time.sleep(0.2)