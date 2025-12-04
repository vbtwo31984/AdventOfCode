"""
Advent of Code 2025 - Day 4: [Puzzle Title]
https://adventofcode.com/2025/day/4
"""

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
    
    def solve_part2(self) -> int:
        """
        Solve part 2: [Description of part 2].
        
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

        removed = True
        
        # Iterate through each position in the grid
        while removed:
            removed = False
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
                            removed = True
                            self.data[row][col] = '.'
        
        return accessible


if __name__ == "__main__":
    day = Day04()
    print(f"Part 1: {day.solve_part1()}")
    print(f"Part 2: {day.solve_part2()}")
