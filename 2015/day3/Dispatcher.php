<?php
namespace Year15\Day3;

class Dispatcher {
    private array $visited = ['0,0'=>true];
    private array $currentPositions  = [];
    private int $nextSanta = 0;

    public function __construct(private int $numberOfSantas = 1) {
        for($i = 0; $i < $numberOfSantas; $i++) {
            $this->currentPositions[$i] = ['x'=>0, 'y'=>0];
        }
    }
    
    public function move($direction) {
        switch($direction) {
            case '>':
                $this->currentPositions[$this->nextSanta]['x']++;
                break;
            case '<':
                $this->currentPositions[$this->nextSanta]['x']--;
                break;
            case '^':
                $this->currentPositions[$this->nextSanta]['y']++;
                break;
            case 'v':
                $this->currentPositions[$this->nextSanta]['y']--;
                break;
        }
        $x = $this->currentPositions[$this->nextSanta]['x'];
        $y = $this->currentPositions[$this->nextSanta]['y'];
        $this->visited["$x,$y"] = true;
        $this->nextSanta = ($this->nextSanta + 1) % $this->numberOfSantas;
    }

    public function getNumberOfVisitedHouses(): int {
        return count($this->visited);
    }
}