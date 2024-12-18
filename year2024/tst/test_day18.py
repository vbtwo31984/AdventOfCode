import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day18 import Day18

class TestDay18(unittest.TestCase):

    def setUp(self):
        self.example_input = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
        self.day18_instance = Day18(self.example_input, 7)

    def test_part1(self):
        result = self.day18_instance.part1(12)
        self.assertEqual(result, 22)

    def test_part2(self):
        result = self.day18_instance.part2(13)
        self.assertEqual(result, "6,1")
    
if __name__ == '__main__':
    unittest.main()
