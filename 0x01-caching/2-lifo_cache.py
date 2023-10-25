#!/usr/bin/python3
""" Create a class LIFOCache that inherits from
    BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data
           the item value for the key key
           must discard the last item put in cache (LIFO algorithm)
           Args:
             key: key of the value to assign
             item: item to add
           Return:
             nothing
        """
        length = len(self.cache_data)
        max_it = BaseCaching.MAX_ITEMS
        if key is not None and item is not None:
            if key in self.cache_data:
                index = self.order.index(key)
                del self.order[index]
                self.order.append(key)
                self.cache_data[key] = item
            elif length >= max_it and key not in self.cache_data:
                last_key = self.order[-1]
                print("DISCARD: {}".format(last_key))
                self.cache_data.pop(last_key)
                del self.order[-1]
                self.order.append(key)
                self.cache_data[key] = item
            else:
                self.order.append(key)
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
