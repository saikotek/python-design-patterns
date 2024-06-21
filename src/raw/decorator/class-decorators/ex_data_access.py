"""
Python Class Decorators

Example: Data Access Control with Class Decorators
In similar manner to Decorator pattern, Python decorators can 
wrap either original behaviour or wrap another decorator
allowing multiple decorators to be applied to a function.

In this example, we have a decorator that checks if a user has
the required role to access a function and another decorator that
caches the result of the function to avoid recomputation.
"""

class Decorator:
    """Decorator class."""

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

class AccessControl(Decorator):
    """Access control decorator."""

    def __init__(self, func, role_required):
        super().__init__(func)
        self.role_required = role_required

    def __call__(self, user, *args, **kwargs):
        if user.get('role') != self.role_required:
            raise Exception(f"Unauthorized: This user does not have the {self.role_required} role.")
        print(f"Access granted for {user['name']}")
        return self.func(user, *args, **kwargs)

class Cache(Decorator):
    """Caching decorator."""

    def __init__(self, func):
        super().__init__(func)
        self.cache = {}

    def __call__(self, *args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in self.cache:
            print("Caching new result")
            self.cache[key] = self.func(*args, **kwargs)
        else:
            print("Returning cached result")
        return self.cache[key]

# Function to be decorated
def get_data(user, data_id):
    print(f"Retrieving data for ID: {data_id}")
    return {"data": "secret data", "id": data_id}


if __name__ == "__main__":
    # Wrap the function with decorators
    decorated_get_data = Cache(AccessControl(get_data, 'admin'))

    # Example Usage
    admin_user = {'name': 'Alice', 'role': 'admin'}
    non_admin_user = {'name': 'Bob', 'role': 'user'}

    try:
        print(decorated_get_data(admin_user, 101))
        print(decorated_get_data(admin_user, 101))  # This call should be cached
    except Exception as e:
        print(e)

    try:
        print(decorated_get_data(non_admin_user, 101))
    except Exception as e:
        print(e)
