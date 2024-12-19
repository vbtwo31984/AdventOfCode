import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day19 import Day19

class TestDay19(unittest.TestCase):

    def setUp(self):
        self.example_input = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""
        self.day19_instance = Day19(self.example_input)

    def test_part1(self):
        result = self.day19_instance.part1()
        self.assertEqual(result, 6)

    def test_part2(self):
        result = self.day19_instance.part2()
        self.assertEqual(result, 16)

if __name__ == '__main__':
    unittest.main()
