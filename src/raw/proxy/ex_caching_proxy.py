# caching proxy stores results of expensive operations and returns the cached result when the same operation is requested again.

class DataFetcher:
    def fetch_data(self, key):
        return f"Data for {key}"

class CachingProxy:
    def __init__(self, fetcher):
        self._fetcher = fetcher
        self._cache = {}

    def fetch_data(self, key):
        if key not in self._cache:
            self._cache[key] = self._fetcher.fetch_data(key)
        return self._cache[key]

# Client code
fetcher = DataFetcher()
proxy = CachingProxy(fetcher)
print(proxy.fetch_data("key1"))  # Data for key1 (fetched)
print(proxy.fetch_data("key1"))  # Data for key1 (cached)
