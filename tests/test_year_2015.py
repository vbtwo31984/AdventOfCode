"""
Tests for 2015 Advent of Code solutions.
"""

import pytest
from src.year_2015.day_01 import Day01

class TestDay01:
    """Test Day 1 solution."""
    
    def test_solve_part1_sample(self):
        """Test part 1 with sample input."""
        day = Day01(input_file=None)
        
        # Test cases for floor 0
        day.data = ["(())"]
        result = day.solve_part1()
        assert result == 0
        
        day.data = ["()()"]
        result = day.solve_part1()
        assert result == 0
        
        # Test cases for floor 3
        day.data = ["((("]
        result = day.solve_part1()
        assert result == 3
        
        day.data = ["(()(()("]
        result = day.solve_part1()
        assert result == 3
        
        day.data = ["))((((("]
        result = day.solve_part1()
        assert result == 3
        
        # Test cases for floor -1 (first basement level)
        day.data = ["())"]
        result = day.solve_part1()
        assert result == -1
        
        day.data = ["))("]
        result = day.solve_part1()
        assert result == -1
        
        # Test cases for floor -3
        day.data = [")))"]
        result = day.solve_part1()
        assert result == -3
        
        day.data = [")())())"]
        result = day.solve_part1()
        assert result == -3
    
    def test_solve_part2_sample(self):
        """Test part 2 with sample input."""
        day = Day01(input_file=None)
        day.data = [")"]
        
        # Test that the first character causes Santa to enter the basement
        result = day.solve_part2()
        assert result == 1  # Position 1 (1-indexed)
        
        day.data = ["()())"]
        result = day.solve_part2()
        assert result == 5  # Position 5 (1-indexed)
