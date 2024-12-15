import time
moves_map = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

class Day15:
    def __init__(self, input):
        self.input = input

    def get_input(self):
        parts = self.input.split("\n\n")
        grid = list(map(list, parts[0].splitlines()))
        moves = "".join(parts[1].splitlines())
        return grid, moves
    
    def find_robot(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "@":
                    return i, j
                
    def find_empty(self, grid, i, j, di, dj):
        while grid[i][j] == "O":
            i += di
            j += dj

        if grid[i][j] == ".":
            return i, j
        else:
            return None
        
    def calculate_score(self, grid):
        score = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O" or grid[i][j] == "[":
                    score += 100 * i + j
        return score
    
    def print_grid(self, grid):
        print()
        for i in range(len(grid)):
            print("".join(grid[i]))

    def part1(self):
        grid, moves = self.get_input()
        i, j = self.find_robot(grid)
        for move in moves:
            di, dj = moves_map[move]
            ni = i + di
            nj = j + dj
            if grid[ni][nj] == ".":
                grid[ni][nj] = "@"
                grid[i][j] = "."
                i, j = ni, nj
            elif grid[ni][nj] == "#":
                continue
            elif grid[ni][nj] == "O":
                res = self.find_empty(grid, ni, nj, di, dj)
                if res is not None:
                    ei, ej = res
                    grid[ei][ej] = "O"
                    grid[ni][nj] = "@"
                    grid[i][j] = "."
                    i, j = ni, nj
        return self.calculate_score(grid)
    
    def get_double_input(self):
        grid, moves = self.get_input()
        double_grid = []
        for i in range(len(grid)):
            line = []
            for j in range(len(grid[0])):
                if grid[i][j] == "@":
                    line.append("@")
                    line.append(".")
                elif grid[i][j] == "O":
                    line.append("[")
                    line.append("]")
                else:
                    line.append(grid[i][j])
                    line.append(grid[i][j])
            double_grid.append(line)
        return double_grid, moves

    def move_horizontally(self, grid, i, j, dj):
        oj = j
        while grid[i][j] == "[" or grid[i][j] == "]":
            j += dj

        if grid[i][j] == ".":
            while j != oj:
                pj = j - dj
                grid[i][j] = grid[i][pj]
                j -= dj
            grid[i][oj] = "@"
            grid[i][oj - dj] = "."
            return i, j
        return i, oj - dj
    
    def move_vertically(self, grid, i, j, di):
        oi, oj = i, j
        width = {i: (j, j)}

        while True:
            pi = i
            i += di
            # any "#"
            if grid[i][width[pi][0]:width[pi][1] + 1].count("#") > 0:
                break
            # all "."
            if grid[i][width[pi][0]:width[pi][1] + 1].count(".") == width[pi][1] - width[pi][0] + 1:
                # move everything
                width[i] = (width[pi][0], width[pi][1])
                while i != oi:
                    pi = i - di
                    for j in range(width[pi][0], width[pi][1] + 1):
                        grid[i][j] = grid[pi][j]
                    if width[pi][0] > width[i][0]:
                        grid[i][width[i][0]] = "."
                    if width[pi][1] < width[i][1]:
                        grid[i][width[i][1]] = "."
                    i -= di

                grid[oi][oj] = "."
                return oi + di, oj
            else:
                # see if width needs updating
                dw1 = 0
                dw2 = 0
                if grid[i][width[pi][0]] == "]":
                    dw1 = -1
                if grid[i][width[pi][1]] == "[":
                    dw2 = 1
                if grid[i][width[pi][0]] == ".":
                    dw1 = 1
                if grid[i][width[pi][1]] == ".":
                    dw2 = -1
                width[i] = (width[pi][0] + dw1, width[pi][1] + dw2)
        
        return oi, j

    def part2(self):
        grid, moves = self.get_double_input()
        i, j = self.find_robot(grid)
        # self.print_grid(grid)
        for move in moves:
            di, dj = moves_map[move]
            ni = i + di
            nj = j + dj
            if grid[ni][nj] == ".":
                grid[ni][nj] = "@"
                grid[i][j] = "."
                i, j = ni, nj
            elif grid[ni][nj] == "#":
                continue
            elif grid[ni][nj] == "[" or grid[ni][nj] == "]":
                if di == 0:
                    i, j = self.move_horizontally(grid, ni, nj, dj)
                else:
                    i, j = self.move_vertically(grid, i, nj, di)
            # print(move)

            # time.sleep(0.3)

            # self.print_grid(grid)
        # self.print_grid(grid)
        return self.calculate_score(grid)
