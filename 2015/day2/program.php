<?php
namespace Year15\Day2;
require_once 'Parser.php';

$presents = Parser::parseInput();
$wrapping_sizes = array_map(fn($p) => $p->getSquareFeetOfWrappingPaper(), $presents);
$ribbon_sizes = array_map(fn($p) => $p->getLengthOfRibbon(), $presents);

$total_wrapping_size = array_sum($wrapping_sizes);
$total_ribbon_size = array_sum($ribbon_sizes);
echo "1: total size of wrapping paper: $total_wrapping_size\n";
echo "2: total length of ribbon: $total_ribbon_size\n";