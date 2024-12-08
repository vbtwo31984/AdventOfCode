import itertools


class Day8:
    def __init__(self, input):
        self.input = input
    
    def get_antennas(self):
        antennas = {}
        lines = self.input.splitlines()
        for i in range(len(lines)):
            line = lines[i]
            for j in range(len(line)):
                symbol = line[j]
                if(symbol != "."):
                    if(symbol not in antennas):
                        antennas[symbol] = []
                    antennas[symbol].append((i, j))
        return antennas
    
    def get_bounds(self):
        lines = self.input.splitlines()
        max_i = len(lines) - 1
        max_j = len(lines[0]) - 1
        return max_i, max_j

    def part1(self):
        max_i, max_j = self.get_bounds()
        antennas = self.get_antennas()
        antinodes = set()
        for antenna in antennas:
            pairs = list(itertools.combinations(antennas[antenna], 2))
            for pair in pairs:
                i1, j1 = pair[0]
                i2, j2 = pair[1]
                diff_i = abs(i1 - i2)
                diff_j = abs(j1 - j2)
                if i1 < i2:
                    new_i1 = i1 - diff_i
                    new_i2 = i2 + diff_i
                else:
                    new_i1 = i1 + diff_i
                    new_i2 = i2 - diff_i

                if j1 < j2:
                    new_j1 = j1 - diff_j
                    new_j2 = j2 + diff_j
                else:
                    new_j1 = j1 + diff_j
                    new_j2 = j2 - diff_j

                if new_i1 >= 0 and new_i1 <= max_i and new_j1 >= 0 and new_j1 <= max_j:
                    antinodes.add((new_i1, new_j1))
                if new_i2 >= 0 and new_i2 <= max_i and new_j2 >= 0 and new_j2 <= max_j:
                    antinodes.add((new_i2, new_j2))
        return len(antinodes)
    
    def part2(self):
        max_i, max_j = self.get_bounds()
        antennas = self.get_antennas()
        antinodes = set()
        for antenna in antennas:
            pairs = list(itertools.combinations(antennas[antenna], 2))
            for pair in pairs:
                i1, j1 = pair[0]
                i2, j2 = pair[1]
                diff_i = abs(i1 - i2)
                diff_j = abs(j1 - j2)

                if i1 < i2 and j1 < j2:
                    while(i1 >= 0 and j1 >= 0):
                        antinodes.add((i1, j1))
                        i1 -= diff_i
                        j1 -= diff_j
                    while(i2 <= max_i and j2 <= max_j):
                        antinodes.add((i2, j2))
                        i2 += diff_i
                        j2 += diff_j
                elif i1 < i2 and j1 > j2:
                    while(i1 >= 0 and j1 <= max_j):
                        antinodes.add((i1, j1))
                        i1 -= diff_i
                        j1 += diff_j
                    while(i2 <= max_i and j2 >= 0):
                        antinodes.add((i2, j2))
                        i2 += diff_i
                        j2 -= diff_j
                elif i1 > i2 and j1 < j2:
                    while(i1 <= max_i and j1 >= 0):
                        antinodes.add((i1, j1))
                        i1 += diff_i
                        j1 -= diff_j
                    while(i2 >= 0 and j2 <= max_j):
                        antinodes.add((i2, j2))
                        i2 -= diff_i
                        j2 += diff_j
                elif i1 > i2 and j1 > j2:
                    while(i1 <= max_i and j1 <= max_j):
                        antinodes.add((i1, j1))
                        i1 += diff_i
                        j1 += diff_j
                    while(i2 >= 0 and j2 >= 0):
                        antinodes.add((i2, j2))
                        i2 -= diff_i
                        j2 -= diff_j
        return len(antinodes)