<?php
$ingredients = [
    [3,0,0,-3,2],
    [-3,3,0,0,9],
    [-1,0,4,0,1],
    [0,0,-2,2,8]
];

$max_score = 0;
for($i = 0; $i < 100; $i++) {
    for($j = 0; $j < 100-$i; $j++) {
        for($k = 0; $k < 100-$i-$j; $k++) {
            $l = 100-$i-$j-$k;
            $scores = [];
            for($s = 0; $s < 4; $s++) {
                $scores[] = max(0, $ingredients[0][$s]*$i+$ingredients[1][$s]*$j+$ingredients[2][$s]*$k+$ingredients[3][$s]*$l);
            }
            $total_score = array_product($scores);
            $max_score = max($max_score, $total_score);
        }
    }
}

echo "Part 1: $max_score\n";

$max_score = 0;
for($i = 0; $i < 100; $i++) {
    for($j = 0; $j < 100-$i; $j++) {
        for($k = 0; $k < 100-$i-$j; $k++) {
            $l = 100-$i-$j-$k;
            $calories = $ingredients[0][4]*$i+$ingredients[1][4]*$j+$ingredients[2][4]*$k+$ingredients[3][4]*$l;
            if($calories !== 500) {
                continue;
            }
            $scores = [];
            for($s = 0; $s < 4; $s++) {
                $scores[] = max(0, $ingredients[0][$s]*$i+$ingredients[1][$s]*$j+$ingredients[2][$s]*$k+$ingredients[3][$s]*$l);
            }
            $total_score = array_product($scores);
            $max_score = max($max_score, $total_score);
        }
    }
}

echo "Part 2: $max_score\n";