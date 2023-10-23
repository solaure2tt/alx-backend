#!/usr/bin/env python3
"""
   return a tuple of size two containing a start
   index and an end index corresponding to the range
   of indexes to return in a list for those particular
   pagination parameters
"""
from typing import Tuple
import csv
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
