#!/usr/bin/python3
""" Create a class LFUCache that inherits from
    BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.order = {}
        self.age = 0

    def put(self, key, item):
        """assign to the dictionary self.cache_data
           the item value for the key key
           must discard the least frequency used item
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
                self.cache_data[key] = item
            elif length >= max_it and key not in self.cache_data:
                data_sorted = sorted(self.order.items(), key=lambda x: x[1])
                convert_data_sorted = dict(data_sorted)
                lru_key = list(convert_data_sorted.keys())[0]
                print("DISCARD: {}".format(lru_key))
                self.cache_data.pop(lru_key)
                del self.order[lru_key]
                self.order[key] = 0
                self.cache_data[key] = item
            else:
                self.order[key] = 0
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
