# A logging proxy logs each request made to the original object.

class Service:
    def operation(self):
        print("Service operation performed.")

class LoggingProxy:
    def __init__(self, service):
        self._service = service
        self._log = []

    def operation(self):
        self._log.append("Operation called")
        self._service.operation()

    def get_log(self):
        return self._log

# Client code
service = Service()
proxy = LoggingProxy(service)
proxy.operation()
proxy.operation()
print(proxy.get_log())  # ['Operation called', 'Operation called']
