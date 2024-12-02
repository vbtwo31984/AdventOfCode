import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day2 import Day2

class TestDay2(unittest.TestCase):

    def setUp(self):
        self.example_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
        self.day2_instance = Day2(self.example_input)

    def test_part1(self):
        result = self.day2_instance.part1()
        self.assertEqual(result, 2)

    def test_part2(self):
        result = self.day2_instance.part2()
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
