<?php
namespace Year15\Day6;
require_once 'Instruction.php';

class Parser {
    public static function parseInput(): array {
        $instructions = [];
        $file = fopen('input.txt', 'r');
        while($line = fgets($file)) {
            $instructions[] = self::parseLine($line);
        }
        return $instructions;
    }

    private static function parseLine(string $line): Instruction {
        $instructionType = self::parseInstructionType($line);
        $numbers = self::parseNumbers($line);
        return new Instruction($instructionType, $numbers[0], $numbers[1], $numbers[2], $numbers[3]);
    }

    private static function parseInstructionType(string $line): InstructionType {
        $match = [];
        preg_match('/[a-z ]+(?= [0-9])/', $line, $match);
        switch($match[0]) {
            case 'turn off':
                return InstructionType::OFF;
            case 'turn on':
                return InstructionType::ON;
            case 'toggle':
                return InstructionType::TOGGLE;
        }
    }

    private static function parseNumbers(string $line): array {
        $match = [];
        preg_match_all('/[0-9]+/', $line, $match, PREG_PATTERN_ORDER);
        $numbers = array_map('intval', $match[0]);
        return $numbers;
    }
}