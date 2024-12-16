import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day16 import Day16

class TestDay16(unittest.TestCase):

    def setUp(self):
        self.example_input = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
        self.day16_instance = Day16(self.example_input)

    def test_part1(self):
        result = self.day16_instance.part1()
        self.assertEqual(result, 11048)

    def test_part2(self):
        result = self.day16_instance.part2()
        self.assertEqual(result, 64)

if __name__ == '__main__':
    unittest.main()
