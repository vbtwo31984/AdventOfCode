"""
Advent of Code 2025 - Day 6: [Puzzle Title]
https://adventofcode.com/2025/day/6
"""

import math

from src.utils.input_reader import InputReader


class Day06:
    """Solution for Day 6 of Advent of Code 2025."""
    
    def __init__(self, input_file: str = None):
        """
        Initialize the solution.
        
        Args:
            input_file: Path to a specific input file
        """
        self.input_reader = InputReader(input_file, year=2025, day=6)
        self.data = self.input_reader.read_lines()

    def get_problems(self) -> list[list[str]]:
        problems = []
        start = 0
        for i in range(len(self.data[0])):
            if i == len(self.data[0]) - 1:
                problem = []
                for line in self.data:
                    problem.append(line[start:].strip())
                problems.append(problem)
                start = i + 1
            all_spaces = True
            for line in self.data:
                if line[i] != " ":
                    all_spaces = False
            if all_spaces:
                problem = []
                for line in self.data:
                    problem.append(line[start:i].strip())
                problems.append(problem)
                start = i + 1
        return problems

    def get_problem_result(self, problem: list[str]) -> int:
        if problem[-1] == "*":
            # Multiply all elements except the last one
            return math.prod(int(num_str) if num_str != "" else 1 for num_str in problem[:-1])
        else:
            # Sum all elements except the last one
            return sum(int(num_str) if num_str != "" else 0 for num_str in problem[:-1])
    
    def solve_part1(self) -> int:
        """
        Solve part 1: [Description of part 1].
        
        Returns:
            Solution for part 1
        """
        problems = self.get_problems()
        return sum(self.get_problem_result(problem) for problem in problems)

    def get_problem_part2(self) -> list[list[str]]:
        problems = []
        problem = []
        for i in range(len(self.data[0])):
            all_spaces = True
            num = ""
            for j in range(len(self.data) - 1):
                if self.data[j][i] != " ":
                    all_spaces = False
                    num += self.data[j][i]
            if num != "":
                problem.append(num)
            if(self.data[-1][i] != " "):
                problem.append(self.data[-1][i])

            if all_spaces or i == len(self.data[0]) - 1:
                # Find operators in problem
                operators = [item for item in problem if item in ['*', '+']]
                # Only append if there's exactly one operator
                if len(operators) == 1:
                    # Remove operator from its current position
                    problem = [item for item in problem if item not in ['*', '+']]
                    # Add operator to the back
                    problem.append(operators[0])
                    problems.append(problem)
                problem = []
        return problems
    
    def solve_part2(self) -> int:
        """
        Solve part 2: [Description of part 2].
        
        Returns:
            Solution for part 2
        """
        problems = self.get_problem_part2()
        return sum(self.get_problem_result(problem) for problem in problems)


if __name__ == "__main__":
    day = Day06()
    print(f"Part 1: {day.solve_part1()}")
    print(f"Part 2: {day.solve_part2()}")
