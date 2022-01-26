<?php
$directions = explode(', ', file_get_contents('input.txt'));

function getNewDirection($currentDirection, $turn) {
    $directions = ['n', 'e', 's', 'w'];
    $positions = array_flip($directions);
    $turn = $turn === 'R' ? 1 : -1;
    $newPos = ($positions[$currentDirection] + $turn + 4) % 4;
    return $directions[$newPos];
}
function move($currentPosition, $direction, $howMuch) {
    switch($direction) {
        case 'n':
            $currentPosition[1] += $howMuch;
            break;
        case 's':
            $currentPosition[1] -= $howMuch;
            break;
        case 'e':
            $currentPosition[0] += $howMuch;
            break;
        case 'w':
            $currentPosition[0] -= $howMuch;
            break;
    }
    return $currentPosition;
}

function part1() {
    global $directions;

    $current = [0,0];
    $facing = 'n';

    foreach($directions as $direction) {
        $facing = getNewDirection($facing, $direction[0]);
        $current = move($current, $facing, intval(substr($direction, 1)));
    }

    return abs($current[0]) + abs($current[1]);
}

function part2() {
    global $directions;

    $visited = [];
    $current = [0,0];
    $facing = 'n';

    foreach($directions as $direction) {
        $facing = getNewDirection($facing, $direction[0]);
        $moves = intval(substr($direction, 1));
        for($i = 0; $i < $moves; $i++) {
            $current = move($current, $facing, 1);
            $key = "{$current[0]},{$current[1]}";
            if(array_key_exists($key, $visited)) break 2;
            $visited[$key] = true;
        }
    }

    return abs($current[0]) + abs($current[1]);
}

echo 'Part 1: '.part1()."\n";
echo 'Part 2: '.part2()."\n";