# Advent of Code Solutions

This repository contains my solutions to Advent of Code puzzles organized by year and day.

## 🚀 Quick Start

```bash
# Set up the project
make setup

# Activate virtual environment
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows

# Run a solution
make run YEAR=2023 DAY=1

# Run tests
make test

# Create a new day
make create-day YEAR=2024 DAY=4
```

## Setup

1. Install `uv` (if not already installed):
   ```bash
   # On macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # On Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Or with pip
   pip install uv
   ```

2. Set up the development environment:
   ```bash
   make setup
   ```

3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

2. Create input files in the `inputs/` directory following the naming convention:
   - `inputs/YYYY/day_DD.txt` (e.g., `inputs/2023/day_01.txt`)

## Usage

### Running Solutions

Run a specific day's solution:
```bash
python run.py --year 2023 --day 1
```

Run with a specific input file:
```bash
python run.py --year 2023 --day 1 --input custom_input.txt
```

### Running Tests

Run all tests:
```bash
pytest
```

Run tests for a specific year:
```bash
pytest tests/test_year_2023.py
```

Run tests with coverage:
```bash
pytest --cov=src
```

## Solution Template

Each day's solution should follow this structure:

```python
from src.utils.input_reader import InputReader

class Day01:
    def __init__(self, input_file: str = None):
        self.input_reader = InputReader(input_file)
        self.data = self.input_reader.read_lines()
    
    def solve_part1(self) -> int:
        # Your solution for part 1
        pass
    
    def solve_part2(self) -> int:
        # Your solution for part 2
        pass

if __name__ == "__main__":
    day = Day01()
    print(f"Part 1: {day.solve_part1()}")
    print(f"Part 2: {day.solve_part2()}")
```

## Testing

Each solution should have corresponding test cases in the `tests/` directory. Tests should use the sample input provided in the puzzle description to verify correctness.

## Code Quality

- Use `black` for code formatting: `uv run black src/ tests/`
- Use `flake8` for linting: `uv run flake8 src/ tests/`
- Write comprehensive tests for all solutions
- Follow PEP 8 style guidelines

## Development with uv

```bash
# Format code
uv run black src/ tests/

# Lint code
uv run flake8 src/ tests/

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src

# Install new dependencies
uv add package-name

# Install dev dependencies
uv add --dev package-name
```
