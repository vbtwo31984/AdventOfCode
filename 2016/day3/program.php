<?php
function isValidTriangle($sides) {
    if($sides[0]+$sides[1] <= $sides[2]) return false;
    if($sides[0]+$sides[2] <= $sides[1]) return false;
    if($sides[1]+$sides[2] <= $sides[0]) return false;
    return true;
}

$file = fopen('input.txt', 'r');
$sides = [];
while($line = fgets($file)) {
    $matches = [];
    preg_match_all('/[\d]+/', $line, $matches);
    $sides[] = array_map('intval', $matches[0]);
}
fclose($file);

$valid_triangles = array_filter($sides, 'isValidTriangle');
$num_valid = count($valid_triangles);
echo "Part 1: $num_valid\n";

$file = fopen('input.txt', 'r');
$sides = [];
$triplet = [];
while($line = fgets($file)) {
    $matches = [];
    preg_match_all('/[\d]+/', $line, $matches);
    $triplet[] = array_map('intval', $matches[0]);
    if(count($triplet) === 3) {
        for($i = 0; $i < 3; $i++) {
            $side = [];
            foreach($triplet as $num) {
                $side[] = $num[$i];
            }
            $sides[] = $side;
        }
        $triplet = [];
    }
}
fclose($file);

$valid_triangles = array_filter($sides, 'isValidTriangle');
$num_valid = count($valid_triangles);
echo "Part 2: $num_valid\n";

