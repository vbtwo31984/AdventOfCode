import unittest
import sys
sys.path.insert(0, 'year2024')
from day25 import Day25

class TestDay25(unittest.TestCase):

    def setUp(self):
        self.example_input = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""
        self.day25_instance = Day25(self.example_input)

    def test_part1(self):
        result = self.day25_instance.part1()
        self.assertEqual(result, 3)

    def test_part2(self):
        result = self.day25_instance.part2()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
