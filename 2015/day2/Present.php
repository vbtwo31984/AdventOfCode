<?php
namespace Year15\Day2;

class Present {
    private int $length;
    private int $width;
    private int $height;

    public function __construct(int $length, int $width, int $height) {
        $this->length = $length;
        $this->width = $width;
        $this->height = $height;
    }

    public function getSquareFeetOfWrappingPaper(): int {
        $surfaceArea = 2 * $this->length * $this->width
            + 2 * $this->width * $this->height
            + 2 * $this->height * $this->length;
        $slack = $this->calculateSlack();

        return $surfaceArea + $slack;
    }

    public function getLengthOfRibbon(): int {
        return $this->calculateWrap() + $this->calculateBow();
    }

    private function calculateSlack(): int {
        $dimensions = $this->getSortedDimensions();
        return $dimensions[0] * $dimensions[1];
    }

    private function getSortedDimensions(): array {
        $dimensions = [$this->length, $this->width, $this->height];
        sort($dimensions);
        return $dimensions;
    }

    private function calculateWrap(): int {
        $dimensions = $this->getSortedDimensions();
        return $dimensions[0] * 2 + $dimensions[1] * 2;
    }

    private function calculateBow(): int {
        return $this->height * $this->width * $this->length;
    }
}