<?php
namespace Year15\Day12;
require_once 'JsonParser.php';

$json = file_get_contents('input.txt');
$parser = new JsonParser($json);
$numbers = $parser->getNumbers();
$sum = array_sum($numbers);
echo "Part 1: $sum\n";

$non_red_numbers = $parser->getNonRedNumbers();
$sum_non_red = array_sum($non_red_numbers);
echo "Part 2: $sum_non_red\n";