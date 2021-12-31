<?php
namespace Year15\Day13;
ini_set('memory_limit', '2g');
require_once 'Parser.php';
require_once 'HappinessCalculator.php';

$happiness = Parser::parseInput();
$calculator = new HappinessCalculator($happiness);
$max = $calculator->getMaxHappiness();
echo "Part 1: $max\n";

$me = [];
foreach($happiness as $from=>&$val) {
    $val['me'] = 0;
    $me[$from] = 0;
}
$happiness['me'] = $me;
$calculator = new HappinessCalculator($happiness);
$max2 = $calculator->getMaxHappiness();
echo "Part 2: $max2\n";