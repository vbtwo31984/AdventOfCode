<?php
namespace Year15\Day13;

class Parser {
    public static function parseInput(): array {
        $happyness = [];

        $file = fopen('input.txt', 'r');
        while($line = fgets($file)) {
            $lineHappyness = self::parseLine($line);
            if(array_key_exists($lineHappyness['from'], $happyness)) {
                $happyness[$lineHappyness['from']][$lineHappyness['to']] = $lineHappyness['amount'];
            }
            else {
                $happyness[$lineHappyness['from']] = [$lineHappyness['to'] => $lineHappyness['amount']];
            }
        }

        return $happyness;
    }

    private static function parseLine(string $line): array {
        $line = trim($line);
        $line = str_replace(
            ['would gain ', 'would lose ', 'happiness units by sitting next to ', '.'],
            ['', '-', '', ''],
            $line
        );
        $items = explode(' ', $line);
        return [
            'from' => $items[0],
            'to' => $items[2],
            'amount' => intval($items[1])
        ];
    }
}