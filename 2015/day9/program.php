<?php
namespace Year15\Day9;
require_once 'Parser.php';
require_once 'DistanceCalculator.php';

$cities = Parser::parseInput();
$distanceCalculator = new DistanceCalculator($cities);
$distances = array_map(fn($city) => $distanceCalculator->resetAndGetShortestDistance($city), array_keys($cities));
$min_distance = min($distances);
echo "Part 1: $min_distance\n";

foreach($cities as &$to) {
    arsort($to);
}
$distanceCalculator = new DistanceCalculator($cities);
$distances = array_map(fn($city) => $distanceCalculator->resetAndGetShortestDistance($city), array_keys($cities));
$max_distance = max($distances);
echo "Part 1: $max_distance\n";