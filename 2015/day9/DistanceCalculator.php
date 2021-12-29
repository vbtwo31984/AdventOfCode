<?php
namespace Year15\Day9;

class DistanceCalculator {
    private array $visited = [];
    public function __construct(private array $cities) {}

    private function reset() {
        $this->visited = [];
        $this->distance = 0;
    }

    public function resetAndGetShortestDistance(string $from): int {
        $this->reset();
        return $this->getShortestDistance($from);
    }

    public function getShortestDistance(string $from): int {
        $this->visited[] = $from;
        if(count($this->visited) === count($this->cities)) return 0;

        $closestCity = $this->findClosestNonVisitedCity($from);
        $distance = $closestCity['distance'] + $this->getShortestDistance($closestCity['city']);
        return $distance;
    }

    public function findClosestNonVisitedCity(string $from): array {
        foreach($this->cities[$from] as $city=>$distance) {
            if(!in_array($city, $this->visited)) {
                return ['city'=>$city, 'distance'=>$distance];
            }
        }
    }
}