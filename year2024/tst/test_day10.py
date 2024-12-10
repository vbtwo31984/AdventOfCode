import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day10 import Day10

class TestDay10(unittest.TestCase):

    def setUp(self):
        self.example_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
        self.day10_instance = Day10(self.example_input)

    def test_part1(self):
        result = self.day10_instance.part1()
        self.assertEqual(result, 36)

    def test_part2(self):
        result = self.day10_instance.part2()
        self.assertEqual(result, 81)

if __name__ == '__main__':
    unittest.main()
