import unittest
import sys
sys.path.insert(0, 'year2024')
from src.day23 import Day23

class TestDay23(unittest.TestCase):

    def setUp(self):
        
        self.example_input = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
        self.day23_instance = Day23(self.example_input)

    def test_part1(self):
        result = self.day23_instance.part1()
        self.assertEqual(result, 7)

    def test_part2(self):
        result = self.day23_instance.part2()
        self.assertEqual(result, "co,de,ka,ta")

if __name__ == '__main__':
    unittest.main()
