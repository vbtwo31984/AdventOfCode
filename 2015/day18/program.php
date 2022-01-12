<?php
$lights = [];
$file = fopen('input.txt', 'r');
while($line = fgets($file)) {
    $lights = array_merge($lights, str_split(trim($line)));
}
fclose($file);

function get($num, $lights) {
    if(array_key_exists($num, $lights)) return $lights[$num] === '#';
    else return false;
}

function isCorner(int $num, int $side) {
    $corners = [0, $side - 1, $side * $side - $side, $side * $side - 1];
    return in_array($num, $corners);
}

function state(int $num, array $lights, $corners_stuck = false): string {
    $side = sqrt(count($lights));
    if($corners_stuck && isCorner($num, $side)) {
        return '#';
    }
    $neighbors = [$num-$side-1, $num-$side, $num-$side+1, $num-1, $num+1, $num+$side-1, $num+$side, $num+$side+1];
    $neighbors = array_filter($neighbors, function($n) use ($side, $num) {
        return abs($n % $side - $num % $side) <= 1;
    });
    $enabled = array_map(function($n) use ($lights) {
        return get($n, $lights);
    }, $neighbors);
    $num_enabled = array_reduce($enabled, fn($carry, $item) => $item ? $carry + 1 : $carry, 0);
    if(get($num, $lights)) {
        return $num_enabled === 2 || $num_enabled === 3 ? '#' : '.';
    }
    else {
        return $num_enabled === 3 ? '#' : '.';
    }
}

function move($lights, $corners_stuck = false) {
    $lights = array_map(function($n) use ($lights, $corners_stuck) {
        return state($n, $lights, $corners_stuck);
    }, array_keys($lights));
    return $lights;
}

function print_lights($lights) {
    $side = sqrt(count($lights));
    $chunks = array_chunk($lights, $side);
    foreach($chunks as $chunk) {
        echo implode($chunk)."\n";
    }
}

$num_moves = 100;
for($i = 0; $i < $num_moves; $i++) {
    $lights = move($lights);
    // print_lights($lights);
    echo "$i of $num_moves\n";
}

$num_enabled = array_reduce($lights, fn($carry, $item) => $item === '#' ? $carry + 1 : $carry, 0);
echo "Part 1: $num_enabled\n";

$lights = [];
$file = fopen('input.txt', 'r');
while($line = fgets($file)) {
    $lights = array_merge($lights, str_split(trim($line)));
}
$side = sqrt(count($lights));
$corners = [0, $side - 1, $side * $side - $side, $side * $side - 1];
foreach($corners as $corner) {
    $lights[$corner] = '#';
}

fclose($file);
for($i = 0; $i < $num_moves; $i++) {
    $lights = move($lights, true);
    // print_lights($lights);
    echo "$i of $num_moves\n";
}
$num_enabled = array_reduce($lights, fn($carry, $item) => $item === '#' ? $carry + 1 : $carry, 0);
echo "Part 2: $num_enabled\n";