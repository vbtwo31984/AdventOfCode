from heapq import heappush, heappop

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Day16:
    def __init__(self, input):
        self.input = input
        self.heap = []
        self.visited = {}

    def get_input(self):
        lines = self.input.splitlines()
        return [list(line) for line in lines]
    
    def check(self, maze, loc, d, points):
        i, j = loc[1][0], loc[1][1]
        di, dj = dirs[d]
        ni, nj = i + di, j + dj

        if maze[ni][nj] != "#":
            nloc = (ni, nj, d)
            np = loc[0] + points
            if nloc not in self.visited or np < self.visited[nloc]:
                self.visited[nloc] = np
                heappush(self.heap, (np, nloc))

    def part1(self):
        maze = self.get_input()
        c = (len(maze) - 2, 1)
        loc = (c[0], c[1], 0)
        heappush(self.heap, (0, loc))
        self.visited[loc] = 0

        while self.heap:
            cost, (i, j, d) = heappop(self.heap)
            if maze[i][j] == "E":
                return cost
            
            # Try moving forward
            self.check(maze, (cost, (i, j, d)), d, 1)
        
            # Try turning left and right
            self.check(maze, (cost, (i, j, d)), (d + 1) % 4, 1001)
            self.check(maze, (cost, (i, j, d)), (d - 1) % 4, 1001)
    
    def part2(self):
        return 0