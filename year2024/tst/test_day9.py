import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day9 import Day9

class TestDay9(unittest.TestCase):

    def setUp(self):
        self.example_input = "2333133121414131402"
        self.day9_instance = Day9(self.example_input)

    def test_part1(self):
        result = self.day9_instance.part1()
        self.assertEqual(result, 1928)

    def test_part2(self):
        result = self.day9_instance.part2()
        self.assertEqual(result, 2858)

if __name__ == '__main__':
    unittest.main()
