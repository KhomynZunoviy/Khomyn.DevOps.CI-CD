import unittest
from calculator import add, subtract
class TestCalculator(unittest.TestCase):
 def test_add(self):
    self.assertEqual(add(3, 4), 7)
 def test_subtract(self):
    self.assertEqual(subtract(5, 4), 1)
if __name__ == '__main__':
 unittest.main()