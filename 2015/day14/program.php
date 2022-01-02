<?php
namespace Year15\Day14;
require_once 'Parser.php';
require_once 'ScoreKeeper.php';

$deer = Parser::parseInput();
$distances = array_map(fn($d) => $d->calculateDistance(2503), $deer);
$max_distance = max($distances);

echo "Part 1: $max_distance\n";

$scoreKeeper = new ScoreKeeper($deer);
$max_score = $scoreKeeper->getWinner(2503);
echo "Part 2: $max_score\n";