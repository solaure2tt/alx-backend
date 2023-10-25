#!/usr/bin/python3
""" Create a class MRUCache that inherits from
    BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.order = {}
        self.age = 0

    def put(self, key, item):
        """assign to the dictionary self.cache_data
           the item value for the key key
           discard the most recently used item
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
                self.order[key] = self.age
                self.age += 1
                self.cache_data[key] = item
            elif length >= max_it and key not in self.cache_data:
                items = self.order.items()
                data_sorted = sorted(items, key=lambda x: x[1], reverse=True)
                convert_data_sorted = dict(data_sorted)
                lru_key = list(convert_data_sorted.keys())[0]
                print("DISCARD: {}".format(lru_key))
                self.cache_data.pop(lru_key)
                del self.order[lru_key]
                self.order[key] = self.age
                self.age += 1
                self.cache_data[key] = item
            else:
                self.order[key] = self.age
                self.age += 1
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
                self.order[key] = self.age
                self.age += 1
                return self.cache_data[key]
        return None
