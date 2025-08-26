"""
Tests for utility functions used in Advent of Code solutions.
"""

import pytest
from pathlib import Path
from src.utils.input_reader import InputReader
from src.utils.common import (
    manhattan_distance,
    euclidean_distance,
    get_neighbors_4,
    bfs,
    dijkstra,
    lcm,
    lcm_list,
    mod_inverse,
    chinese_remainder_theorem,
    parse_int_grid,
    transpose_grid,
    rotate_grid_90_clockwise,
    rotate_grid_90_counterclockwise,
)


class TestInputReader:
    """Test the InputReader class."""

    def test_init_with_input_file(self, tmp_path):
        """Test initialization with a specific input file."""
        input_file = tmp_path / "test_input.txt"
        input_file.write_text("test\ninput")

        reader = InputReader(input_file=str(input_file))
        assert reader.file_path == input_file

    def test_init_with_year_day(self):
        """Test initialization with year and day."""
        reader = InputReader(year=2023, day=1)
        expected_path = Path(__file__).parent.parent / "inputs" / "2023" / "day_01.txt"
        assert reader.file_path == expected_path

    def test_init_validation(self):
        """Test that initialization requires proper parameters."""
        with pytest.raises(ValueError):
            InputReader()

        with pytest.raises(ValueError):
            InputReader(year=2023)

        with pytest.raises(ValueError):
            InputReader(day=1)

    def test_read_text(self, tmp_path):
        """Test reading input as text."""
        input_file = tmp_path / "test_input.txt"
        input_file.write_text("line1\nline2\n")

        reader = InputReader(input_file=str(input_file))
        assert reader.read_text() == "line1\nline2"

    def test_read_lines(self, tmp_path):
        """Test reading input as lines."""
        input_file = tmp_path / "test_input.txt"
        input_file.write_text("line1\n\nline2\n")

        reader = InputReader(input_file=str(input_file))
        lines = reader.read_lines()
        assert lines == ["line1", "line2"]

        lines_with_empty = reader.read_lines(strip_empty=False)
        assert lines_with_empty == ["line1", "", "line2"]

    def test_read_ints(self, tmp_path):
        """Test reading input as integers."""
        input_file = tmp_path / "test_input.txt"
        input_file.write_text("1\n2\n3\n")

        reader = InputReader(input_file=str(input_file))
        assert reader.read_ints() == [1, 2, 3]

    def test_read_ints_separated(self, tmp_path):
        """Test reading comma-separated integers."""
        input_file = tmp_path / "test_input.txt"
        input_file.write_text("1, 2, 3")

        reader = InputReader(input_file=str(input_file))
        assert reader.read_ints_separated() == [1, 2, 3]

    def test_read_grid(self, tmp_path):
        """Test reading input as a grid."""
        input_file = tmp_path / "test_input.txt"
        input_file.write_text("123\n456")

        reader = InputReader(input_file=str(input_file))
        grid = reader.read_grid()
        assert grid == [["1", "2", "3"], ["4", "5", "6"]]

    def test_read_blocks(self, tmp_path):
        """Test reading input as blocks."""
        input_file = tmp_path / "test_input.txt"
        input_file.write_text("block1\n\nblock2")

        reader = InputReader(input_file=str(input_file))
        blocks = reader.read_blocks()
        assert blocks == ["block1", "block2"]


class TestCommonUtils:
    """Test common utility functions."""

    def test_manhattan_distance(self):
        """Test Manhattan distance calculation."""
        assert manhattan_distance((0, 0), (3, 4)) == 7
        assert manhattan_distance((1, 1), (4, 5)) == 7
        assert manhattan_distance((0, 0), (0, 0)) == 0

    def test_euclidean_distance(self):
        """Test Euclidean distance calculation."""
        assert euclidean_distance((0, 0), (3, 4)) == 5.0
        assert euclidean_distance((1, 1), (4, 5)) == 5.0
        assert euclidean_distance((0, 0), (0, 0)) == 0.0

    def test_get_neighbors_4(self):
        """Test getting 4-directional neighbors."""
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        # Center position
        neighbors = get_neighbors_4((1, 1), grid)
        expected = [(0, 1), (1, 2), (2, 1), (1, 0)]
        assert set(neighbors) == set(expected)

        # Corner position
        neighbors = get_neighbors_4((0, 0), grid)
        expected = [(0, 1), (1, 0)]
        assert set(neighbors) == set(expected)

        # With diagonals
        neighbors = get_neighbors_4((1, 1), grid, include_diagonals=True)
        expected = [(0, 1), (1, 2), (2, 1), (1, 0), (0, 0), (0, 2), (2, 0), (2, 2)]
        assert set(neighbors) == set(expected)

    def test_bfs(self):
        """Test breadth-first search."""
        grid = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]

        # Simple path
        path = bfs((0, 0), (2, 3), grid, lambda pos: grid[pos[0]][pos[1]] == 1)
        assert path is not None
        assert len(path) == 6  # Shortest path length

        # No path (blocked)
        path = bfs((0, 0), (1, 1), grid, lambda pos: grid[pos[0]][pos[1]] == 1)
        assert path is None

    def test_dijkstra(self):
        """Test Dijkstra's algorithm."""
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        # Path with costs - the algorithm finds: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2)
        # Cost: 1 + 2 + 3 + 6 + 9 = 20
        result = dijkstra((0, 0), (2, 2), grid, lambda pos: grid[pos[0]][pos[1]])
        assert result is not None
        cost, path = result
        assert cost == 20  # 1 + 2 + 3 + 6 + 9 = 20

    def test_lcm(self):
        """Test least common multiple calculation."""
        assert lcm(12, 18) == 36
        assert lcm(7, 13) == 91
        assert lcm(0, 5) == 0

    def test_lcm_list(self):
        """Test LCM calculation for a list of numbers."""
        assert lcm_list([12, 18, 24]) == 72
        assert lcm_list([2, 3, 5, 7]) == 210

    def test_mod_inverse(self):
        """Test modular multiplicative inverse."""
        assert mod_inverse(3, 11) == 4  # 3 * 4 = 12 ≡ 1 (mod 11)
        assert mod_inverse(7, 13) == 2  # 7 * 2 = 14 ≡ 1 (mod 13)

        with pytest.raises(ValueError):
            mod_inverse(4, 8)  # GCD(4, 8) = 4 ≠ 1

    def test_chinese_remainder_theorem(self):
        """Test Chinese Remainder Theorem."""
        # x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7)
        remainders = [2, 3, 2]
        moduli = [3, 5, 7]
        result = chinese_remainder_theorem(remainders, moduli)
        assert result == 23

    def test_parse_int_grid(self):
        """Test parsing string grid to integer grid."""
        grid = [["1", "2", "3"], ["4", "5", "6"]]
        int_grid = parse_int_grid(grid)
        assert int_grid == [[1, 2, 3], [4, 5, 6]]

    def test_transpose_grid(self):
        """Test grid transposition."""
        grid = [[1, 2, 3], [4, 5, 6]]
        transposed = transpose_grid(grid)
        assert transposed == [(1, 4), (2, 5), (3, 6)]

    def test_rotate_grid_90_clockwise(self):
        """Test 90-degree clockwise rotation."""
        grid = [[1, 2, 3], [4, 5, 6]]
        rotated = rotate_grid_90_clockwise(grid)
        assert rotated == [(3, 6), (2, 5), (1, 4)]

    def test_rotate_grid_90_counterclockwise(self):
        """Test 90-degree counterclockwise rotation."""
        grid = [[1, 2, 3], [4, 5, 6]]
        rotated = rotate_grid_90_counterclockwise(grid)
        assert rotated == [(4, 1), (5, 2), (6, 3)]
