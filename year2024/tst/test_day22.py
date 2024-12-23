import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day22 import Day22

class TestDay22(unittest.TestCase):

    def setUp(self):
        self.example_input = """1
2
3
2024"""
        self.day22_instance = Day22(self.example_input)

    def test_mix(self):
        secret = 42
        num = 15
        result = self.day22_instance.mix(secret, num)
        self.assertEqual(result, 37)

    def test_prune(self):
        secret = 100000000
        result = self.day22_instance.prune(secret)
        self.assertEqual(result, 16113920)

    def test_part1(self):
        result = self.day22_instance.part1()
        self.assertEqual(result, 37990510)

    def test_part2(self):
        result = self.day22_instance.part2()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
