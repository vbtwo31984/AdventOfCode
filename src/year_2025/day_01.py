"""
Advent of Code 2025 - Day 1: [Puzzle Title]
https://adventofcode.com/2025/day/1
"""

import math

from src.utils.input_reader import InputReader

class Day01:
    """Solution for Day 1 of Advent of Code 2025."""
    
    def __init__(self, input_file: str = None):
        """
        Initialize the solution.
        
        Args:
            input_file: Path to a specific input file
        """
        self.input_reader = InputReader(input_file, year=2025, day=1)
        self.data = self.input_reader.read_lines()
    
    def solve_part1(self) -> int:
        """
        Solve part 1: [Description of part 1].
        
        Returns:
            Solution for part 1
        """
        current = 50
        num_zero = 0
        
        for line in self.data:
            direction = line[0]
            digit = int(line[1:])
            
            if direction == 'L':
                current = current - digit
            elif direction == 'R':
                current = current + digit
            
            if current % 100 == 0:
                num_zero += 1
        
        return num_zero
    
    def solve_part2(self) -> int:
        """
        Solve part 2: [Description of part 2].
        
        Returns:
            Solution for part 2
        """
        
        current = 50
        num_zero = 0
        
        for line in self.data:
            direction = line[0]
            digit = int(line[1:])
            lastCurrent = current

            num_zero += math.floor(digit / 100) # num full rotations
            
            if direction == 'L':
                current = (current - digit) % 100
                if current > lastCurrent and lastCurrent != 0 and current != 0:
                    num_zero += 1
            elif direction == 'R':
                current = (current + digit) % 100
                if current < lastCurrent and lastCurrent != 0 and current != 0:
                    num_zero += 1

            if(current == 0 and digit % 100 != 0):
                num_zero += 1

            print(f"Line: {line}, Current: {current}, Num Zero: {num_zero}")
        
        return num_zero


if __name__ == "__main__":
    day = Day01()
    print(f"Part 1: {day.solve_part1()}")
    print(f"Part 2: {day.solve_part2()}")
