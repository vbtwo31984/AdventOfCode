import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day6 import Day6

class TestDay6(unittest.TestCase):

    def setUp(self):
        self.example_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
        self.day6_instance = Day6(self.example_input)

    def test_part1(self):
        result = self.day6_instance.part1()
        self.assertEqual(result, 41)

    def test_part2(self):
        result = self.day6_instance.part2()
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
