"""
Decorator Design Pattern

Example: Data Access Service with Access Control and Caching Decorators
"""

class Component:
    """Abstract component interface for data service."""

    def get_data(self, user, data_id):
        raise NotImplementedError("Subclasses must implement `get_data`.")

class DataService(Component):
    """Concrete component providing basic data fetching functionality."""

    def get_data(self, user, data_id):
        print(f"Fetching data for ID: {data_id}")
        return {"data": "Here is your data", "id": data_id}

class Decorator(Component):
    """Base decorator class that follows the same interface as Component."""

    def __init__(self, component):
        self._component = component

    def get_data(self, user, data_id):
        return self._component.get_data(user, data_id)

class AccessControlDecorator(Decorator):
    """Decorator that adds access control."""

    def __init__(self, component, role_required):
        super().__init__(component)
        self.role_required = role_required

    def get_data(self, user, data_id):
        if user.get('role') != self.role_required:
            raise Exception(f"Unauthorized: This user does not have the {self.role_required} role.")
        print(f"Access granted for {user['name']}")
        return super().get_data(user, data_id)

class CacheDecorator(Decorator):
    """Decorator that adds caching."""

    def __init__(self, component):
        super().__init__(component)
        self.cache = {}

    def get_data(self, user, data_id):
        key = (user['name'], data_id)
        if key in self.cache:
            print("Returning cached result for", key)
            return self.cache[key]
        result = super().get_data(user, data_id)
        self.cache[key] = result
        return result


if __name__ == "__main__":
    # Combine decorators with the concrete component
    data_service = DataService()
    data_service = AccessControlDecorator(data_service, role_required='admin')
    data_service = CacheDecorator(data_service)

    # Example usage
    admin_user = {'name': 'Alice', 'role': 'admin'}
    try:
        # First fetch
        result = data_service.get_data(admin_user, 101)
        print(result)
        # Second fetch, should retrieve from cache
        result = data_service.get_data(admin_user, 101)
        print(result)
    except Exception as e:
        print(e)

    # Attempt with unauthorized user
    non_admin_user = {'name': 'Bob', 'role': 'user'}
    try:
        result = data_service.get_data(non_admin_user, 101)
        print(result)
    except Exception as e:
        print(e)