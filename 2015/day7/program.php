<?php
namespace Year15\Day7;

require_once 'Parser.php';
require_once 'Assembler.php';

$operations = Parser::parseInput();
$assembler = new Assembler($operations);
$assembler->runOperations();
$valA = $assembler->getValue('a');

$assembler2 = new Assembler($operations, ['b'=>$valA]);
$assembler2->runOperations();
$valA2 = $assembler2->getValue('a');
echo "Part 1: $valA\n";
echo "Part 2: $valA2\n";