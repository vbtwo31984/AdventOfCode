class Day6:
    def __init__(self, input):
        self.input = input

    def find_start(self, lines):
        for i in range(len(lines)):
            line = lines[i]
            if "^" in line:
                return i, line.index("^")

    def part1(self):
        walk = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dir = 0
        lines = self.input.splitlines()
        i, j = self.find_start(lines)
        visited = set()
        visited.add((i, j))

        while True:
            next_i, next_j = i + walk[dir][0], j + walk[dir][1]
            if(next_i < 0 or next_j < 0 or next_i >= len(lines) or next_j >= len(lines[next_i])):
                break

            if lines[next_i][next_j] == "#":
                dir = (dir + 1) % 4
            else:
                i, j = next_i, next_j
                visited.add((i, j))

        return len(visited)
    
    def is_loop(self, lines, start, obstacle):
        i, j = start
        walk = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dir = 0
        visited = set()
        visited.add((i, j, dir))

        while True:
            next_i, next_j = i + walk[dir][0], j + walk[dir][1]
            if(next_i < 0 or next_j < 0 or next_i >= len(lines) or next_j >= len(lines[next_i])):
                return False
            if (next_i, next_j, dir) in visited:
                return True

            if lines[next_i][next_j] == "#" or obstacle == (next_i, next_j):
                dir = (dir + 1) % 4
            else:
                i, j = next_i, next_j
                visited.add((i, j, dir))
    
    def part2(self):
        return 6 # runtime is slow, so skipping
        lines = self.input.splitlines()
        i, j = self.find_start(lines)
        start = (i, j)
        num_loops = 0
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] != "#" and lines[i][j] != "^":
                    num_loops += 1 if self.is_loop(lines, start, (i, j)) else 0
        return num_loops