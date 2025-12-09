"""
Advent of Code 2025 - Day 9: [Puzzle Title]
https://adventofcode.com/2025/day/9
"""

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

    def calculate_area(self) -> list[tuple[int, str, str]]:
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
    
    def intersects(self, p1: list[int], p2: list[int], polygon: list[tuple[int, int]]) -> bool:
        minX = min(p1[0], p2[0])
        maxX = max(p1[0], p2[0])
        minY = min(p1[1], p2[1])
        maxY = max(p1[1], p2[1])

        start = polygon[0]
        for line in polygon[1:]:
            if line[0] != start[0]: # horizontal line
                minLine = min(start[0], line[0]) 
                maxLine = max(start[0], line[0])
                if minY <= line[1] <= maxY and (minX < minLine < maxX or minX < maxLine < maxX or (minLine < minX and maxLine > maxX)):
                    return True
            else: # vertical line
                minLine = min(start[1], line[1])
                maxLine = max(start[1], line[1])
                if minX <= line[0] <= maxX and (minY < minLine < maxY or minY < maxLine < maxY or (minLine < minY and maxLine > maxY)):
                    return True
            start = line
        return False
    
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

        areas = sorted(self.calculate_area(), reverse=True)
        for area in areas:
            p1 = [int(c) for c in area[1].split(",")]
            p2 = [int(c) for c in area[2].split(",")]
            if not self.intersects(p1, p2, points):
                return area[0]
        return 0


if __name__ == "__main__":
    day = Day09()
    print(f"Part 1: {day.solve_part1()}")
    print(f"Part 2: {day.solve_part2()}")
