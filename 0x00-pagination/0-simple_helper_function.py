#!/usr/bin/env python3
"""
   return a tuple of size two containing a start
   index and an end index corresponding to the range
   of indexes to return in a list for those particular
   pagination parameters
"""
from typing import Tuple


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
