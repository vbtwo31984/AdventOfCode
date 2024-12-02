import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day7 import Day7

class TestDay7(unittest.TestCase):

    def setUp(self):
        self.example_input = "example input"
        self.day7_instance = Day7(self.example_input)

    def test_part1(self):
        result = self.day7_instance.part1()
        self.assertEqual(result, 0)

    def test_part2(self):
        result = self.day7_instance.part2()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()