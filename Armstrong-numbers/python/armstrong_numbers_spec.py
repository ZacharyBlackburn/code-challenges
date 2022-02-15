# The code is written as driver code. Can you convert it to Unit Test?
import unittest 
from armstrong_numbers import find_armstrong_numbers

class ArmstrongTestCase(unittest.TestCase):
  """Tests for armstrong_numbers.py"""

  def test_returns_a_list(self):
    """Tests find_armstrong_numbers to see that it returns a list"""
    self.assertEqual(type(find_armstrong_numbers(list(range(0,9)))), list)

  def test_returns_correct_list(self):
    """Tests find_armstrong_numbers to determine it gives the correct list of numbers""" 
    self.assertEqual(find_armstrong_numbers(list(range(0,999))), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])

if __name__ == "__main__":
    unittest.main() 
