<?php
ini_set('memory_limit', '2g');
$num_presents = 34000000;
$houses = array_fill(1, $num_presents / 10, 0);
for($i = 1; $i < $num_presents / 10; $i++) {
    for($j = $i; $j < $num_presents / 10; $j += $i) {
        $houses[$j] += $i * 10;
    }
}
foreach($houses as $house=>$num) {
    if($num >= $num_presents) {
        echo "Part 1: $house\n";
        break;
    }
}


$houses = array_fill(1, ceil($num_presents / 11), 0);
for($i = 1; $i < $num_presents / 11; $i++) {
    for($j = $i, $k = 0; $j < $num_presents / 11 && $k < 50; $j += $i, $k++) {
        $houses[$j] += $i * 11;
    }
}
foreach($houses as $house=>$num) {
    if($num >= $num_presents) {
        echo "Part 2: $house\n";
        break;
    }
}