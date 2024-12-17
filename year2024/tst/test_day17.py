import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day17 import Day17

class TestDay17(unittest.TestCase):

    def setUp(self):
        self.example_input = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
        self.day17_instance = Day17(self.example_input)

    def test_part1(self):
        result = self.day17_instance.part1()
        self.assertEqual(result, "4,6,3,5,6,3,5,2,1,0")

if __name__ == '__main__':
    unittest.main()
