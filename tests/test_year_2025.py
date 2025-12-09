"""
Tests for 2025 Advent of Code solutions.
"""

import pytest
from src.year_2025.day_01 import Day01


class TestDay01:
    """Test Day 1 solution."""
    
    def test_solve_part1_sample(self):
        """Test part 1 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        day = Day01(input_file=None)
        day.data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part1()
        assert result == 3
    
    def test_solve_part2_sample(self):
        """Test part 2 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        day = Day01(input_file=None)
        day.data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part2()
        assert result == 6


class TestDay02:
    """Test Day 2 solution."""
    
    def test_solve_part1_sample(self):
        """Test part 1 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_02 import Day02
        
        day = Day02(input_file=None)
        day.data = ["11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"]
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part1()
        assert result == 1227775554
    
    def test_solve_part2_sample(self):
        """Test part 2 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_02 import Day02
        
        day = Day02(input_file=None)
        day.data = ["11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"]
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part2()
        assert result == 4174379265


class TestDay03:
    """Test Day 3 solution."""
    
    def test_solve_part1_sample(self):
        """Test part 1 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_03 import Day03
        
        day = Day03(input_file=None)
        day.data = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part1()
        assert result == 357
    
    def test_solve_part2_sample(self):
        """Test part 2 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_03 import Day03
        
        day = Day03(input_file=None)
        day.data = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part2()
        assert result == 3121910778619


class TestDay04:
    """Test Day 4 solution."""

    def get_input(self):
        lines = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".splitlines()
        return [list(line) for line in lines]
    
    def test_solve_part1_sample(self):
        """Test part 1 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_04 import Day04
        
        day = Day04(input_file=None)
        day.data = self.get_input()
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part1()
        assert result == 13
    
    def test_solve_part2_sample(self):
        """Test part 2 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_04 import Day04
        
        day = Day04(input_file=None)
        day.data = self.get_input()
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part2()
        assert result == 43


class TestDay05:
    """Test Day 5 solution."""

    def get_input(self):
        blocks = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".split("\n\n")
        return [block.split("\n") for block in blocks]
    
    def test_solve_part1_sample(self):
        """Test part 1 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_05 import Day05
        
        day = Day05(input_file=None)
        day.data = self.get_input()
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part1()
        assert result == 3
    
    def test_solve_part2_sample(self):
        """Test part 2 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_05 import Day05
        
        day = Day05(input_file=None)
        day.data = self.get_input()
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part2()
        assert result == 14


class TestDay06:
    """Test Day 6 solution."""

    def get_input(self):
        return """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.splitlines()
    
    def test_solve_part1_sample(self):
        """Test part 1 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_06 import Day06
        
        day = Day06(input_file=None)
        day.data = self.get_input()
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part1()
        assert result == 4277556
    
    def test_solve_part2_sample(self):
        """Test part 2 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_06 import Day06
        
        day = Day06(input_file=None)
        day.data = self.get_input()
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part2()
        assert result == 3263827


class TestDay07:
    """Test Day 7 solution."""
    
    def get_input(self):
        return """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".splitlines()

    def test_solve_part1_sample(self):
        """Test part 1 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_07 import Day07
        
        day = Day07(input_file=None)
        day.data = self.get_input()
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part1()
        assert result == 21
    
    def test_solve_part2_sample(self):
        """Test part 2 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_07 import Day07
        
        day = Day07(input_file=None)
        day.data = self.get_input()
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part2()
        assert result == 40


class TestDay08:
    """Test Day 8 solution."""

    def get_data(self):
        return """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""".splitlines()
    
    def test_solve_part1_sample(self):
        """Test part 1 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_08 import Day08
        
        day = Day08(input_file=None)
        day.data = self.get_data()
        day.distances = sorted(day.calculate_distance())
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part1(10)
        assert result == 40
    
    def test_solve_part2_sample(self):
        """Test part 2 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_08 import Day08
        
        day = Day08(input_file=None)
        day.data = self.get_data()
        day.distances = sorted(day.calculate_distance())
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part2()
        assert result == 25272


class TestDay09:
    """Test Day 9 solution."""

    def get_data(self):
        return """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".splitlines()
    
    def test_solve_part1_sample(self):
        """Test part 1 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_09 import Day09
        
        day = Day09(input_file=None)
        day.data = self.get_data()
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part1()
        assert result == 50
    
    def test_solve_part2_sample(self):
        """Test part 2 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_2025.day_09 import Day09
        
        day = Day09(input_file=None)
        day.data = self.get_data()
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part2()
        assert result == 24
