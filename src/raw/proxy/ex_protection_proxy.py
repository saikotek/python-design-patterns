# Access control, or protection proxy, controls access to the original object.

class SensitiveData:
    def __init__(self):
        self.data = "Sensitive Data"

    def get_data(self):
        return self.data

class ProtectionProxy:
    def __init__(self, user_role):
        self._user_role = user_role
        self._sensitive_data = SensitiveData()

    def get_data(self):
        if self._user_role == "admin":
            return self._sensitive_data.get_data()
        else:
            return "Access Denied"

# Client code
admin_proxy = ProtectionProxy("admin")
user_proxy = ProtectionProxy("user")

print(admin_proxy.get_data())  # Sensitive Data
print(user_proxy.get_data())  # Access Denied
