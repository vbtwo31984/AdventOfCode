<?php
namespace Year15\Day9;

class Parser {
    public static function parseInput(): array {
        $cities = [];

        $file = fopen('input.txt', 'r');
        while($line = fgets($file)) {
            $cityDistance = self::parseLine($line);
            self::insertCity($cityDistance, $cities);
        }
        self::sortCities($cities);

        return $cities;
    }

    private static function parseLine(string $line): array {
        $parts = explode(' = ', $line);
        $distance = intval($parts[1]);
        $cities = explode(' to ', $parts[0]);

        return ['city1' => $cities[0], 'city2' => $cities[1], 'distance' => $distance];
    }

    private static function insertCity(array $cityDistance, array &$to) {
        if(array_key_exists($cityDistance['city1'], $to)) {
            $to[$cityDistance['city1']][$cityDistance['city2']] = $cityDistance['distance'];
        }
        else {
            $to[$cityDistance['city1']] = [$cityDistance['city2'] => $cityDistance['distance']];
        }
        if(array_key_exists($cityDistance['city2'], $to)) {
            $to[$cityDistance['city2']][$cityDistance['city1']] = $cityDistance['distance'];
        }
        else {
            $to[$cityDistance['city2']] = [$cityDistance['city1'] => $cityDistance['distance']];
        }
    }

    private static function sortCities(array &$cities) {
        foreach($cities as &$to) {
            asort($to);
        }
    }
}