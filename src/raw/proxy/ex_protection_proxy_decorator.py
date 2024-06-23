from __future__ import annotations

class SensitiveData:
    """Class representing sensitive data."""

    def get_data(self) -> str:
        """Returns the sensitive data."""
        return "Sensitive Data"

class ProtectionProxy:
    """Protection proxy that controls access to the SensitiveData object based on user role."""

    def __init__(self, user_role: str) -> None:
        """Initializes the ProtectionProxy with a user role."""
        self._user_role = user_role
        self._sensitive_data = SensitiveData()

    def admin_required(func):
        """Decorator to restrict access to a method based on the user's role."""

        def wrapper(self: ProtectionProxy, *args, **kwargs):
            """Wrapper function to check user's role before calling the original function."""
            if self._user_role == "admin":
                return func(self, *args, **kwargs)
            else:
                return "Access Denied"
        return wrapper

    @admin_required
    def get_data(self) -> str:
        """Returns the sensitive data if the user is an admin."""
        return self._sensitive_data.get_data()


# Client code
if __name__ == "__main__":
    admin_proxy = ProtectionProxy("admin")
    user_proxy = ProtectionProxy("user")

    print(admin_proxy.get_data())  # Sensitive Data
    print(user_proxy.get_data())   # Access Denied
