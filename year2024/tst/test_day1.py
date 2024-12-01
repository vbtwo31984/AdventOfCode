import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day1 import Day1

class TestDay1(unittest.TestCase):

    def setUp(self):
        self.example_input = """3   4
4   3
2   5
1   3
3   9
3   3"""
        self.day1_instance = Day1(self.example_input)

    def test_part1(self):
        result = self.day1_instance.part1()
        self.assertEqual(result, 11)

    def test_part2(self):
        result = self.day1_instance.part2()
        self.assertEqual(result, 31)

if __name__ == '__main__':
    unittest.main()
