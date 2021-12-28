<?php
namespace Year15\Day6;

class Decorator {
    private array $lights = [];
    private array $brightness = [];

    public function __construct(int $numX, int $numY)
    {
        for($x = 0; $x < $numX; $x++) {
            for($y = 0; $y < $numY; $y++) {
                $this->lights["$x,$y"] = false;
                $this->brightness["$x,$y"] = 0;
            }
        }
    }

    public function runInstruction(Instruction $instruction) {
        switch($instruction->instructionType) {
            case InstructionType::ON:
                $this->turnOn($instruction);
                break;
            case InstructionType::OFF:
                $this->turnOff($instruction);
                break;
            case InstructionType::TOGGLE:
                $this->toggle($instruction);
                break;
        }
    }

    public function getCountOn(): int {
        $on = array_filter($this->lights);
        return count($on);
    }

    public function getTotalBrightness(): int {
        return array_sum($this->brightness);
    }

    private function turnOn(Instruction $instruction) {
        for($x = $instruction->fromX; $x <= $instruction->toX; $x++) {
            for($y = $instruction->fromY; $y <= $instruction->toY; $y++) {
                $this->lights["$x,$y"] = true;
                $this->brightness["$x,$y"]++;
            }
        }
    }

    private function turnOff(Instruction $instruction) {
        for($x = $instruction->fromX; $x <= $instruction->toX; $x++) {
            for($y = $instruction->fromY; $y <= $instruction->toY; $y++) {
                $this->lights["$x,$y"] = false;
                if($this->brightness["$x,$y"] > 0)
                    $this->brightness["$x,$y"]--;
            }
        }
    }

    private function toggle(Instruction $instruction) {
        for($x = $instruction->fromX; $x <= $instruction->toX; $x++) {
            for($y = $instruction->fromY; $y <= $instruction->toY; $y++) {
                $this->lights["$x,$y"] = !$this->lights["$x,$y"];
                $this->brightness["$x,$y"]+=2;
            }
        }
    }
}