class Day25:
    def __init__(self, input):
        parts = input.split("\n\n")
        locks = []
        keys = []
        for part in parts:
            lines = part.splitlines()
            if lines[0].startswith("#"):
                locks.append(self.get_part(lines))
            else:
                lines.reverse()
                keys.append(self.get_part(lines))
        self.locks = locks
        self.keys = keys


    def get_part(self, lines):
        key = [0, 0, 0, 0, 0]
        for i in range(1, len(lines)):
            line = lines[i]
            for j in range(len(line)):
                if line[j] == "." and lines[i-1][j] == "#":
                    key[j] = i - 1
        return key

    def is_pair(self, lock, key):
        for i in range(len(lock)):
            if lock[i] + key[i] > 5:
                return False
        return True

    def part1(self):
        pairs = 0
        for lock in self.locks:
            for key in self.keys:
                if self.is_pair(lock, key):
                    pairs += 1
        return pairs
    
    def part2(self):
        return 0