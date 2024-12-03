import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day3 import Day3

class TestDay3(unittest.TestCase):

    def setUp(self):
        example_input1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        self.day3_instance = Day3(example_input1)

        example_input2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        self.day3_instance2 = Day3(example_input2)

    def test_part1(self):
        result = self.day3_instance.part1()
        self.assertEqual(result, 161)

    def test_part2(self):
        result = self.day3_instance2.part2()
        self.assertEqual(result, 48)

if __name__ == '__main__':
    unittest.main()
