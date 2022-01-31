<?php
$strings = file('input.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
$len = strlen($strings[0]);
$decoded = '';
$decoded2 = '';
for($i = 0; $i < $len; $i++) {
    $nums = [];
    foreach($strings as $string) {
        $char = $string[$i];
        if(array_key_exists($char, $nums)) $nums[$char]++;
        else $nums[$char] = 1;
    }
    arsort($nums);
    $decoded .= key($nums);

    asort($nums);
    $decoded2 .= key($nums);
}

echo "Part 1: $decoded\n";
echo "Part 2: $decoded2\n";