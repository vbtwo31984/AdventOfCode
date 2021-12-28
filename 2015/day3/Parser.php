<?php
namespace Year15\Day3;

class Parser {
    public static function parseInput(): array {
        $input = file_get_contents('input.txt');
        return str_split($input);
    }
}