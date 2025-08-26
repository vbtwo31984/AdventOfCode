#!/usr/bin/env python3
"""
Helper script to create new day solution files.
Usage: python create_day.py --year 2024 --day 2
"""

import argparse
import os
from pathlib import Path


def create_day_solution(year: int, day: int):
    """Create a new day solution file and input file."""
    
    # Create year directory if it doesn't exist
    year_dir = Path(f"src/year_{year}")
    year_dir.mkdir(exist_ok=True)
    
    # Create input directory if it doesn't exist
    input_dir = Path(f"inputs/{year}")
    input_dir.mkdir(exist_ok=True)
    
    # Create solution file
    solution_file = year_dir / f"day_{day:02d}.py"
    
    if solution_file.exists():
        print(f"Solution file {solution_file} already exists!")
        return
    
    solution_content = f'''"""
Advent of Code {year} - Day {day}: [Puzzle Title]
https://adventofcode.com/{year}/day/{day}
"""

from src.utils.input_reader import InputReader


class Day{day:02d}:
    """Solution for Day {day} of Advent of Code {year}."""
    
    def __init__(self, input_file: str = None):
        """
        Initialize the solution.
        
        Args:
            input_file: Path to a specific input file
        """
        self.input_reader = InputReader(input_file, year={year}, day={day})
        self.data = self.input_reader.read_lines()
    
    def solve_part1(self) -> int:
        """
        Solve part 1: [Description of part 1].
        
        Returns:
            Solution for part 1
        """
        # TODO: Implement solution for part 1
        pass
    
    def solve_part2(self) -> int:
        """
        Solve part 2: [Description of part 2].
        
        Returns:
            Solution for part 2
        """
        # TODO: Implement solution for part 2
        pass


if __name__ == "__main__":
    day = Day{day:02d}()
    print(f"Part 1: {{day.solve_part1()}}")
    print(f"Part 2: {{day.solve_part2()}}")
'''
    
    with open(solution_file, 'w') as f:
        f.write(solution_content)
    
    print(f"Created solution file: {solution_file}")
    
    # Create input file
    input_file = input_dir / f"day_{day:02d}.txt"
    
    if input_file.exists():
        print(f"Input file {input_file} already exists!")
    else:
        input_content = f"# Input file for {year} Day {day}\n# Replace with actual puzzle input\n"
        with open(input_file, 'w') as f:
            f.write(input_content)
        print(f"Created input file: {input_file}")
    
    # Create test file
    test_file = Path(f"tests/test_year_{year}.py")
    
    if test_file.exists():
        # Add test methods to existing file
        with open(test_file, 'r') as f:
            content = f.read()
        
        # Check if test class already exists
        if f"class TestDay{day:02d}" not in content:
            # Add test class at the end of the file
            test_class = f'''

class TestDay{day:02d}:
    """Test Day {day} solution."""
    
    def test_solve_part1_sample(self):
        """Test part 1 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_{year}.day_{day:02d} import Day{day:02d}
        
        day = Day{day:02d}(input_file=None)
        day.data = ["sample", "input"]
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part1()
        # assert result == expected_result
    
    def test_solve_part2_sample(self):
        """Test part 2 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        from src.year_{year}.day_{day:02d} import Day{day:02d}
        
        day = Day{day:02d}(input_file=None)
        day.data = ["sample", "input"]
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part2()
        # assert result == expected_result
'''
            
            with open(test_file, 'a') as f:
                f.write(test_class)
            print(f"Added test class to: {test_file}")
    else:
        # Create new test file
        test_content = f'''"""
Tests for {year} Advent of Code solutions.
"""

import pytest
from src.year_{year}.day_{day:02d} import Day{day:02d}


class TestDay{day:02d}:
    """Test Day {day} solution."""
    
    def test_solve_part1_sample(self):
        """Test part 1 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        day = Day{day:02d}(input_file=None)
        day.data = ["sample", "input"]
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part1()
        # assert result == expected_result
    
    def test_solve_part2_sample(self):
        """Test part 2 with sample input."""
        # TODO: Add sample input and expected result when puzzle is implemented
        day = Day{day:02d}(input_file=None)
        day.data = ["sample", "input"]
        
        # Placeholder test - will need to be updated with actual puzzle
        result = day.solve_part2()
        # assert result == expected_result
'''
        
        with open(test_file, 'w') as f:
            f.write(test_content)
        print(f"Created test file: {test_file}")
    
    print(f"\nDay {day} setup complete! You can now:")
    print(f"1. Add your puzzle input to: inputs/{year}/day_{day:02d}.txt")
    print(f"2. Implement your solution in: src/year_{year}/day_{day:02d}.py")
    print(f"3. Run your solution with: python run.py --year {year} --day {day}")
    print(f"4. Run tests with: pytest tests/test_year_{year}.py::TestDay{day:02d}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Create a new day solution")
    parser.add_argument("--year", "-y", type=int, required=True, help="Year of the puzzle")
    parser.add_argument("--day", "-d", type=int, required=True, help="Day of the puzzle")
    
    args = parser.parse_args()
    
    if not 1 <= args.day <= 25:
        print("Error: Day must be between 1 and 25")
        return
    
    if not 2015 <= args.year <= 2030:
        print("Error: Year must be between 2015 and 2030")
        return
    
    create_day_solution(args.year, args.day)


if __name__ == "__main__":
    main()
