"""
Input reader utility for Advent of Code puzzles.
Provides common functionality for reading and parsing input files.
"""

import os
from pathlib import Path
from typing import List, Optional, Union


class InputReader:
    """Utility class for reading and parsing Advent of Code input files."""

    def __init__(
        self,
        input_file: Optional[str] = None,
        year: Optional[int] = None,
        day: Optional[int] = None,
    ):
        """
        Initialize the input reader.

        Args:
            input_file: Path to a specific input file
            year: Year for the puzzle (e.g., 2023)
            day: Day for the puzzle (e.g., 1)
        """
        self.input_file = input_file
        self.year = year
        self.day = day

        if input_file:
            self.file_path = Path(input_file)
        elif year and day:
            self.file_path = self._get_default_input_path(year, day)
        else:
            raise ValueError("Either input_file or both year and day must be provided")

    def _get_default_input_path(self, year: int, day: int) -> Path:
        """Get the default input file path for a given year and day."""
        project_root = Path(__file__).parent.parent.parent
        return project_root / "inputs" / str(year) / f"day_{day:02d}.txt"

    def read_text(self) -> str:
        """Read the entire input file as a single string."""
        if not self.file_path.exists():
            raise FileNotFoundError(f"Input file not found: {self.file_path}")

        with open(self.file_path, "r", encoding="utf-8") as f:
            return f.read().rstrip("\n")

    def read_lines(self, strip_empty: bool = True) -> List[str]:
        """
        Read the input file as a list of lines.

        Args:
            strip_empty: Whether to remove empty lines from the result

        Returns:
            List of lines from the input file
        """
        text = self.read_text()
        lines = text.split("\n")

        if strip_empty:
            lines = [line for line in lines if line.strip()]

        return lines

    def read_ints(self) -> List[int]:
        """Read the input file and convert each line to an integer."""
        lines = self.read_lines()
        return [int(line) for line in lines]

    def read_ints_separated(self, separator: str = ",") -> List[int]:
        """
        Read a single line and split by separator, converting to integers.

        Args:
            separator: Character to split the line by

        Returns:
            List of integers from the input
        """
        text = self.read_text()
        return [int(x.strip()) for x in text.split(separator)]

    def read_grid(self, delimiter: str = "") -> List[List[str]]:
        """
        Read the input as a 2D grid.

        Args:
            delimiter: Character to split each line by (empty string = character by character)

        Returns:
            2D list representing the grid
        """
        lines = self.read_lines(strip_empty=False)
        if delimiter == "":
            return [list(line) for line in lines]
        else:
            return [line.split(delimiter) for line in lines]

    def read_blocks(self, separator: str = "\n\n") -> List[str]:
        """
        Read the input file as blocks separated by a specific separator.

        Args:
            separator: String that separates blocks

        Returns:
            List of blocks
        """
        text = self.read_text()
        return text.split(separator)

    def read_blocks_as_lines(self, separator: str = "\n\n") -> List[List[str]]:
        """
        Read the input file as blocks, where each block is a list of lines.

        Args:
            separator: String that separates blocks

        Returns:
            List of blocks, where each block is a list of lines
        """
        blocks = self.read_blocks(separator)
        return [block.split("\n") for block in blocks]
