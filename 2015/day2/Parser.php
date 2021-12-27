<?php
namespace Year15\Day2;
require_once 'Present.php';

class Parser {
    public static function parseInput(): array {
        $file = fopen('input.txt', 'r');
        $presents = [];
        while($line = fgets($file)) {
            $dimensions = explode('x', $line);
            $dimensions = array_map('intval', $dimensions);
            $presents[] = new Present($dimensions[0], $dimensions[1], $dimensions[2]);
        }
        return $presents;
    }
}