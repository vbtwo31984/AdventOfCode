<?php
namespace Year15\Day14;
require_once 'Deer.php';

class Parser {
    public static function parseInput(): array {
        $deer = [];
        $file = fopen('input.txt', 'r');
        while($line = fgets($file)) {
            $deer[] = new Deer($line);
        }
        return $deer;
    }
}