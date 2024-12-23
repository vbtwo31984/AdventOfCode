import functools


class Day22:
    def __init__(self, input):
        self.input = input

    def mix(self, secret, num):
        return secret ^ num 
    
    def prune(self, secret):
        return secret % 16777216
    
    def get_next_secret(self, secret):
        result = secret * 64
        secret = self.mix(secret, result)
        secret = self.prune(secret)

        result = secret // 32
        secret = self.mix(secret, result)
        secret = self.prune(secret)

        result = secret * 2048
        secret = self.mix(secret, result)
        secret = self.prune(secret)

        return secret
    
    def part1(self):
        sum = 0
        lines = self.input.splitlines()
        for line in lines:
            secret = int(line)
            for _ in range(2000):
                secret = self.get_next_secret(secret)
            sum += secret
        return sum
    
    def part2(self):
        return 0