# tests/test_searching.py

import unittest
from services.searching import linear_search, binary_search

class TestSearching(unittest.TestCase):
    
    def setUp(self):
        self.data_ordenada = [1, 2, 3, 5, 7, 10]
        self.data_no_ordenada = [10, 7, 5, 3, 2, 1]
    
    def test_linear_search_encontrar(self):
        index = linear_search(self.data_no_ordenada, 3)
        self.assertEqual(index, 3)  # Esperamos encontrar '3' en posición 3
    
    def test_linear_search_no_encontrar(self):
        index = linear_search(self.data_no_ordenada, 100)
        self.assertEqual(index, -1)
    
    def test_binary_search_encontrar(self):
        index = binary_search(self.data_ordenada, 7)
        self.assertEqual(index, 4)  # '7' está en índice 4
    
    def test_binary_search_no_encontrar(self):
        index = binary_search(self.data_ordenada, 999)
        self.assertEqual(index, -1)

if __name__ == "__main__":
    unittest.main()
