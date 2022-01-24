<?php
$instructions = [];
$file = fopen('input.txt', 'r');
while($line = fgets($file)) {
    $line = explode(' ', $line);
    $instruction = $line[0];
    switch($instruction) {
        case 'hlf':
        case 'tpl':
        case 'inc':
            $register = trim($line[1]);
            $instructions[] = ['i'=>$instruction, 'r'=>$register];
            break;
        case 'jmp':
            $amount = intval($line[1]);
            $instructions[] = ['i'=>$instruction, 'a'=>$amount];
            break;
        case 'jie':
        case 'jio':
            $instructions[] = ['i'=>$instruction, 'r'=>trim($line[1], ','), 'a'=>intval($line[2])];
    }
}

$part1 = ['a'=>0,'b'=>0];
$part2 = ['a'=>1,'b'=>0];
function run($registers, $instructions) {
    $current = 0;
    while(array_key_exists($current, $instructions)) {
        $instruction = $instructions[$current];
        //echo "$current - {$instruction['i']} - a: {$registers['a']}, b: {$registers['b']}\n";
        switch($instruction['i']) {
            case 'hlf':
                $registers[$instruction['r']] /= 2;
                $current++;
                break;
            case 'tpl':
                $registers[$instruction['r']] *= 3;
                $current++;
                break;
            case 'inc':
                $registers[$instruction['r']]++;
                $current++;
                break;
            case 'jmp':
                $current += $instruction['a'];
                break;
            case 'jie':
                if($registers[$instruction['r']] % 2 === 0) {
                    $current += $instruction['a'];
                }
                else $current++;
                break;
            case 'jio':
                if($registers[$instruction['r']] === 1) {
                    $current += $instruction['a'];
                }
                else $current++;
                break;
        }
    }
    return $registers;
}
$registers = run($part1, $instructions);
echo "Part 1: {$registers['b']}\n";
$registers = run($part2, $instructions);
echo "Part 1: {$registers['b']}\n";