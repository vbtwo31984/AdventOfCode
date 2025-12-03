"""
Advent of Code 2025 - Day 3: [Puzzle Title]
https://adventofcode.com/2025/day/3
"""

from src.utils.input_reader import InputReader


class Day03:
    """Solution for Day 3 of Advent of Code 2025."""
    
    def __init__(self, input_file: str = None):
        """
        Initialize the solution.
        
        Args:
            input_file: Path to a specific input file
        """
        self.input_reader = InputReader(input_file, year=2025, day=3)
        self.data = self.input_reader.read_lines()
    
    def solve_part1(self) -> int:
        """
        Solve part 1: [Description of part 1].
        
        Returns:
            Solution for part 1
        """
        total_joltage = 0
        for line in self.data:
            max1 = int(line[-2])
            max2 = int(line[-1])
            for char in reversed(line[:-2]):
                num = int(char)
                if num >= max1:
                    if max1 > max2:
                        max2 = max1
                    max1 = num
            total = int(f"{max1}{max2}")
            total_joltage += total

        return total_joltage
    
    def get_initial(self, line: str) -> list[int]:
        """Get the initial values for the line."""
        vals = []
        for i in range(-12, 0):
            vals.append(int(line[i]))
        return vals
    
    def replace_max(self, cur_max: list[int], num: int) -> list[int]:
        """Replace the max values."""
        for i in range(len(cur_max)):
            cur_num = num
            if num >= cur_max[i]:
                num = cur_max[i]
                cur_max[i] = cur_num
            else:
                break
        return cur_max
    
    def solve_part2(self) -> int:
        """
        Solve part 2: [Description of part 2].
        
        Returns:
            Solution for part 2
        """
        
        total_joltage = 0
        for line in self.data:
            cur_max = self.get_initial(line)
            for char in reversed(line[:-12]):
                num = int(char)
                cur_max = self.replace_max(cur_max, num)
            total_joltage += int("".join(str(x) for x in cur_max))
        return total_joltage


if __name__ == "__main__":
    day = Day03()
    print(f"Part 1: {day.solve_part1()}")
    print(f"Part 2: {day.solve_part2()}")
