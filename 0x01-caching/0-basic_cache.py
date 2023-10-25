#!/usr/bin/python3
""" Create a class BasicCache that inherits from BaseCaching
    and is a caching system:
    You must use self.cache_data - dictionary from the parent class BaseCaching
    This caching system doesn’t have limit
    def put(self, key, item):
        Must assign to the dictionary self.cache_data the item
           value for the key key.
        If key or item is None, this method should not do anything.
    def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
         return None
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initiliaze
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """assign to the dictionary self.cache_data
           the item value for the key key
           Args:
             key: key of the value to assign
             item: item to add
           Return:
             nothing
        """
        if key is not None and item is not None:
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
