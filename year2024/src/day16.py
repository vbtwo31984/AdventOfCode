from heapq import heappush, heappop

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Day16:
    def __init__(self, input):
        self.input = input

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
        self.heap = []
        self.visited = {}
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
    

    
    def check_with_path(self, maze, loc, d, points, path):
        i, j = loc[1][0], loc[1][1]
        di, dj = dirs[d]
        ni, nj = i + di, j + dj

        if maze[ni][nj] != "#":
            nloc = (ni, nj, d)
            np = loc[0] + points
            if nloc not in self.visited or np <= self.visited[nloc]:
                self.visited[nloc] = np

                path = path.copy()
                path.append((ni, nj))
                heappush(self.heap, (np, nloc, path))

    def print_maze(self, maze, path):
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if (i, j) in path:
                    print("O", end="")
                else:
                    print(maze[i][j], end="")
            print()

    def part2(self):
        self.heap = []
        self.visited = {}

        maze = self.get_input()
        c = (len(maze) - 2, 1)
        loc = (c[0], c[1], 0)
        path = [(loc[0], loc[1])]
        heappush(self.heap, (0, loc, path))
        min_cost = -1

        all_paths = set()

        while self.heap:
            cost, (i, j, d), path = heappop(self.heap)
            if cost > min_cost and min_cost != -1:
                break

            if maze[i][j] == "E":
                if min_cost == -1 or cost <= min_cost:
                    min_cost = cost
                    for p in path:
                        all_paths.add(p)
            
            # Try moving forward
            self.check_with_path(maze, (cost, (i, j, d)), d, 1, path)
        
            # Try turning left and right
            self.check_with_path(maze, (cost, (i, j, d)), (d + 1) % 4, 1001, path)
            self.check_with_path(maze, (cost, (i, j, d)), (d - 1) % 4, 1001, path)
        return len(all_paths)