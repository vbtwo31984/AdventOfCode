"""
Advent of Code 2025 - Day 5: [Puzzle Title]
https://adventofcode.com/2025/day/5
"""

from src.utils.input_reader import InputReader


class Day05:
    """Solution for Day 5 of Advent of Code 2025."""
    
    def __init__(self, input_file: str = None):
        """
        Initialize the solution.
        
        Args:
            input_file: Path to a specific input file
        """
        self.input_reader = InputReader(input_file, year=2025, day=5)
        self.data = self.input_reader.read_blocks_as_lines()

    def get_ranges(self):
        ranges = []
        for line in self.data[0]:
            range = line.split("-")
            ranges.append((int(range[0]), int(range[1])))
        return ranges
    
    def solve_part1(self) -> int:
        """
        Solve part 1: [Description of part 1].
        
        Returns:
            Solution for part 1
        """
        ranges = self.get_ranges()
        ingredients = [int(i) for i in self.data[1]]
        num_fresh = 0
        for i in ingredients:
            for r in ranges:
                if r[0] <= i <= r[1]:
                    num_fresh += 1
                    break

        return num_fresh
    
    def solve_part2(self) -> int:
        """
        Solve part 2: [Description of part 2].
        
        Returns:
            Solution for part 2
        """
        ranges = self.get_ranges()
        ranges.sort()
        num_fresh = 0
        start = 0
        for r in ranges:
            range_start = r[0] if r[0] > start else start + 1
            if r[1] >= range_start:
                num_fresh += r[1] - range_start + 1
                start = r[1]
        return num_fresh


if __name__ == "__main__":
    day = Day05()
    print(f"Part 1: {day.solve_part1()}")
    print(f"Part 2: {day.solve_part2()}")
