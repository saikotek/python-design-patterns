"""
Python Function Decorators

Example: Access Control Decorator
"""

import functools

def access_control(required_role: str):
    """
    Decorator to enforce access control based on user roles.

    Args:
        required_role (str): The role required to access the decorated function.

    Returns:
        function: The wrapped function with access control.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get('role') != required_role:
                raise Exception(f"Unauthorized: This user does not have the {required_role} role.")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@access_control(required_role='admin')
def delete_user(user: dict) -> None:
    """
    Deletes a user if the user has the required role.

    Args:
        user (dict): The user to be deleted.
    """
    print(f"User {user['name']} deleted")


if __name__ == "__main__":
    """
    Example usage of the delete_user function with access control.
    """
    admin_user = {'name': 'Alice', 'role': 'admin'}
    regular_user = {'name': 'Bob', 'role': 'user'}

    try:
        delete_user(admin_user)  # This should work
    except Exception as e:
        print(e)

    try:
        delete_user(regular_user)  # This should raise an exception
    except Exception as e:
        print(e)
