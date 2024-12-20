class Day20:
    def __init__(self, input):
        self.input = input
        lines = input.splitlines()
        self.maze = [list(line) for line in lines]
        self.track = {}
        self.populate_maze()

    def find_start(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == "S":
                    return i, j
                
    def populate_maze(self):
        pos = self.find_start()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        while self.maze[pos[0]][pos[1]] != "E":
            self.track[pos] = i
            i += 1
            for dir in dirs:
                new_pos = (pos[0] + dir[0], pos[1] + dir[1])
                if new_pos not in self.track and self.maze[new_pos[0]][new_pos[1]] != "#":
                    pos = new_pos
                    break
        self.track[pos] = i
        

    def part1(self, diff = 100):
        dirs = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        total = 0
        for pos in self.track:
            for dir in dirs:
                new_pos = (pos[0] + dir[0], pos[1] + dir[1])
                if new_pos in self.track and self.track[new_pos] - self.track[pos] - 2 >= diff:
                    total += 1
        return total
    
    def part2(self, diff = 100):
        total = 0
        for pos in self.track:
            for pos2 in self.track:
                len_cheat = abs(pos[0] - pos2[0]) + abs(pos[1] - pos2[1])
                if 2 <= len_cheat <= 20:
                    if self.track[pos2] - self.track[pos] - len_cheat >= diff:
                        total += 1
        return total