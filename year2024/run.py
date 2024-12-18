import sys
import importlib
import time
sys.path.insert(0, 'year2024')

print("Year 2024:         Part 1      Time  |           Part 2      Time")
for day in range(1, 26):
    print(f"Day {day:2}: ", end="")

    module_name = f"src.day{day}"
    module = importlib.import_module(module_name)
    day_class = getattr(module, f"Day{day}")

    with open(f"year2024/input/day{day}.txt") as f:
        input = f.read()

    day_instance = day_class(input)

    start_1 = time.time()
    part1 = day_instance.part1()
    end_1 = time.time()
    time_1 = end_1 - start_1
    print(f"{part1:17}  {time_1:8.5f}", end="")

    start_2 = time.time()
    part2 = day_instance.part2()
    end_2 = time.time()
    time_2 = end_2 - start_2
    print(f"  |  {part2:15}  {time_2:8.5f}")
