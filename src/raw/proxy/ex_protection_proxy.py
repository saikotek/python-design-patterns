class SensitiveData:
    """Class representing sensitive data."""

    def __init__(self) -> None:
        self.data = "Sensitive Data"

    def get_data(self) -> str:
        return self.data

class ProtectionProxy:
    """Protection proxy that controls access to the SensitiveData object based on user role."""

    def __init__(self, user_role: str) -> None:
        """Initializes the ProtectionProxy with a user role."""
        self._user_role = user_role
        self._sensitive_data = SensitiveData()

    def get_data(self) -> str:
        """Returns the sensitive data if the user is an admin."""
        if self._user_role == "admin":
            return self._sensitive_data.get_data()
        else:
            return "Access Denied"


# Client code
if __name__ == "__main__":
    admin_proxy = ProtectionProxy("admin")
    user_proxy = ProtectionProxy("user")

    print(admin_proxy.get_data())  # Sensitive Data
    print(user_proxy.get_data())   # Access Denied
