import sys
import importlib
sys.path.insert(0, 'year2024')

day = 1

module_name = f"src.day{day}"
module = importlib.import_module(module_name)
day_class = getattr(module, f"Day{day}")

with open(f"year2024/input/day{day}.txt") as f:
    input = f.read()

day_instance = day_class(input)
print("Part 1: ", day_instance.part1())
print("Part 2: ", day_instance.part2())