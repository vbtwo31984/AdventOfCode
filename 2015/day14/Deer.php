<?php
namespace Year15\Day14;

class Deer {
    private int $speed;
    private int $flyTime;
    private int $restTime;

    public function __construct(string $description)
    {
        $matches = [];
        preg_match_all('/[0-9]+/', $description, $matches);
        $this->speed = intval($matches[0][0]);
        $this->flyTime = intval($matches[0][1]);
        $this->restTime = intval($matches[0][2]);
    }

    public function calculateDistance(int $seconds): int {
        $distance = 0;
        $curTime = 0;
        $flying = true;
        while($curTime < $seconds) {
            if($flying) {
                $flyTime = min($this->flyTime, $seconds - $curTime);
                $distance += $flyTime * $this->speed;
                $curTime += $this->flyTime;
            }
            else {
                $curTime += $this->restTime;
            }
            $flying = !$flying;
        }
        return $distance;
    }
}