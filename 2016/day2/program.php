<?php
$instructions = file('input.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

function move($position, $direction, $buttons) {
    switch($direction) {
        case 'U':
            $newX = $position[0]-1;
            if($newX < 0 || $buttons[$newX][$position[1]] === '.')
                return $position;
            else return [$newX, $position[1]];
        case 'D':
            $newX = $position[0]+1;
            if($newX >= count($buttons) || $buttons[$newX][$position[1]] === '.')
                return $position;
            else return [$newX, $position[1]];
        case 'L':
            $newY = $position[1]-1;
            if($newY < 0 || $buttons[$position[0]][$newY] === '.')
                return $position;
            else return [$position[0], $newY];
        case 'R':
            $newY = $position[1]+1;
            if($newY >= count($buttons[0]) || $buttons[$position[0]][$newY] === '.')
                return $position;
            else return [$position[0], $newY];
    }
}

function followInstructions($buttons, $current_position) {
    global $instructions;
    $digits = [];

    foreach($instructions as $instruction) {
        $length = strlen($instruction);
        for($i = 0; $i < $length; $i++) {
            $direction = $instruction[$i];
            $current_position = move($current_position, $direction, $buttons);
        }
        $digits[] = $buttons[$current_position[0]][$current_position[1]];
    }

    return implode('', $digits);
}

function part1() {
    $buttons = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9']
    ];
    $current_position = [1, 1];
    return followInstructions($buttons, $current_position);
}

function part2() {
    $buttons = [
        ['.','.','1','.','.'],
        ['.','2','3','4','.'],
        ['5','6','7','8','9'],
        ['.','A','B','C','.'],
        ['.','.','D','.','.'],
    ];
    $current_position = [2, 0];
    return followInstructions($buttons, $current_position);
}

echo "Part 1: ".part1()."\n";
echo "Part 2: ".part2()."\n";