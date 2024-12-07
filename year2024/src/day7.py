class Day7:
    def __init__(self, input):
        self.input = input

    def get_input(self):
        nums = {}
        lines = self.input.splitlines()
        for line in lines:
            line = line.split(": ")
            total = int(line[0])
            numbers = list(map(int, line[1].split(" ")))
            nums[total] = numbers
        return nums
    
    def is_valid(self, total, numbers, allow_concat = False):
        if numbers[0] >= total:
            return False
        sum = numbers[0] + numbers[1]
        product = numbers[0] * numbers[1]
        concat = int(str(numbers[0]) + str(numbers[1]))

        if len(numbers) == 2:
            return sum == total or product == total or (allow_concat and concat == total)

        sum_numbers = [sum] + numbers[2:]
        product_numbers = [product] + numbers[2:]

        if not allow_concat:
            return self.is_valid(total, sum_numbers, allow_concat) \
                or self.is_valid(total, product_numbers, allow_concat)
        concat_numbers = [concat] + numbers[2:]
        return self.is_valid(total, sum_numbers, allow_concat) \
            or self.is_valid(total, product_numbers, allow_concat) \
            or self.is_valid(total, concat_numbers, allow_concat)

    def part1(self):
        input = self.get_input()
        total = sum(total for total in input if self.is_valid(total, input[total]))
        return total
    
    def part2(self):
        input = self.get_input()
        total = sum(total for total in input if self.is_valid(total, input[total], True))
        return total