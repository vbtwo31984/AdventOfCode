class Day4:
    def __init__(self, input):
        self.input = input

    def has_word(self, i, j, lines, possibility):
        word_to_find = "MAS"
        for letter in range(3):
            if possibility[letter][0] < 0 or possibility[letter][1] < 0 or possibility[letter][0] >= len(lines) or possibility[letter][1] >= len(lines[i]):
                return False
            if lines[possibility[letter][0]][possibility[letter][1]] != word_to_find[letter]:
                return False
        return True

    def find_xmax(self, i, j, lines):
        found = 0
        possibilities = [
            [(i-1,j-1), (i-2,j-2), (i-3,j-3)],
            [(i-1, j+1), (i-2, j+2), (i-3, j+3)],
            [(i+1, j-1), (i+2, j-2), (i+3, j-3)],
            [(i+1, j+1), (i+2, j+2), (i+3, j+3)],
            [(i-1, j), (i-2, j), (i-3, j)],
            [(i+1, j), (i+2, j), (i+3, j)],
            [(i, j-1), (i, j-2), (i, j-3)],
            [(i, j+1), (i, j+2), (i, j+3)]
        ]
        word_to_find = "MAS"
        return sum(1 for possibility in possibilities if self.has_word(i, j, lines, possibility))

    def part1(self):
        lines = self.input.splitlines()
        found = 0
        for i in range(len(lines)):
            line = lines[i]
            for j in range(len(lines)):
                if(line[j] == "X"):
                    num_found = self.find_xmax(i, j, lines)
                    found += num_found
        return found
    
    def find_mas(self, i, j, lines):
        if i < 1 or j < 1 or i >= len(lines) - 1 or j >= len(lines[i]) - 1:
            return False
        top_left = lines[i-1][j-1]
        top_right = lines[i-1][j+1]
        bottom_left = lines[i+1][j-1]
        bottom_right = lines[i+1][j+1]

        num_found = 0
        if top_left == "M" and bottom_right == "S":
            num_found += 1
        if top_right == "M" and bottom_left == "S":
            num_found += 1
        if bottom_left == "M" and top_right == "S":
            num_found += 1
        if bottom_right == "M" and top_left == "S":
            num_found += 1
        return num_found == 2

    def part2(self):
        lines = self.input.splitlines()
        found = 0
        for i in range(len(lines)):
            line = lines[i]
            for j in range(len(lines)):
                if(line[j] == "A"):
                    num_found = self.find_mas(i, j, lines)
                    found += num_found
        return found