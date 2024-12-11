import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day11 import Day11

class TestDay11(unittest.TestCase):

    def setUp(self):
        self.example_input = "125 17"
        self.day11_instance = Day11(self.example_input)

    def test_part1(self):
        result = self.day11_instance.part1()
        self.assertEqual(result, 55312)

if __name__ == '__main__':
    unittest.main()
