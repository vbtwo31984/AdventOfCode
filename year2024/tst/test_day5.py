import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day5 import Day5

class TestDay5(unittest.TestCase):

    def setUp(self):
        self.example_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
        self.day5_instance = Day5(self.example_input)

    def test_part1(self):
        result = self.day5_instance.part1()
        self.assertEqual(result, 143)

    def test_part2(self):
        result = self.day5_instance.part2()
        self.assertEqual(result, 123)

if __name__ == '__main__':
    unittest.main()
