class Day1:
    def __init__(self, input):
        self.input = input

    def get_lists(self):
        lines = self.input.splitlines()
        lines = [list(map(int, line.split('   '))) for line in lines]
        firsts = [line[0] for line in lines]
        seconds = [line[1] for line in lines]
        return firsts,seconds

    def part1(self):
        firsts, seconds = self.get_lists()
        firsts.sort()
        seconds.sort()

        total_diff = 0
        for (first, second) in zip(firsts, seconds):
            total_diff += abs(first - second)
        return total_diff
    
    def part2(self):
        firsts, seconds = self.get_lists()
        num = sum(map(lambda n: seconds.count(n) * n, firsts))
        return num