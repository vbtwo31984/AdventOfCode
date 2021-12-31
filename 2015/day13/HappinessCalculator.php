<?php

namespace Year15\Day13;

class HappinessCalculator
{
    private array $happinessPairs = [];
    private array $perms = [];
    public function __construct(private array $happiness)
    {
        foreach ($happiness as $from => $toArr) {
            foreach ($toArr as $to => $amount) {
                $totalHappiness = $amount + $happiness[$to][$from];
                if (array_key_exists($from, $this->happinessPairs)) {
                    $this->happinessPairs[$from][$to] = $totalHappiness;
                } else {
                    $this->happinessPairs[$from] = [$to => $totalHappiness];
                }
            }
        }
        $this->permute(array_keys($happiness));
    }

    private function permute(array $items, array $perms = [])
    {
        if (empty($items)) {
            $this->perms[] = $perms;
        } else {
            for ($i = count($items) - 1; $i >= 0; --$i) {
                $newitems = $items;
                $newperms = $perms;
                list($foo) = array_splice($newitems, $i, 1);
                array_unshift($newperms, $foo);
                $this->permute($newitems, $newperms);
            }
        }
    }

    public function getMaxHappiness()
    {
        $happiness = array_map(fn($order) => $this->calculateHappiness($order), $this->perms);
        return max($happiness);
    }

    private function calculateHappiness(array $order): int {
        $order[] = $order[0];
        $happiness = 0;
        for($i = 0; $i < count($order) - 1; $i++) {
            $happiness += $this->happinessPairs[$order[$i]][$order[$i+1]];
        }
        return $happiness;
    }
}
