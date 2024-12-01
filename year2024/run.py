import sys
import importlib
sys.path.insert(0, 'year2024')

print("Year 2024   Part 1     Part 2 |             Part 1     Part 2 |             Part 1     Part 2 |             Part 1     Part 2 |             Part 1     Part 2")
for day in range(1, 26):
    print(f"Day {day:2}: ", end="")

    module_name = f"src.day{day}"
    module = importlib.import_module(module_name)
    day_class = getattr(module, f"Day{day}")

    with open(f"year2024/input/day{day}.txt") as f:
        input = f.read()

    day_instance = day_class(input)
    print(f"{day_instance.part1():10} {day_instance.part2():10} ", end="")

    if day % 5 == 0:
        print()
    else:
        print("| ", end="")
