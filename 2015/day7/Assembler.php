<?php
namespace Year15\Day7;

require_once 'Operation.php';

class Assembler {
    private array $state = [];

    public function __construct(
        private array $operations, 
        private array $overrides = []) {}

    public function runOperations() {
        $operationsToRun = $this->operations;
        while($operationsToRun) {
            foreach($operationsToRun as $i=>$operation) {
                try {
                    $this->state = $operation->run($this->state);
                    foreach($this->overrides as $var=>$val) {
                        $this->state[$var] = $val;
                    }
                    unset($operationsToRun[$i]);
                }
                catch(OperationException $e) {}
            }
        }
    }

    public function getValue(string $var) {
        return $this->state[$var];
    }
}