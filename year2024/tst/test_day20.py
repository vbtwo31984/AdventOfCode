import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day20 import Day20

class TestDay20(unittest.TestCase):

    def setUp(self):
        self.example_input = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
        self.day20_instance = Day20(self.example_input)

    def test_part1(self):
        result = self.day20_instance.part1(40)
        self.assertEqual(result, 2)

    def test_part2(self):
        result = self.day20_instance.part2(50)
        self.assertEqual(result, 32+31+29+39+25+23+20+19+12+14+12+22+4+3)

if __name__ == '__main__':
    unittest.main()
