class Day12:
    def __init__(self, input):
        self.input = input

    def get_input(self):
        return [list(line) for line in self.input.splitlines()]
    
    def get_area_perimeter(self, input, seen: set, x, y):
        area = 0
        perimeter = 0
        sides = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visit = [(x, y)]
        seen.add((x, y))
        while visit:
            x, y = visit.pop()
            area += 1
            plant = input[x][y]
            for dir in dirs:
                dx, dy = dir
                nx, ny = x + dx, y + dy
                nxs, nys = x + dx / 4, y + dy / 4
                if 0 <= nx < len(input) and 0 <= ny < len(input[0]) and (nx, ny) not in seen and input[nx][ny] == plant:
                    seen.add((nx, ny))
                    visit.append((nx, ny))
                elif nx < 0 or ny < 0 or nx >= len(input) or ny >= len(input[0]) or input[nx][ny] != plant:
                    perimeter += 1
                    sides.add((nxs, nys))

        num_sides = 0
        while len(sides) > 0:
            side = sides.pop()
            num_sides += 1
            if side[1] % 1 == 0: # horizontal
                dy = 1
                while (side[0], side[1] + dy) in sides:
                    sides.remove((side[0], side[1] + dy))
                    dy += 1
                dy = -1
                while (side[0], side[1] + dy) in sides:
                    sides.remove((side[0], side[1] + dy))
                    dy -= 1
            else: # vertical
                dx = 1
                while (side[0] + dx, side[1]) in sides:
                    sides.remove((side[0] + dx, side[1]))
                    dx += 1
                dx = -1
                while (side[0] + dx, side[1]) in sides:
                    sides.remove((side[0] + dx, side[1]))
                    dx -= 1
        return area, perimeter, num_sides

    def part1(self):
        input = self.get_input()
        seen = set()
        price = 0
        for x in range(len(input)):
            for y in range(len(input[0])):
                if (x, y) not in seen:
                    a, p, s = self.get_area_perimeter(input, seen, x, y)
                    price += a * p
        return price
    
    def part2(self):
        input = self.get_input()
        seen = set()
        price = 0
        for x in range(len(input)):
            for y in range(len(input[0])):
                if (x, y) not in seen:
                    a, p, s = self.get_area_perimeter(input, seen, x, y)
                    price += a * s
        return price