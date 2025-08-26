"""
Common utility functions for Advent of Code puzzles.
Contains frequently used algorithms and data structures.
"""

from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, deque
import heapq
import math


def manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    """Calculate Manhattan distance between two 2D points."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def euclidean_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    """Calculate Euclidean distance between two 2D points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def get_neighbors_4(
    pos: Tuple[int, int], grid: List[List], include_diagonals: bool = False
) -> List[Tuple[int, int]]:
    """
    Get valid 4-directional neighbors of a position in a grid.

    Args:
        pos: Current position (row, col)
        grid: 2D grid
        include_diagonals: Whether to include diagonal neighbors

    Returns:
        List of valid neighbor positions
    """
    row, col = pos
    rows, cols = len(grid), len(grid[0])
    neighbors = []

    # 4-directional neighbors
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    if include_diagonals:
        directions.extend([(1, 1), (1, -1), (-1, 1), (-1, -1)])

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbors.append((new_row, new_col))

    return neighbors


def bfs(
    start: Tuple[int, int],
    goal: Tuple[int, int],
    grid: List[List],
    is_walkable: callable = None,
) -> Optional[List[Tuple[int, int]]]:
    """
    Breadth-first search to find shortest path between two points.

    Args:
        start: Starting position
        goal: Goal position
        grid: 2D grid
        is_walkable: Function to check if a position is walkable

    Returns:
        List of positions forming the path, or None if no path exists
    """
    if is_walkable is None:
        is_walkable = lambda pos: True

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (row, col), path = queue.popleft()

        if (row, col) == goal:
            return path

        for neighbor in get_neighbors_4((row, col), grid):
            if neighbor not in visited and is_walkable(neighbor):
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return None


def dijkstra(
    start: Tuple[int, int],
    goal: Tuple[int, int],
    grid: List[List],
    get_cost: callable = None,
) -> Optional[Tuple[int, List[Tuple[int, int]]]]:
    """
    Dijkstra's algorithm to find shortest path with weighted edges.

    Args:
        start: Starting position
        goal: Goal position
        grid: 2D grid
        get_cost: Function to get cost of moving to a position

    Returns:
        Tuple of (total_cost, path), or None if no path exists
    """
    if get_cost is None:
        get_cost = lambda pos: 1

    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, (row, col), path = heapq.heappop(pq)

        if (row, col) == goal:
            return cost, path

        if (row, col) in visited:
            continue

        visited.add((row, col))

        for neighbor in get_neighbors_4((row, col), grid):
            if neighbor not in visited:
                new_cost = cost + get_cost(neighbor)
                new_path = path + [neighbor]
                heapq.heappush(pq, (new_cost, neighbor, new_path))

    return None


def lcm(a: int, b: int) -> int:
    """Calculate least common multiple of two numbers."""
    return abs(a * b) // math.gcd(a, b)


def lcm_list(numbers: List[int]) -> int:
    """Calculate least common multiple of a list of numbers."""
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result


def mod_inverse(a: int, m: int) -> int:
    """Calculate modular multiplicative inverse using extended Euclidean algorithm."""

    def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return (x % m + m) % m


def chinese_remainder_theorem(remainders: List[int], moduli: List[int]) -> int:
    """
    Solve system of congruences using Chinese Remainder Theorem.

    Args:
        remainders: List of remainders
        moduli: List of moduli (must be pairwise coprime)

    Returns:
        Solution to the system of congruences
    """
    if len(remainders) != len(moduli):
        raise ValueError("Remainders and moduli must have same length")

    total = 0
    product = 1

    for modulus in moduli:
        product *= modulus

    for remainder, modulus in zip(remainders, moduli):
        pi = product // modulus
        total += remainder * pi * mod_inverse(pi, modulus)

    return total % product


def parse_int_grid(grid: List[List[str]]) -> List[List[int]]:
    """Convert a grid of string digits to integers."""
    return [[int(cell) for cell in row] for row in grid]


def transpose_grid(grid: List[List]) -> List[List]:
    """Transpose a 2D grid (swap rows and columns)."""
    return list(zip(*grid))


def rotate_grid_90_clockwise(grid: List[List]) -> List[List]:
    """Rotate a 2D grid 90 degrees clockwise."""
    return list(zip(*grid))[::-1]


def rotate_grid_90_counterclockwise(grid: List[List]) -> List[List]:
    """Rotate a 2D grid 90 degrees counterclockwise."""
    return list(zip(*grid[::-1]))


def print_grid(grid: List[List], separator: str = "") -> None:
    """Print a 2D grid in a readable format."""
    for row in grid:
        print(separator.join(str(cell) for cell in row))
