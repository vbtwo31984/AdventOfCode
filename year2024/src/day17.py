class Day17:
    a = b = c = 0
    program = []
    pointer = 0
    output = []

    def __init__(self, input):
        self.input = input

    def _reset(self):
        lines = self.input.splitlines()
        self.a = int(lines[0].split(": ")[1])
        self.b = int(lines[1].split(": ")[1])
        self.c = int(lines[2].split(": ")[1])
        self.program = list(map(int, lines[4].split(": ")[1].split(",")))
        self.pointer = 0
        self.output = []

    def _combo_op(self, op):
        if 0 < op < 4:
            return op
        elif op == 4:
            return self.a
        elif op == 5:
            return self.b
        elif op == 6:
            return self.c
        
    def _run_op(self):
        operation = self.program[self.pointer]
        operand = self.program[self.pointer + 1]

        if operation == 0: #adv (division)
            operand = self._combo_op(operand)
            numerator = self.a
            denominator = pow(2, operand)
            self.a = numerator // denominator
        elif operation == 1: #bxl (xor)
            self.b ^= operand
        elif operation == 2: #bst (mod)
            operand = self._combo_op(operand)
            self.b = operand % 8
        elif operation == 3: #jnz (jump)
            if self.a != 0:
                self.pointer = operand - 2
        elif operation == 4: #bxc (register xor)
            self.b ^= self.c
        elif operation == 5: #out
            operand = self._combo_op(operand)
            self.output.append(operand % 8)
        elif operation == 6: #bdv
            operand = self._combo_op(operand)
            numerator = self.a
            denominator = pow(2, operand)
            self.b = numerator // denominator
        elif operation == 7: #cdv
            operand = self._combo_op(operand)
            numerator = self.a
            denominator = pow(2, operand)
            self.c = numerator // denominator
        
        self.pointer += 2

    def _run(self):
        while self.pointer < len(self.program):
            self._run_op()

    def part1(self):
        self._reset()
        self._run()
        return ",".join(map(str, self.output))
    
    def part2(self):
        candidates = [0]
        for length in range(1, len(self.program) + 1):
            out = []
            for num in candidates:
                for offset in range(2**3):
                    a = (2**3) * num + offset
                    self._reset()
                    self.a = a
                    self._run()
                    if self.output == self.program[-length:]:
                        out.append(a)
            candidates = out

        return min(candidates)