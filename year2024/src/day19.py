class Day19:
    def __init__(self, input):
        self.input = input
        lines = input.splitlines()
        self.patterns = sorted(lines[0].split(", "), reverse=True, key=lambda l: len(l))
        self.designs = lines[2:]
        self.checked = {}

    def is_valid(self, design):
        return self.num_valid(design) > 0
    
    def num_valid(self, design):
        if design in self.checked:
            return self.checked[design]
        if len(design) == 0:
            return 1
        num = 0
        for pattern in self.patterns:
            if design.startswith(pattern):
                num += self.num_valid(design[len(pattern):])
        self.checked[design] = num
        return num

    def part1(self):
        num_valid = sum(1 for design in self.designs if self.is_valid(design))
        return num_valid
    
    def part2(self):
        num = sum(self.num_valid(design) for design in self.designs)
        return num