from enum import Enum
from functools import lru_cache

class Operation(Enum):
    XOR = "XOR"
    OR = "OR"
    AND = "AND"

class Day24:
    def __init__(self, input):
        self.input = input
        split = input.split("\n\n")
        self._set_initial_values(split[0])
        self._set_wires(split[1])

    def _set_initial_values(self, input):
        lines = input.splitlines()
        values = {}
        for line in lines:
            line = line.split(": ")
            values[line[0]] = int(line[1])
        self.initial_values = values

    def _set_wires(self, input):
        lines = input.splitlines()
        wires = {}
        for line in lines:
            line = line.split(" -> ")
            operations = line[0].split(" ")
            wires[line[1]] = (operations[0], Operation(operations[1]), operations[2])
        self.wires = wires

    def find_z_wires(self):
        return sorted([wire for wire in self.wires if wire[0] == "z"], reverse=True)

    @lru_cache(maxsize=None)
    def get_value(self, wire):
        if wire in self.initial_values:
            return self.initial_values[wire]
        operation = self.wires[wire]
        if operation[1] == Operation.AND:
            return self.get_value(operation[0]) & self.get_value(operation[2])
        if operation[1] == Operation.OR:
            return self.get_value(operation[0]) | self.get_value(operation[2])
        if operation[1] == Operation.XOR:
            return self.get_value(operation[0]) ^ self.get_value(operation[2])


    def part1(self):
        z_wires = self.find_z_wires()
        values = [self.get_value(wire) for wire in z_wires]
        output = int("".join(map(str, values)), 2)
        return output
    
    def part2(self):
        return 0