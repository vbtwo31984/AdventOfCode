<?php
class Parser {
    public static function parseInput(): string {
        $input = file_get_contents('input.txt');
        return $input;
    }
}

class Elevator {
    private string $instructions;
    private int $floor = 0;

    public function __construct(string $instructions) {
        $this->instructions = $instructions;
    }

    private function reset() {
        $this->floor = 0;
    }

    public function move(string $instruction) {
        if($instruction === '(') $this->floor++;
        else $this->floor--;
    }

    public function getEndFloor(): int {
        $this->reset();
        $size = strlen($this->instructions);
        for($i = 0; $i < $size; $i++) {
            $char = $this->instructions[$i];
            $this->move($char);
        }
        return $this->floor;
    }

    public function getFirstBasementPosition(): int {
        $this->reset();
        $position = 0;
        while($this->floor !== -1) {
            $this->move($this->instructions[$position]);
            $position++;
        }
        return $position;
    }
}

$input = Parser::parseInput();
$elevator = new Elevator($input);
$floor = $elevator->getEndFloor();
$positionOfBasement = $elevator->getFirstBasementPosition();

echo "1: end: $floor floor\n";
echo "2: position of first basement: $positionOfBasement\n";