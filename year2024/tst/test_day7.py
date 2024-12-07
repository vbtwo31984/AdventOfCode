import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day7 import Day7

class TestDay7(unittest.TestCase):

    def setUp(self):
        self.example_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
        self.day7_instance = Day7(self.example_input)

    def test_part1(self):
        result = self.day7_instance.part1()
        self.assertEqual(result, 3749)

    def test_part2(self):
        result = self.day7_instance.part2()
        self.assertEqual(result, 11387)

if __name__ == '__main__':
    unittest.main()
