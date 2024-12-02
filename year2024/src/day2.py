class Day2:
    def __init__(self, input):
        self.input: str = input

    def is_safe(self, line):
        digits = list(map(int, line.split(" ")))
        increasing = False
        if digits[1] > digits[0]:
            increasing = True

        for i in range(1, len(digits)):
            diff = digits[i] - digits[i - 1]
            if increasing and (diff > 3 or diff <=0):
                return False
            if not increasing and (diff < -3 or diff >= 0):
                return False

        return True
    
    def is_really_safe(self, line):
        digits = list(map(int, line.split(" ")))
        if self.is_safe(line):
            return True
        for i in range(0, len(digits)):
            removed_digits = digits[:i] + digits[i + 1:]
            if self.is_safe(" ".join(str(d) for d in removed_digits)):
                return True
        return False

    def part1(self):
        reports = self.input.splitlines()
        return sum(1 for report in reports if self.is_safe(report))
    
    def part2(self):
        reports = self.input.splitlines()
        return sum(1 for report in reports if self.is_really_safe(report))
