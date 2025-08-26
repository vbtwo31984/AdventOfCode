#!/usr/bin/env python3
"""
Main runner script for Advent of Code solutions.
Allows running any year/day combination with optional custom input files.
"""

import argparse
import importlib
import sys
from pathlib import Path


def get_solution_class(year: int, day: int):
    """
    Dynamically import and return the solution class for a given year and day.
    
    Args:
        year: Year of the puzzle
        day: Day of the puzzle
        
    Returns:
        Solution class for the specified year and day
        
    Raises:
        ImportError: If the solution module cannot be imported
        AttributeError: If the solution class is not found
    """
    try:
        module_name = f"src.year_{year}.day_{day:02d}"
        module = importlib.import_module(module_name)
        
        # Find the solution class (should be named Day{day:02d})
        class_name = f"Day{day:02d}"
        solution_class = getattr(module, class_name)
        
        return solution_class
        
    except ImportError as e:
        raise ImportError(f"Could not import solution for year {year}, day {day}: {e}")
    except AttributeError as e:
        raise AttributeError(f"Could not find solution class for year {year}, day {day}: {e}")


def run_solution(year: int, day: int, input_file: str = None, part: int = None):
    """
    Run a specific Advent of Code solution.
    
    Args:
        year: Year of the puzzle
        day: Day of the puzzle
        input_file: Optional custom input file path
        part: Optional specific part to run (1 or 2)
    """
    try:
        # Import the solution class
        solution_class = get_solution_class(year, day)
        
        # Create instance with optional custom input
        if input_file:
            solution = solution_class(input_file)
        else:
            solution = solution_class()
        
        # Run the solution(s)
        if part is None or part == 1:
            result1 = solution.solve_part1()
            print(f"Part 1: {result1}")
        
        if part is None or part == 2:
            result2 = solution.solve_part2()
            print(f"Part 2: {result2}")
            
    except Exception as e:
        print(f"Error running solution for year {year}, day {day}: {e}")
        sys.exit(1)


def list_available_solutions():
    """List all available solutions in the project."""
    src_dir = Path("src")
    available = []
    
    for year_dir in src_dir.glob("year_*"):
        if year_dir.is_dir():
            year = int(year_dir.name.split("_")[1])
            for day_file in year_dir.glob("day_*.py"):
                day = int(day_file.name.split("_")[1].split(".")[0])
                available.append((year, day))
    
    if available:
        print("Available solutions:")
        available.sort()
        for year, day in available:
            print(f"  Year {year}, Day {day}")
    else:
        print("No solutions found.")


def main():
    """Main entry point for the runner script."""
    parser = argparse.ArgumentParser(
        description="Run Advent of Code solutions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run.py --year 2023 --day 1
  python run.py --year 2023 --day 1 --part 1
  python run.py --year 2023 --day 1 --input custom_input.txt
  python run.py --list
        """
    )
    
    parser.add_argument(
        "--year", "-y",
        type=int,
        help="Year of the puzzle (e.g., 2023)"
    )
    
    parser.add_argument(
        "--day", "-d",
        type=int,
        help="Day of the puzzle (e.g., 1)"
    )
    
    parser.add_argument(
        "--input", "-i",
        type=str,
        help="Custom input file path"
    )
    
    parser.add_argument(
        "--part", "-p",
        type=int,
        choices=[1, 2],
        help="Run only a specific part (1 or 2)"
    )
    
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List all available solutions"
    )
    
    args = parser.parse_args()
    
    # Handle --list option
    if args.list:
        list_available_solutions()
        return
    
    # Validate required arguments
    if args.year is None or args.day is None:
        parser.error("--year and --day are required (unless using --list)")
    
    # Validate day range
    if not 1 <= args.day <= 25:
        parser.error("Day must be between 1 and 25")
    
    # Validate year range (reasonable bounds)
    if not 2015 <= args.year <= 2030:
        parser.error("Year must be between 2015 and 2030")
    
    # Run the solution
    run_solution(args.year, args.day, args.input, args.part)


if __name__ == "__main__":
    main()
