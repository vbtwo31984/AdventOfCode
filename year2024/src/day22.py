from collections import defaultdict
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
    
    def get_prices(self):
        prices = []
        for line in self.input.splitlines():
            buyer_prices = []
            secret = int(line)
            for _ in range(2000):
                price = int(str(secret)[-1])
                buyer_prices.append(price)
                secret = self.get_next_secret(secret)
            prices.append(buyer_prices)
        return prices
    
    def get_changes(self, prices):
        changes = []
        for i in range(len(prices)):
            change = []
            for j in range(1, len(prices[i])):
                change.append(prices[i][j] - prices[i][j-1])
            changes.append(change)
        return changes
    
    def get_sequence_counts(self, prices, change):
        counts = {}
        for i in range(4, len(change)):
            sequence = tuple(change[i-4:i])
            if sequence not in counts:
                counts[sequence] = prices[i]
        return counts
    
    def get_all_sequence_counts(self, prices, changes):
        all_counts = []
        for i in range(len(changes)):
            counts = self.get_sequence_counts(prices[i], changes[i])
            all_counts.append(counts)
        return all_counts
    
    def find_max(self, all_counts):
        max_counts = defaultdict(int)
        for counts in all_counts:
            for key in counts:
                max_counts[key] = max_counts[key] + counts[key]
        return max(max_counts.values())
    
    def part2(self):
        prices = self.get_prices()
        changes = self.get_changes(prices)
        counts = self.get_all_sequence_counts(prices, changes)
        max = self.find_max(counts)
        return max