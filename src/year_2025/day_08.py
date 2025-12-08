"""
Advent of Code 2025 - Day 8: [Puzzle Title]
https://adventofcode.com/2025/day/8
"""

from src.utils.input_reader import InputReader
import math

class UnionFind:
    def __init__(self, col: list[str]) -> None:
        self.parent = {c: c for c in col}
        self.rank = {c: 1 for c in col}
        self.total = len(col)

    def find(self, x: str) -> str:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: str, y: str) -> int:
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return self.total
        self.parent[yroot] = xroot
        self.rank[xroot] += self.rank[yroot]
        self.total -= 1
        return self.total

    def get_ranks(self) -> list[int]:
        return sorted([self.rank[c] for c in self.rank.keys() if self.find(c) == c], reverse=True)

class Day08:
    """Solution for Day 8 of Advent of Code 2025."""
    
    def __init__(self, input_file: str = None):
        """
        Initialize the solution.
        
        Args:
            input_file: Path to a specific input file
        """
        self.input_reader = InputReader(input_file, year=2025, day=8)
        self.data = self.input_reader.read_lines()
        self.distances = sorted(self.calculate_distance())

    def calculate_distance(self) -> list[tuple[int, str, str]]:
        distances = []
        calculated = set()
        for p1 in self.data:
            p1Coords = [int(c) for c in p1.split(",")]
            for p2 in self.data:
                if p1 == p2:
                    continue
                sortedPoints = "-".join(sorted([p1, p2]))
                if sortedPoints in calculated:
                    continue
                p2Coords = [int(c) for c in p2.split(",")]
                distance = math.sqrt((p2Coords[0] - p1Coords[0]) ** 2 + (p2Coords[1] - p1Coords[1]) ** 2 + (p2Coords[2] - p1Coords[2]) ** 2)
                distances.append((distance, p1, p2))
                calculated.add(sortedPoints)
        return distances
    
    def solve_part1(self, num_shortest = 1000) -> int:
        """
        Solve part 1: [Description of part 1].
        
        Returns:
            Solution for part 1
        """
        distances = self.distances[:num_shortest]
        union_find = UnionFind(self.data)
        for d in distances:
            union_find.union(d[1], d[2])
        ranks = union_find.get_ranks()[:3]
        return math.prod(ranks)
    
    def solve_part2(self) -> int:
        """
        Solve part 2: [Description of part 2].
        
        Returns:
            Solution for part 2
        """
        union_find = UnionFind(self.data)
        for d in self.distances:
            num_circuits = union_find.union(d[1], d[2])
            if num_circuits == 1:
                x1 = int(d[1].split(",")[0])
                x2 = int(d[2].split(",")[0])
                return x1 * x2

if __name__ == "__main__":
    day = Day08()
    print(f"Part 1: {day.solve_part1()}")
    print(f"Part 2: {day.solve_part2()}")
