<?php
namespace Year15\Day7;

require_once 'Operation.php';

class Parser {
    public static function parseInput(): array {
        $file = fopen('input.txt', 'r');
        $operations = [];

        while($line = fgets($file)) {
            $operations[] = Operation::create($line);
        }
        return $operations;
    }
}