"""
Advent of Code 2015 - Day 1: [Not Quite Lisp]
https://adventofcode.com/2015/day/1
"""

from src.utils.input_reader import InputReader


class Day01:
    """Solution for Day 1 of Advent of Code 2015."""
    
    def __init__(self, input_file: str = None):
        """
        Initialize the solution.
        
        Args:
            input_file: Path to a specific input file
        """
        self.input_reader = InputReader(input_file, year=2015, day=1)
        self.data = self.input_reader.read_lines()
    
    def solve_part1(self) -> int:
        """
        Solve part 1: Find floor from input.
        
        Returns:
            Floor number after following instructions
        """
        # Read the input string (should be a single line with parentheses)
        input_string = self.data[0] if self.data else ""
        
        floor = 0
        for char in input_string:
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
        
        return floor
    
    def solve_part2(self) -> int:
        """
        Solve part 2: Find the position of the first character that causes Santa to enter the basement.
        
        Returns:
            Position of the first character that causes Santa to enter the basement (1-indexed)
        """
        # Read the input string (should be a single line with parentheses)
        input_string = self.data[0] if self.data else ""
        
        floor = 0
        for i, char in enumerate(input_string):
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
            
            # Check if we've entered the basement (floor < 0)
            if floor < 0:
                return i + 1  # Return 1-indexed position
        
        # If we never enter the basement
        return -1


if __name__ == "__main__":
    day = Day01()
    print(f"Part 1: {day.solve_part1()}")
    print(f"Part 2: {day.solve_part2()}")
