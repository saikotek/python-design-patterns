# Access control, or protection proxy, controls access to the original object.
# This example uses a decorator to restrict access to the sensitive data based on the user's role.

class SensitiveData:
    def get_data(self):
        return "Sensitive Data"

def admin_required(func):
    def wrapper(self, *args, **kwargs):
        if self._user_role == "admin":
            return func(self, *args, **kwargs)
        else:
            return "Access Denied"
    return wrapper

class ProtectionProxy:
    def __init__(self, user_role):
        self._user_role = user_role
        self._sensitive_data = SensitiveData()

    @admin_required
    def get_data(self):
        return self._sensitive_data.get_data()

# Client code
admin_proxy = ProtectionProxy("admin")
user_proxy = ProtectionProxy("user")

print(admin_proxy.get_data())  # Sensitive Data
print(user_proxy.get_data())  # Access Denied
