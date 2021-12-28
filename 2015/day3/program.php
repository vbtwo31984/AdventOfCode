<?php
namespace Year15\Day3;

use Year15\Day3\Dispatcher;

require_once 'Parser.php';
require_once 'Dispatcher.php';

$instructions = Parser::parseInput();
$dispatcher = new Dispatcher();
$dispatcher2 = new Dispatcher(2);

foreach($instructions as $instruction) {
    $dispatcher->move($instruction);
    $dispatcher2->move($instruction);
}

$num_visited = $dispatcher->getNumberOfVisitedHouses();
$num_visited2 = $dispatcher2->getNumberOfVisitedHouses();

echo "Part 1: $num_visited visited houses\n";
echo "Part 2: $num_visited2 visited houses\n";