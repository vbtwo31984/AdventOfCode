class Day10:
    def __init__(self, input):
        self.input = input

    def get_input(self):
        lines = self.input.splitlines()
        input = [list(map(int, list(line))) for line in lines]
        return input
    
    def score(self, input, x, y, depth):
        score = set()
        if depth == 9:
            score.add((x,y))
            return score
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dir in dirs:
            dx, dy = dir
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(input) and 0 <= ny < len(input[0]) and input[nx][ny] == depth + 1:
                score = score.union(self.score(input, nx, ny, depth + 1))
        return score
    
    def score2(self, input, x, y, depth):
        if depth == 9:
            return 1
        
        score = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dir in dirs:
            dx, dy = dir
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(input) and 0 <= ny < len(input[0]) and input[nx][ny] == depth + 1:
                score += self.score2(input, nx, ny, depth + 1)
        return score

    def part1(self):
        input = self.get_input()
        total = 0
        for x in range(len(input)):
            for y in range(len(input[x])):
                if input[x][y] == 0:
                    scoreset = self.score(input, x, y, 0)
                    total += len(scoreset)
        return total
    
    def part2(self):
        input = self.get_input()
        total = 0
        for x in range(len(input)):
            for y in range(len(input[x])):
                if input[x][y] == 0:
                    total += self.score2(input, x, y, 0)
        return total