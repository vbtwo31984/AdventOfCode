import re

class Day14:
    def __init__(self, input, ax = 101, ay = 103):
        self.input = input
        self.ax = ax
        self.ay = ay

    def get_input(self):
        r = r"-?[0-9]+"
        lines = self.input.splitlines()
        return [list(map(int, re.findall(r, line))) for line in lines]
    
    def get_position(self, init, move, num_moves):
        x, y = init
        dx, dy = move[0] * num_moves, move[1] * num_moves
        return ((x + dx) % self.ax, (y + dy) % self.ay)

    def part1(self):
        mx = self.ax // 2
        my = self.ay // 2

        robots = self.get_input()
        positions = [self.get_position((robot[0],robot[1]), (robot[2], robot[3]), 100) for robot in robots]
        quadrants = [0, 0, 0, 0]
        for position in positions:
            if position[0] < mx and position[1] < my:
                quadrants[0] += 1
            elif position[0] < mx and position[1] > my:
                quadrants[1] += 1
            elif position[0] > mx and position[1] < my:
                quadrants[2] += 1
            elif position[0] > mx and position[1] > my:
                quadrants[3] += 1

        return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    

    def count_adjacent_positions(self, positions):
        adjacent_count = 0
        for position in positions:
            x, y = position
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (x + dx, y + dy) in positions:
                    adjacent_count += 1
                    break  # no need to check other directions if one is adjacent
        return adjacent_count
    
    def print_matrix(self, positions):
        for y in range(self.ay):
            for x in range(self.ax):
                if (x, y) in positions:
                    print("#", end="")
                else:
                    print(".", end="")
            print()

    def part2(self):
        robots = self.get_input()
        max_adjacent_count = 0
        max_i = 0
        for i in range(1, 10000):
            positions = set([self.get_position((robot[0],robot[1]), (robot[2], robot[3]), i) for robot in robots])
            adjacent_count = self.count_adjacent_positions(positions)
            if adjacent_count > max_adjacent_count:
                max_adjacent_count = adjacent_count
                max_i = i
            # if i == 8179:
            #     self.print_matrix(positions)
        return max_i