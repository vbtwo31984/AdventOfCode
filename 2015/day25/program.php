<?php
$row = 2981;
$column = 3075;

$num = 1;
for($i = 1; $i < $row; $i++) {
    $num += $i;
}
for($i = 1; $i < $column; $i++) {
    $num += $row + $i;
}

echo "Num: $num\n";

$code = 20151125;
for($i = 1; $i < $num; $i++) {
    $code = ($code * 252533) % 33554393;
}
echo "Part 1: $code\n";