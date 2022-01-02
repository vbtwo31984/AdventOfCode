<?php
namespace Year15\Day14;
require_once 'Deer.php';

class ScoreKeeper {
    public function __construct(private array $deer) {}

    public function getWinner(int $seconds): int {
        $scores = array_fill(0, count($this->deer), 0);
        for($i = 1; $i <= $seconds; $i++) {
            $distances = array_map(fn($d) => $d->calculateDistance($i), $this->deer);
            $max = max($distances);
            foreach($distances as $index=>$distance) {
                if($distance === $max) {
                    $scores[$index]++;
                }
            }
        }
        return max($scores);
    }
}