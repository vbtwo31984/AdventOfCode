<?php
namespace Year15\Day6;
ini_set('memory_limit', '2G');
require_once 'Parser.php';
require_once 'Decorator.php';

$instructions = Parser::parseInput();
$decorator = new Decorator(1000, 1000);
foreach($instructions as $instruction) {
    $decorator->runInstruction($instruction);
}

$numOn = $decorator->getCountOn();
$brightness = $decorator->getTotalBrightness();
echo "Part 1: $numOn\n";
echo "Part 2: $brightness\n";