.PHONY: help setup test test-cov format lint clean

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup:  ## Set up the development environment
	uv venv
	@echo "Virtual environment created. Activate it with:"
	@echo "  source .venv/bin/activate  # On macOS/Linux"
	@echo "  .venv\\Scripts\\activate     # On Windows"
	uv pip install -e .

test:  ## Run tests
	uv run pytest

test-cov:  ## Run tests with coverage
	uv run pytest --cov=src --cov-report=html

format:  ## Format code with black
	uv run black src/ tests/

lint:  ## Lint code with flake8
	uv run flake8 src/ tests/

check: format lint test  ## Run format, lint, and test

clean:  ## Clean up generated files
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

run:  ## Run a specific day (usage: make run YEAR=2023 DAY=1)
	@if [ -z "$(YEAR)" ] || [ -z "$(DAY)" ]; then \
		echo "Usage: make run YEAR=2023 DAY=1"; \
		exit 1; \
	fi
	uv run python run.py --year $(YEAR) --day $(DAY)

create-day:  ## Create a new day (usage: make create-day YEAR=2024 DAY=3)
	@if [ -z "$(YEAR)" ] || [ -z "$(DAY)" ]; then \
		echo "Usage: make create-day YEAR=2024 DAY=3"; \
		exit 1; \
	fi
	uv run python create_day.py --year $(YEAR) --day $(DAY)
