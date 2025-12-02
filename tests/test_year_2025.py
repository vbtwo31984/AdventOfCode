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
