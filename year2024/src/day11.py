class Day11:
    def __init__(self, input):
        self.input = input

    def transform(self, stone):
        stone_str = str(stone)
        if stone == 0:
            return [1]
        elif len(stone_str) % 2 == 0:
            return [int(stone_str[:len(stone_str)//2]), int(stone_str[len(stone_str)//2:])]
        else:
            return [stone * 2024]

    def part1(self, num_runs = 25):
        input = list(map(int, self.input.split(" ")))
        num_map = {}
        for i in input:
            if i not in num_map:
                num_map[i] = 1
            else:
                num_map[i] += 1
        
        for _ in range(num_runs):
            new_map = {}
            for i in num_map:
                result = self.transform(i)
                for j in result:
                    if j not in new_map:
                        new_map[j] = num_map[i]
                    else:
                        new_map[j] += num_map[i]
            num_map = new_map
        return sum(new_map.values())
    
    def part2(self):
        return self.part1(75)