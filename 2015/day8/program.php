<?php
namespace Year15\Day8;

require_once 'Parser.php';
require_once 'CodeString.php';

$strings = Parser::parseInput();
$lengths = array_map(fn($s) => $s->getLength(), $strings);
$code_lengths = array_map(fn($s) => $s->getCodeLength(), $strings);
$encoded_lengths = array_map(fn($s) => $s->getEncodedLength(), $strings);

$sum_lengths = array_sum($lengths);
$sum_code_lengths = array_sum($code_lengths);
$sum_encoded_lengths = array_sum($encoded_lengths);

$sum_diff = $sum_lengths - $sum_code_lengths;
$encoded_diff = $sum_encoded_lengths - $sum_lengths;
echo "Part 1: $sum_diff\n";
echo "Part 2: $encoded_diff\n";