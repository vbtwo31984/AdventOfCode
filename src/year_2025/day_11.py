"""
Advent of Code 2025 - Day 11: [Puzzle Title]
https://adventofcode.com/2025/day/11
"""

from src.utils.input_reader import InputReader
from functools import cache

class Day11:
    """Solution for Day 11 of Advent of Code 2025."""
    
    def __init__(self, input_file: str = None):
        """
        Initialize the solution.
        
        Args:
            input_file: Path to a specific input file
        """
        self.input_reader = InputReader(input_file, year=2025, day=11)
        self.data = self.input_reader.read_lines()

    def get_paths(self) -> dict[str, set[str]]:
        paths = {}
        for line in self.data:
            parts = line.split(": ")
            targets = parts[1].split(" ")
            paths[parts[0]] = set(targets)
        return paths
    
    def visit(self, path: str) -> int:
        if path == "out":
            return 1
        total = 0
        for target in self.paths[path]:
            total += self.visit(target)
        return total

    def solve_part1(self) -> int:
        """
        Solve part 1: [Description of part 1].
        
        Returns:
            Solution for part 1
        """
        self.paths = self.get_paths()
        return self.visit("you")
    
    @cache
    def part2_visit(self, cur: tuple[str, bool, bool]) -> int:
        dac_visited = cur[1] or cur[0] == "dac"
        fft_visited = cur[2] or cur[0] == "fft"

        if cur[0] == "out" and dac_visited and fft_visited:
            return 1
        if cur[0] == "out":
            return 0
        total = 0

        for target in self.paths[cur[0]]:
            result = self.part2_visit((target, dac_visited, fft_visited))
            total += result
        return total
    
    def solve_part2(self) -> int:
        """
        Solve part 2: [Description of part 2].
        
        Returns:
            Solution for part 2
        """
        self.paths = self.get_paths()  
        return self.part2_visit(("svr", False, False))


if __name__ == "__main__":
    day = Day11()
    print(f"Part 1: {day.solve_part1()}")
    print(f"Part 2: {day.solve_part2()}")
