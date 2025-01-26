# tests/test_sorting.py

import unittest
from services.sorting import bubble_sort, insertion_sort, merge_sort

class TestSorting(unittest.TestCase):
    
    def test_bubble_sort(self):
        data = [34, 2, 78, 1, 56, 9]
        bubble_sort(data)
        self.assertEqual(data, sorted([34, 2, 78, 1, 56, 9]))
    
    def test_insertion_sort(self):
        data = [34, 2, 78, 1, 56, 9]
        insertion_sort(data)
        self.assertEqual(data, sorted([34, 2, 78, 1, 56, 9]))
    
    def test_merge_sort(self):
        data = [34, 2, 78, 1, 56, 9]
        merge_sort(data)
        self.assertEqual(data, sorted([34, 2, 78, 1, 56, 9]))

if __name__ == "__main__":
    unittest.main()
