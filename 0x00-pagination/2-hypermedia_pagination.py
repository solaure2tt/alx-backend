#!/usr/bin/env python3
"""
   returns a dictionary containing the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
"""
from typing import Tuple
import csv
from math import *
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """start index and an end index corresponding to th
       range of indexes to return in a list
       args:
         page : number of the pqge
         page_size: size of one page
       return:
          (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    res = (start_index, end_index)
    return res


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """find the correct indexes to paginate the dataset
            correctly and return the appropriate page of the dataset
            args:
              page : number of the pqge
              page_size: size of one page
            return:
              List[List]
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        (start, end) = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """returns a dictionary containing key value
        concerning the dataset return
           args:
              page : number of the pqge
              page_size: size of one page
            return:
              dictionnary
        """
        data = self.get_page(page, page_size)
        res = {}
        res['page_size'] = len(data)
        res['data'] = data
        res['page'] = page
        res['total_pages'] = ceil(len(self.dataset()) / page_size)
        if page <= 1:
            res['prev_page'] = None
        else:
            res['prev_page'] = page - 1
        if page >= res['total_pages']:
            res['next_page'] = None
        else:
            res['next_page'] = page + 1
        return res
