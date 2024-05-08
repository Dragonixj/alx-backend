#!/usr/bin/env python3
"""Task 0: Basic dictionary"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Basic caching system"""

    def put(self, key, item):
        """Add new item to the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from cache"""
        if key is None:
            return None

        return self.cache_data.get(key, None)
