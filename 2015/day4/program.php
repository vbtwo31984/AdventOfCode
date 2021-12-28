<?php
namespace Year15\Day4;

require_once 'Miner.php';

$input = 'bgvyzdsv';
$miner = new Miner($input);
$lowestNumber5 = $miner->mineNumber(5);
echo "Part 1: $lowestNumber5\n";
$lowestNumber6 = $miner->mineNumber(6);
echo "Part 1: $lowestNumber6\n";