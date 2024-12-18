class Day18:
    def __init__(self, input, size = 71):
        self.input = input
        self.size = size
        self.bytes = self.get_bytes()

    def get_bytes(self):
        lines = self.input.splitlines()
        return [tuple(map(int, line.split(","))) for line in lines]

    def part1(self, num_bytes = 1024):
        obstacles = set(self.bytes[0:num_bytes])
        pos = (0, 0)
        score = {pos: 0}
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        to_visit = [pos]
        while to_visit:
            pos = to_visit.pop()
            for dir in dirs:
                new_pos = (pos[0] + dir[0], pos[1] + dir[1])
                if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= self.size or new_pos[1] >= self.size:
                    continue
                if new_pos in obstacles:
                    continue
                if new_pos in score and score[new_pos] <= score[pos] + 1:
                    continue
                score[new_pos] = score[pos] + 1
                to_visit.append(new_pos)

        return score[(self.size - 1, self.size - 1)]
    
    def find_error(self, start, end):
        mid = (start + end) // 2
        try:
            self.part1(mid)
            if start == mid:
                return start + 1
            return self.find_error(mid, end)
        except KeyError:
            if start == mid:
                return start
            return self.find_error(start, mid)

    def part2(self, start_bytes = 1025):
        start = start_bytes
        end = len(self.bytes)
        i = self.find_error(start, end)
        return ",".join(map(str, self.bytes[i-1]))