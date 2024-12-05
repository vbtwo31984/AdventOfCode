import functools

class Day5:
    def __init__(self, input):
        self.input = input

    def get_input(self):
        split = self.input.split("\n\n")
        rules = split[0].splitlines()
        rules = [rule.split("|") for rule in rules]

        before = {}
        after = {}
        for rule in rules:
            if rule[0] not in after:
                after[rule[0]] = []
            if rule[0] not in before:
                before[rule[0]] = []
            if rule[1] not in after:
                after[rule[1]] = []
            if rule[1] not in before:
                before[rule[1]] = []
            before[rule[1]].append(rule[0])
            after[rule[0]].append(rule[1])

        updates = split[1].splitlines()
        updates = [update.split(",") for update in updates]

        rules = {"before": before, "after": after}
        return rules, updates
    
    def sort_update(self, rules, update):
        key_func = functools.cmp_to_key(lambda x, y: -1 if y in rules["after"][x] else -1 if x in rules["before"][y] else 0)

        sorted_nums = sorted(update, key=key_func)
        return sorted_nums
    
    def is_valid(self, rules, update):
        seen = set()
        for u in update:
            for v in rules["after"][u]:
                if v in seen:
                    return False
            seen.add(u)
        return True
    
    def get_middle(self, update):
        length = len(update)
        return int(update[length // 2])

    def part1(self):
        rules, updates = self.get_input()
        total = sum(self.get_middle(update) if self.is_valid(rules, update) else 0 for update in updates)
        return total
    
    def part2(self):
        rules, updates = self.get_input()
        total = sum(self.get_middle(self.sort_update(rules,update)) if not self.is_valid(rules, update) else 0 for update in updates)
        return total