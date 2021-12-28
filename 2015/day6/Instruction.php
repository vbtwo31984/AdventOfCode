<?php
namespace Year15\Day6;

enum InstructionType {
    case ON;
    case OFF;
    case TOGGLE;
}

class Instruction {
    public function __construct(
        public InstructionType $instructionType,
        public int $fromX,
        public int $fromY,
        public int $toX,
        public int $toY
    ) {}
}