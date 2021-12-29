<?php
namespace Year15\Day8;
require_once 'CodeString.php';

class Parser {
    public static function parseInput(): array {
        $file = fopen('input.txt', 'r');
        $strings = [];
        while($line = fgets($file)) {
            $strings[] = new CodeString($line);
        }
        return $strings;
    }
}