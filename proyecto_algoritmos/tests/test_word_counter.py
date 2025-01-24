import unittest
from services.word_counter import count_words

class TestWordCounter(unittest.TestCase):
    
    def test_empty_list(self):
        words = []
        result = count_words(words)
        self.assertEqual(result, {})
    
    def test_basic_count(self):
        words = ["Hola", "hola", "Mundo"]
        result = count_words(words)
        self.assertEqual(result["hola"], 2)  # 'Hola' y 'hola' => 'hola': 2
        self.assertEqual(result["mundo"], 1)
    
    def test_mixed_case(self):
        words = ["Python", "python", "PYTHON", "PyThOn"]
        result = count_words(words)
        self.assertEqual(result["python"], 4)

if __name__ == '__main__':
    unittest.main()
