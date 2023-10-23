#!/usr/bin/env python3
"""
hypermedia pagination with deletions
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        returns a dictionary with
        the following key-value pairs:
            index: index of the first item in the current page
            next_index: index of the first item in the next page
            page_size: the current page size
            data: actual page of the dataset
        Args:
            index(int): first index
            page_size(int): number records per page
        """
        res = {}
        dataset = self.indexed_dataset()
        size_data = len(dataset)
        assert 0 <= index < size_data
        data = []
        res['index'] = index
        for i in range(page_size):
            while True:
                current_data = dataset.get(index)
                index += 1
                if current_data is not None:
                    break
            data.append(current_data)

        res['data'] = data
        res['page_size'] = len(data)
        if dataset.get(index):
            res['next_index'] = index
        else:
            res['next_index'] = None
        return res
