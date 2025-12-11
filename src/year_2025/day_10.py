"""
Advent of Code 2025 - Day 10: [Puzzle Title]
https://adventofcode.com/2025/day/10
"""

from src.utils.input_reader import InputReader

class Machine:
    def __init__(self, line: str):
        parts = line.split(" ")
        self.final_state = parts[0][1:-1]
        self.buttons = [[int(x) for x in part[1:-1].split(",")] for part in parts[1:-1]]
        self.joltage = [int(x) for x in parts[-1][1:-1].split(",")]

    def fewest_button_presses(self) -> int:
        queue: list[tuple[str, int]] = [("." * len(self.final_state), 0)]
        visited = set()
        while queue:
            state, presses = queue.pop(0)
            if state == self.final_state:
                return presses
            if state in visited:
                continue
            visited.add(state)
            for button in self.buttons:
                new_state = list(state)
                for i in button:
                    new_state[i] = "#" if state[i] == "." else "."
                queue.append(("".join(new_state), presses + 1))
        return -1

class Day10:
    """Solution for Day 10 of Advent of Code 2025."""
    
    def __init__(self, input_file: str = None):
        """
        Initialize the solution.
        
        Args:
            input_file: Path to a specific input file
        """
        self.input_reader = InputReader(input_file, year=2025, day=10)
        self.data = self.input_reader.read_lines()
    
    def solve_part1(self) -> int:
        """
        Solve part 1: Find minimal button presses to reach target state.
        
        Returns:
            Solution for part 1
        """
        machines = [Machine(line) for line in self.data]
        presses = [machine.fewest_button_presses() for machine in machines]
        return sum(presses)
    
    def solve_part2(self) -> int:
        """
        Solve part 2: Find minimal button presses to reach target joltage.
        
        Returns:
            Solution for part 2
        """
        total = 0
        
        return total
    
    