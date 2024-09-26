"""Caching Proxy Pattern Example: A caching proxy that stores results
of expensive operations and returns the cached result when the same
operation is requested again.
"""


class DataFetcher:
    """Class responsible for fetching data."""

    def fetch_data(self, key: str) -> str:
        """Simulates fetching data for the given key."""
        return f"Data for {key}"

class CachingProxy:
    """Caching proxy that stores results of expensive operations and returns the cached result when the same operation is requested again.

    Attributes:
        _fetcher (DataFetcherProtocol): The data fetcher to delegate data fetching to.
        _cache (dict): Cache storing fetched data.
    """

    def __init__(self, fetcher: DataFetcher) -> None:
        """Initializes the CachingProxy with a data fetcher."""
        self._fetcher = fetcher
        self._cache = {}

    def fetch_data(self, key: str) -> str:
        """Fetches data for the given key, using cache if available."""
        if key not in self._cache:
            self._cache[key] = self._fetcher.fetch_data(key)
        else:
            print(f"Retrieved data for {key} from cache.")
        return self._cache[key]


# Client code
if __name__ == "__main__":
    fetcher = DataFetcher()
    proxy = CachingProxy(fetcher)
    print(proxy.fetch_data("key1"))  # Data for key1 (fetched)
    print(proxy.fetch_data("key2"))  # Data for key1 (fetched)
    print(proxy.fetch_data("key1"))  # Data for key1 (cached)
