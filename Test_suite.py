import unittest
#checking
from Function_to_test import add_numbers

class TestFunction(unittest.TestCase):

    def test_addition(self):
        result = add_numbers(3)
        self.assertEqual(result,6)

    def test_addition_neg_number(self):
        result = add_numbers(-3)
        self.assertEqual(result,0)

if __name__ == '__main__':
    unittest.main()
