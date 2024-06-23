class Service:
    """Class representing the original service."""

    def operation(self) -> None:
        """Performs the service operation."""
        print("Service operation performed.")

class LoggingProxy:
    """Logging proxy that logs each request made to the original object."""

    def __init__(self, service: Service) -> None:
        """Initializes the LoggingProxy with a service."""
        self._service = service
        self._log = []

    def operation(self) -> None:
        """Logs the operation call and delegates to the original service."""
        self._log.append("Operation called")
        self._service.operation()

    def get_log(self) -> list:
        """Returns the log of operations."""
        return self._log


# Client code
if __name__ == "__main__":
    service = Service()
    proxy = LoggingProxy(service)
    proxy.operation()
    proxy.operation()
    print(proxy.get_log())  # ['Operation called', 'Operation called']
