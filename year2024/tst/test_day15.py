import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day15 import Day15

class TestDay15(unittest.TestCase):

    def setUp(self):
        self.example_input = "example input"
        self.day15_instance = Day15(self.example_input)

    def test_part1(self):
        result = self.day15_instance.part1()
        self.assertEqual(result, 0)

    def test_part2(self):
        result = self.day15_instance.part2()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
