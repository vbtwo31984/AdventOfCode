"""
Advent of Code 2025 - Day 4: [Puzzle Title]
https://adventofcode.com/2025/day/4
"""

import time
from src.utils.input_reader import InputReader


class Day04:
    """Solution for Day 4 of Advent of Code 2025."""
    
    def __init__(self, input_file: str = None):
        """
        Initialize the solution.
        
        Args:
            input_file: Path to a specific input file
        """
        self.input_reader = InputReader(input_file, year=2025, day=4)
        self.data = self.input_reader.read_grid()
    
    def solve_part1(self) -> int:
        """
        Solve part 1: Count '@' characters with less than 4 adjacent '@' characters.
        
        Returns:
            Solution for part 1
        """
        accessible = 0
        
        # Get grid dimensions
        rows = len(self.data)
        if rows == 0:
            return accessible
        cols = len(self.data[0])
        
        # Define 8 directions: top-left, top, top-right, left, right, bottom-left, bottom, bottom-right
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Iterate through each position in the grid
        for row in range(rows):
            for col in range(cols):
                # Check if current position is '@'
                if self.data[row][col] == '@':
                    # Count adjacent '@' characters
                    adjacent_count = 0
                    
                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc
                        
                        # Check bounds
                        if 0 <= new_row < rows and 0 <= new_col < cols:
                            # Check if adjacent position is '@'
                            if self.data[new_row][new_col] == '@':
                                adjacent_count += 1
                    
                    # If less than 4 adjacent '@' characters, increment accessible
                    if adjacent_count < 4:
                        accessible += 1
        
        return accessible
    
    def count_adjacent(self, row: int, col: int, rows: int, cols: int, directions: list) -> int:
        """
        Count adjacent '@' characters for a given position.
        
        Args:
            row: Row position
            col: Column position
            rows: Total rows in grid
            cols: Total columns in grid
            directions: List of direction tuples
            
        Returns:
            Count of adjacent '@' characters
        """
        count = 0
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if self.data[new_row][new_col] == '@':
                    count += 1
        
        return count
    
    def solve_part2(self) -> int:
        """
        Solve part 2: Count '@' characters removed using set-based cascading removal.
        
        Returns:
            Solution for part 2
        """
        accessible = 0
        
        # Get grid dimensions
        rows = len(self.data)
        if rows == 0:
            return accessible
        cols = len(self.data[0])
        
        # Define 8 directions: top-left, top, top-right, left, right, bottom-left, bottom, bottom-right
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Initial scan: find all '@' cells with < 4 neighbors
        to_remove = set()
        for row in range(rows):
            for col in range(cols):
                if self.data[row][col] == '@':
                    if self.count_adjacent(row, col, rows, cols, directions) < 4:
                        to_remove.add((row, col))
        
        # Process set - cascading removal
        while to_remove:
            row, col = to_remove.pop()
            
            # Remove cell
            self.data[row][col] = '.'
            accessible += 1
            
            # Check all neighbors - if they now have < 4 neighbors, add to set
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if self.data[new_row][new_col] == '@':
                        if self.count_adjacent(new_row, new_col, rows, cols, directions) < 4:
                            to_remove.add((new_row, new_col))
        
        return accessible


if __name__ == "__main__":
    day = Day04()
    
    start_time = time.time()
    result1 = day.solve_part1()
    end_time = time.time()
    elapsed_ms = (end_time - start_time) * 1000
    print(f"Part 1: {result1}")
    print(f"Part 1 took {elapsed_ms:.2f}ms to run")
    
    start_time = time.time()
    result2 = day.solve_part2()
    end_time = time.time()
    elapsed_ms = (end_time - start_time) * 1000
    print(f"Part 2: {result2}")
    print(f"Part 2 took {elapsed_ms:.2f}ms to run")
