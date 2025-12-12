"""
Advent of Code 2025 - Day 12: [Puzzle Title]
https://adventofcode.com/2025/day/12
"""

from src.utils.input_reader import InputReader
import math

class Day12:
    """Solution for Day 12 of Advent of Code 2025."""
    
    def __init__(self, input_file: str = None):
        """
        Initialize the solution.
        
        Args:
            input_file: Path to a specific input file
        """
        self.input_reader = InputReader(input_file, year=2025, day=12)
        self.data = self.input_reader.read_blocks()
    
    def solve_part1(self) -> int:
        """
        Solve part 1: [Description of part 1].
        
        Returns:
            Solution for part 1
        """
        boxes = self.data[-1].splitlines()
        fit = 0
        for box in boxes:
            area = math.prod([int(x) for x in box[0:5].split("x")])
            num_presents = sum([int(x) for x in box[7:].split(" ")])
            if area >= 8 * num_presents:
                fit += 1
        return fit
    
    def solve_part2(self) -> int:
        """
        Solve part 2: [Description of part 2].
        
        Returns:
            Solution for part 2
        """
        # TODO: Implement solution for part 2
        pass


if __name__ == "__main__":
    day = Day12()
    print(f"Part 1: {day.solve_part1()}")
    print(f"Part 2: {day.solve_part2()}")
