#!/usr/bin/python3
"""basicaching"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""

    def put(self, key, item):
        """item value for key key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """value of the key in self.cache_data"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
