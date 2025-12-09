"""
Advent of Code 2025 - Day 9: [Puzzle Title]
https://adventofcode.com/2025/day/9
"""

import shapely
from src.utils.input_reader import InputReader


class Day09:
    """Solution for Day 9 of Advent of Code 2025."""
    
    def __init__(self, input_file: str | None = None):
        """
        Initialize the solution.
        
        Args:
            input_file: Path to a specific input file
        """
        self.input_reader = InputReader(input_file, year=2025, day=9)
        self.data = self.input_reader.read_lines()

    def calculate_area(self, polygon: shapely.Polygon | None = None) -> list[tuple[int, str, str]]:
        areas = []
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
                area = (abs(p2Coords[0] - p1Coords[0]) + 1) * (abs(p2Coords[1] - p1Coords[1]) + 1)
                if polygon is None or polygon.contains(shapely.box(p1Coords[0], p1Coords[1], p2Coords[0], p2Coords[1])):
                    areas.append((area, p1, p2))
                calculated.add(sortedPoints)
        return areas
    
    def solve_part1(self) -> int:
        """
        Solve part 1: [Description of part 1].
        
        Returns:
            Solution for part 1
        """
        areas = sorted(self.calculate_area(), reverse=True)
        return areas[0][0]
    
    def solve_part2(self) -> int:
        """
        Solve part 2: Find the largest rectangle with corners at polygon vertices
        that is fully contained within the polygon.
        
        Returns:
            Area of the largest rectangle
        """
        
        points: list[tuple[int, int]] = []
        for line in self.data:
            coords = line.split(",")
            points.append((int(coords[0]), int(coords[1])))
        points.append(points[0])
        polygon = shapely.Polygon(points)

        areas = sorted(self.calculate_area(polygon), reverse=True)
        return areas[0][0]


if __name__ == "__main__":
    day = Day09()
    print(f"Part 1: {day.solve_part1()}")
    print(f"Part 2: {day.solve_part2()}")
