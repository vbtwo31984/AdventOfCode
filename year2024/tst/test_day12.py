import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day12 import Day12

class TestDay12(unittest.TestCase):

    def setUp(self):
        self.example_input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
        self.day12_instance = Day12(self.example_input)

    def test_part1(self):
        result = self.day12_instance.part1()
        self.assertEqual(result, 1930)

    def test_part2(self):
        result = self.day12_instance.part2()
        self.assertEqual(result, 1206)

if __name__ == '__main__':
    unittest.main()
