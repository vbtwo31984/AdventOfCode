import re
class Day3:
    def __init__(self, input):
        self.input = input

    def part1(self):
        pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
        matches = re.findall(pattern, self.input, re.DOTALL)
        total = sum(int(match[0]) * int(match[1]) for match in matches)
        return total
    
    def part2(self):
        do_dont_pattern = r"don\'t\(\).*?do\(\)"
        self.input = re.sub(do_dont_pattern, "", self.input, flags=re.DOTALL)
        return self.part1()