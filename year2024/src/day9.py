class Day9:
    def __init__(self, input):
        self.input = input

    def is_space(self, index):
        return index % 2 == 1
    
    def get_checksum(self, output):
        counter = 0
        total = 0
        for cur in output:
            for j in range(cur[1]):
                total += counter * cur[0]
                counter += 1
        return total

    def part1(self):
        input = list(self.input)
        output = []
        i = 0
        j = len(self.input) - 1
        if self.is_space(j):
            j -= 1
        begin_index = 0
        end_index = j // 2

        while(i <= j):
            if not self.is_space(i):
                output.append((begin_index, int(input[i])))
                begin_index += 1
                i += 1
            else:
                space_left = int(input[i])
                while space_left > 0 and i <= j:
                    num_needed = int(input[j])
                    if(space_left > num_needed):
                        output.append((end_index, num_needed))
                        space_left -= num_needed
                        j -= 2
                        end_index -= 1
                    else:
                        left = num_needed - space_left
                        output.append((end_index, space_left))
                        if left == 0:
                            j -= 2
                            end_index -= 1
                        else:
                            input[j] = str(left)
                        space_left = 0
                i += 1
        total = self.get_checksum(output)
        return total
    
    def part2(self):
        input = list(self.input)
        output = []
        i = 0
        begin_index = 0

        while(i < len(input)):
            space_left = int(input[i])
            if not self.is_space(i):
                count = int(input[i])
                if count >= 0:
                    output.append((begin_index, count))
                else:
                    output.append((0, abs(count)))
                begin_index += 1
                i += 1
            else:
                j = len(self.input) - 1
                if self.is_space(j):
                    j -= 1
                end_index = j // 2
                while j > i and space_left > 0:
                    num_needed = int(input[j])
                    if(space_left >= num_needed and num_needed > 0):
                        output.append((end_index, num_needed))
                        space_left -= num_needed
                        input[j] = str(0-num_needed)
                        input[i] = str(space_left)
                    j -= 2
                    end_index -= 1
                if space_left > 0:
                    output.append((0, space_left))
                i += 1

        total = self.get_checksum(output)
        return total