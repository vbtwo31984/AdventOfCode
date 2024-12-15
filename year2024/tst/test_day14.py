import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day14 import Day14

class TestDay14(unittest.TestCase):

    def setUp(self):
        self.example_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
        self.day14_instance = Day14(self.example_input, 11, 7)

    def test_part1(self):
        result = self.day14_instance.part1()
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()
