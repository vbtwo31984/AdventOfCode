"""
Advent of Code 2025 - Day 2: [Puzzle Title]
https://adventofcode.com/2025/day/2
"""

from src.utils.input_reader import InputReader


class Day02:
    """Solution for Day 2 of Advent of Code 2025."""
    
    def __init__(self, input_file: str = None):
        """
        Initialize the solution.
        
        Args:
            input_file: Path to a specific input file
        """
        self.input_reader = InputReader(input_file, year=2025, day=2)
        self.data = self.input_reader.read_lines()
    
    def solve_part1(self) -> int:
        """
        Solve part 1: Filter IDs where first half equals second half.
        
        Returns:
            Count of IDs that match the criteria
        """
        ranges = self.data[0].split(",")
        invalid_ids = []
        for range in ranges:
            range_parts = range.split("-")
            start = range_parts[0]
            end = int(range_parts[1])
            
            half = start[0:len(start) // 2]
            if(len(start) % 2 != 0):
                half = int("1" + "0" * (len(start) // 2))
            else:
                half = int(half)

            while True:
                full = int(f"{half}{half}")
                if full > end:
                    break
                if full >= int(start):
                    invalid_ids.append(full)
                half += 1
        return sum(invalid_ids)
    
    def solve_part2(self) -> int:
        """
        Solve part 2: [Description of part 2].
        
        Returns:
            Solution for part 2
        """
        ranges = self.data[0].split(",")
        invalid_ids = []
        for range in ranges:
            range_parts = range.split("-")
            start = int(range_parts[0])
            end = int(range_parts[1])
            max  = int(range_parts[1][0:len(range_parts[1]) // 2]) if len(range_parts[1]) % 2 == 0 else int("1" + "0" * (len(range_parts[1]) // 2))
            i = 1
            while i <= max:
                full = int(f"{i}{i}")
                while full < start:
                    full = int(f"{full}{i}")
                if full <= end and full not in invalid_ids:
                    invalid_ids.append(full)
                i += 1
        return sum(invalid_ids)


if __name__ == "__main__":
    day = Day02()
    print(f"Part 1: {day.solve_part1()}")
    print(f"Part 2: {day.solve_part2()}")
