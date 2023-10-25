#!/usr/bin/python3
""" Create a class FIFOCache that inherits from
    BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data
           the item value for the key key
           must discard the first item put in cache (FIFO algorithm)
           Args:
             key: key of the value to assign
             item: item to add
           Return:
             nothing
        """
        length = len(self.cache_data)
        if key is not None and item is not None:
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                first_key = list(self.cache_data.keys())[0]
                print("DISCARD: {}".format(first_key))
                self.cache_data.pop(first_key)
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key
           Args:
              key: key of the value to return
           Return:
              value
        """
        if key is not None:
            if key in self.cache_data:
                return self.cache_data[key]
        return None
