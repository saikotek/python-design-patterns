"""Singleton Design Pattern

Example: Configuration class that stores application settings as a singleton.
"""
from __future__ import annotations


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class ConfigurationManager(metaclass=SingletonMeta):
    def __init__(self):
        if not hasattr(self, 'config'):
            self.config = self._load_config()

    def _load_config(self):
        # Simulate loading a configuration file or settings
        return {
            'database_host': 'localhost',
            'database_port': 5432,
            'api_key': 'ABC123XYZ',
            'debug_mode': True,
        }

    def __getitem__(self, key):
        return self.config.get(key)

    def __setitem__(self, key, value):
        self.config[key] = value


# Usage example
if __name__ == "__main__":
    config1 = ConfigurationManager()
    print(f"config1 instance's database_host: {config1['database_host']}")  # Output: localhost

    config2 = ConfigurationManager()
    print(f"config2 instance's database_host: {config2['database_host']}")  # Output: localhost
    print("Changing config2's database_host to 'remotehost'...")
    config2['database_host'] = 'remotehost'

    print(f"config1 instance's database_host: {config1['database_host']}")  # Output: remotehost
    print(f"config2 instance's database_host: {config2['database_host']}")  # Output: localhost
