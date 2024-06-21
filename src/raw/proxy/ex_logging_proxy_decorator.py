# A logging proxy logs each request made to the original object.
# This example utilizes a decorator to log each call to the operation.

class Service:
    def operation(self):
        print("Service operation performed.")

class LoggingProxy:
    def __init__(self, service):
        self._service = service
        self._log = []

    def log(func):
        def wrapper(self, *args, **kwargs):
            self._log.append(f"{func.__name__} called")
            return func(self, *args, **kwargs)
        return wrapper

    @log
    def operation(self):
        self._service.operation()

    def get_log(self):
        return self._log

# Client code
service = Service()
proxy = LoggingProxy(service)
proxy.operation()
proxy.operation()
print(proxy.get_log())  # ['operation called', 'operation called']
