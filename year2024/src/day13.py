import re

class Day13:
    def __init__(self, input):
        self.input = input

    def get_input(self):
        games = self.input.split("\n\n")
        input = []
        for game in games:
            a_reg = r"A: X\+([0-9]+), Y\+([0-9]+)"
            a_match = re.search(a_reg, game, re.MULTILINE)
            a = ([int(a_match.group(1)), int(a_match.group(2))])

            b_reg = r"B: X\+([0-9]+), Y\+([0-9]+)"
            b_match = re.search(b_reg, game, re.MULTILINE)
            b = ([int(b_match.group(1)), int(b_match.group(2))])

            prize_reg = r"Prize: X=([0-9]+), Y=([0-9]+)"
            prize_match = re.search(prize_reg, game, re.MULTILINE)
            prize = ([int(prize_match.group(1)), int(prize_match.group(2))])

            input.append({"a": a, "b": b, "prize": prize})
        return input
    
    def calculate_score(self, num_a, num_b):
        return num_a*3 + num_b

    def get_score(self, game):
        a, b, prize = game["a"], game["b"], game["prize"]
        score = 0

        a1, a2 = a
        b1, b2 = b
        n1, n2 = prize

        nb1 = b1 * a2
        nn1 = n1 * a2

        nb2 = b2 * a1
        nn2 = n2 * a1

        b3 = nb1 - nb2
        n3 = nn1 - nn2

        y = n3 / b3
        x = (n1 - b1 * y) / a1


        if x.is_integer() and y.is_integer():
            score += self.calculate_score(x, y)

        return int(score)

    def part1(self):
        games = self.get_input()
        total = sum(self.get_score(game) for game in games)
        return total
    
    def part2(self):
        games = self.get_input()
        for game in games:
            game["prize"] = (game["prize"][0] + 10000000000000, game["prize"][1] + 10000000000000)
        total = sum(self.get_score(game) for game in games)
        return total