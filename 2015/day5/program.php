<?php
namespace Year15\Day5;
require_once 'StringChecker.php';

$lines = file('input.txt');

$nice_lines1 = array_filter($lines, fn($line) => StringChecker::isStringNicePart1($line));
$num_nice_lines1 = count($nice_lines1);
$nice_lines2 = array_filter($lines, fn($line) => StringChecker::isStringNicePart2($line));
$num_nice_lines2 = count($nice_lines2);

echo "Part 1: $num_nice_lines1\n";
echo "Part 2: $num_nice_lines2\n";