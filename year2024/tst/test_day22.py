import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day22 import Day22

class TestDay22(unittest.TestCase):

    def setUp(self):
        self.example_input = "example input"
        self.day22_instance = Day22(self.example_input)

    def test_part1(self):
        result = self.day22_instance.part1()
        self.assertEqual(result, 0)

    def test_part2(self):
        result = self.day22_instance.part2()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
