<?php
function parseInput(): array
{
    $aunts = [];
    $file = fopen('input.txt', 'r');
    while ($line = fgets($file)) {
        $matches = [];
        preg_match('/Sue (\d+): (\w*): (\d*), (\w*): (\d*), (\w*): (\d*)/', $line, $matches);
        $aunts[intval($matches[1])] = [
            $matches[2] => intval($matches[3]),
            $matches[4] => intval($matches[5]),
            $matches[6] => intval($matches[7])
        ];
    }
    return $aunts;
}
$machine_result = [
    'children' => 3,
    'cats' => 7,
    'samoyeds' => 2,
    'pomeranians' => 3,
    'akitas' => 0,
    'vizslas' => 0,
    'goldfish' => 5,
    'trees' => 3,
    'cars' => 2,
    'perfumes' => 1,
];
$aunts = parseInput();
foreach($aunts as $num=>$vals) {
    foreach($vals as $what=>$how_much) {
        if($machine_result[$what] !== $how_much) {
            continue 2;
        }
    }
    echo "Part 1: $num\n";
    break;
}

foreach($aunts as $num=>$vals) {
    foreach($vals as $what=>$how_much) {
        if($what === 'cats' || $what === 'trees') {
            if($machine_result[$what] >= $how_much) {
                continue 2;
            }
        }
        elseif($what === 'pomeranians' || $what === 'goldfish') {
            if($machine_result[$what] <= $how_much) {
                continue 2;
            }
        }
        elseif($machine_result[$what] !== $how_much) {
            continue 2;
        }
    }
    echo "Part 2: $num\n";
    break;
}
