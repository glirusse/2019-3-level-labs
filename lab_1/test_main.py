import unittest

from main import sum_of_list

class TestSum(unittest.TestCase):

    def test_list_of_integers(self):
        integers = [1, 2, 3, 4]
        result = sum_of_list(integers)
        self.assertEqual(result, 10)
    
    def test_list_of_floats(self):
        floats = [0.1, 0.2, 0.6]
        result = sum_of_list(floats)
        self.assertEqual(result, 0.9)
        
if __name__ == '__main__':
	unittest.main()