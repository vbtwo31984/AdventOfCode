<?php
function display(array $display) {
    foreach($display as $row) {
        foreach($row as $val) {
            echo $val ? '#' : '.';
        }
        echo "\n";
    }
    echo "\n";
}

function rect(array &$display, int $rows, int $columns) {
    for($x = 0; $x < $rows; $x++) {
        for($y = 0; $y < $columns; $y++) {
            $display[$x][$y] = true;
        }
    }
}

function shift(array &$arr, int $by) {
    for($by; $by > 0; $by--) {
        array_unshift($arr, array_pop($arr));
    }
}

function rotateColumn(array &$display, int $column, int $by) {
    $column_arr = array_map(fn($row) => $row[$column], $display);
    shift($column_arr, $by);
    foreach($column_arr as $y=>$val) {
        $display[$y][$column] = $val;
    }
}

function rotateRow(array &$display, int $row, int $by) {
    shift($display[$row], $by);
}

function countLit(array $display): int {
    $lit = array_reduce($display, fn($carry, $row) => $carry + count(array_filter($row)), 0);
    return $lit;
}

function run(array $display, array $instructions) {
    foreach($instructions as $instruction) {
        $matches = [];
        preg_match_all('/[\d]+/', $instruction, $matches);
        if(str_starts_with($instruction, 'rect')) {
            rect($display, intval($matches[0][1]), intval($matches[0][0]));
        }
        elseif(str_starts_with($instruction, 'rotate column')) {
            rotateColumn($display, intval($matches[0][0]), intval($matches[0][1]));
        }
        else {
            rotateRow($display, intval($matches[0][0]), intval($matches[0][1]));
        }
    }
    $lit = countLit($display);
    echo "Part 1: $lit\n";
    echo "Part 2:\n";
    display($display);
}

$row = array_fill(0, 50, false);
$display = array_fill(0, 6, $row);
$instructions = file('input.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
run($display, $instructions);