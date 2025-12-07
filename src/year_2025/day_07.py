"""
Advent of Code 2025 - Day 7: [Puzzle Title]
https://adventofcode.com/2025/day/7
"""

from src.utils.input_reader import InputReader


class Day07:
    """Solution for Day 7 of Advent of Code 2025."""
    
    def __init__(self, input_file: str = None):
        """
        Initialize the solution.
        
        Args:
            input_file: Path to a specific input file
        """
        self.input_reader = InputReader(input_file, year=2025, day=7)
        self.data = self.input_reader.read_lines()
    
    def solve_part1(self) -> int:
        """
        Solve part 1: [Description of part 1].
        
        Returns:
            Solution for part 1
        """
        beams = {self.data[0].index("S")}
        num_split = 0
        for line in self.data[1:]:
            new_beams = set()
            for beam in beams:
                if line[beam] == "^":
                    new_beams.add(beam - 1)
                    new_beams.add(beam + 1)
                    num_split += 1
                else:
                    new_beams.add(beam)
            beams = new_beams

        return num_split

    def num_timelines(self, start: int, cur_line: int, memo: dict[tuple[int, int], int]) -> int:
        if (start, cur_line) in memo:
            return memo[(start, cur_line)]
        if cur_line == len(self.data):
            return 1
        
        if self.data[cur_line][start] == ".":
            memo[(start, cur_line)] = self.num_timelines(start, cur_line + 1, memo)
        elif self.data[cur_line][start] == "^":
            memo[(start, cur_line)] = self.num_timelines(start - 1, cur_line + 1, memo) + self.num_timelines(start + 1, cur_line + 1, memo)
        return memo[(start, cur_line)]

    def solve_part2(self) -> int:
        """
        Solve part 2: [Description of part 2].
        
        Returns:
            Solution for part 2
        """
        start = self.data[0].index("S")
        memo = {}
        return self.num_timelines(start, 1, memo)


if __name__ == "__main__":
    day = Day07()
    print(f"Part 1: {day.solve_part1()}")
    print(f"Part 2: {day.solve_part2()}")
