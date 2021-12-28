<?php
namespace Year15\Day7;

use Exception;

class OperationException extends Exception {}

abstract class Operation {
    public abstract function run(array $state): array;
    
    public static function create(string $line): Operation {
        $match = [];
        if(preg_match('/^([a-z0-9]+) -> ([a-z]+)/', $line, $match)) {
            return new AssignOperation($match[1], $match[2]);
        }
        if(preg_match('/^([a-z0-9]+) AND ([a-z]+) -> ([a-z]+)/', $line, $match)) {
            return new AndOperation($match[1], $match[2], $match[3]);
        }
        if(preg_match('/^([a-z0-9]+) OR ([a-z]+) -> ([a-z]+)/', $line, $match)) {
            return new OrOperation($match[1], $match[2], $match[3]);
        }
        if(preg_match('/^([a-z]+) LSHIFT ([0-9]+) -> ([a-z]+)/', $line, $match)) {
            return new LShiftOperation($match[1], $match[2], $match[3]);
        }
        if(preg_match('/^([a-z]+) RSHIFT ([0-9]+) -> ([a-z]+)/', $line, $match)) {
            return new RShiftOperation($match[1], $match[2], $match[3]);
        }
        if(preg_match('/^NOT ([a-z]+) -> ([a-z]+)/', $line, $match)) {
            return new NotOperation($match[1], $match[2]);
        }
        echo $line;
    }

    protected function get(string $var, array $state): int {
        if(array_key_exists($var, $state)) {
            return $state[$var];
        }
        else throw new OperationException('Not Assigned');
    }
}

class AssignOperation extends Operation {
    public function __construct(private string $val, private string $to) {}

    public function run(array $state): array {
        $state[$this->to] = is_numeric($this->val) ? intval($this->val) : $this->get($this->val, $state);
        return $state;
    }
}

class AndOperation extends Operation {
    public function __construct(private string $leftOperand, private string $rightOperand, private string $to) {}

    public function run(array $state): array {
        $left = is_numeric($this->leftOperand) ? intval($this->leftOperand) : $this->get($this->leftOperand, $state);
        $right = $this->get($this->rightOperand, $state);

        $state[$this->to] = $left & $right;
        return $state;
    }
}

class OrOperation extends Operation {
    public function __construct(private string $leftOperand, private string $rightOperand, private string $to) {}

    public function run(array $state): array {
        $left = is_numeric($this->leftOperand) ? intval($this->leftOperand) : $this->get($this->leftOperand, $state);
        $right = $this->get($this->rightOperand, $state);

        $state[$this->to] = $left | $right;
        return $state;
    }
}

class LShiftOperation extends Operation {
    public function __construct(private string $operand, private int $howMuch, private string $to) {}

    public function run(array $state): array {
        $val = $this->get($this->operand, $state);

        $state[$this->to] = ($val << $this->howMuch) & 65535;
        return $state;
    }
}

class RShiftOperation extends Operation {
    public function __construct(private string $operand, private int $howMuch, private string $to) {}

    public function run(array $state): array {
        $val = $this->get($this->operand, $state);

        $state[$this->to] = $val >> $this->howMuch;
        return $state;
    }
}

class NotOperation extends Operation {
    public function __construct(private string $operand, private string $to) {}

    public function run(array $state): array {
        $val = $this->get($this->operand, $state);

        $state[$this->to] = ~$val;
        return $state;
    }
}