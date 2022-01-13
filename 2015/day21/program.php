<?php
/*
Hit Points: 103
Damage: 9
Armor: 2
*/
$weapons = [
    ['Dagger', 8, 4, 0],
    ['Shortsword', 10, 5, 0],
    ['Warhammer', 25, 6, 0],
    ['Longsword', 40, 7, 0],
    ['Greataxe', 74, 8, 0]
];
$armor = [
    ['Leather', 13, 0, 1],
    ['Chainmail', 31, 0, 2],
    ['Splintmail', 53, 0, 3],
    ['Bandedmail', 75, 0, 4],
    ['Platemail', 102, 0, 5]
];
$rings = [
    ['Damage +1', 25, 1, 0],
    ['Damage +2', 50, 2, 0],
    ['Damage +3', 100, 3, 0],
    ['Defense +1', 20, 0, 1],
    ['Defense +2', 40, 0, 2],
    ['Defense +3', 80, 0, 3]
];
$boss = [103, 9, 2];

function win($player, $boss)
{
    $playerHit = max($player[1] - $boss[2], 1);
    $bossHit = max($boss[1] - $player[2], 1);
    $playerNeedsMoves = ceil($boss[0] / $playerHit);
    $bossNeedsMoves = ceil($player[0] / $bossHit);
    return $playerNeedsMoves <= $bossNeedsMoves;
}

$min_price = PHP_INT_MAX;
$max_price = PHP_INT_MIN;
foreach ($weapons as $weapon) {
    // just weapon
    $player = [100, $weapon[2], $weapon[3]];
    if (win($player, $boss)) {
        $min_price = min($min_price, $weapon[1]);
    }
    else {
        $max_price = max($max_price, $weapon[1]);
    }

    foreach ($armor as $armor_piece) {
        // weapon+armor
        $player = [100, $weapon[2], $armor_piece[3]];
        $price = $weapon[1] + $armor_piece[1];
        if (win($player, $boss)) {
            $min_price = min($min_price, $price);
        }
        else {
            $max_price = max($max_price, $price);
        }

        foreach ($rings as $ring1) {
            //weapon+armor+1 ring
            $player = [100, $weapon[2] + $ring1[2], $armor_piece[3] + $ring1[3]];
            $price = $weapon[1] + $armor_piece[1] + $ring1[1];
            if (win($player, $boss)) {
                $min_price = min($min_price, $price);
            }
            else {
                $max_price = max($max_price, $price);
            }

            foreach ($rings as $ring2) {
                //weapon+armor+2 rings
                if ($ring1[0] === $ring2[0]) continue;
                $player = [100, $weapon[2] + $ring1[2] + $ring2[2], $armor_piece[3] + $ring1[3] + $ring2[3]];
                $price = $weapon[1] + $armor_piece[1] + $ring1[1] + $ring2[1];
                if (win($player, $boss)) {
                    $min_price = min($min_price, $price);
                }
                else {
                    $max_price = max($max_price, $price);
                }
            }
        }
    }

    foreach ($rings as $ring1) {
        //weapon+1 ring
        $player = [100, $weapon[2] + $ring1[2], $ring1[3]];
        $price = $weapon[1] + $ring1[1];
        if (win($player, $boss)) {
            $min_price = min($min_price, $price);
        }
        else {
            $max_price = max($max_price, $price);
        }

        foreach ($rings as $ring2) {
            //weapon+2 rings
            if ($ring1[0] === $ring2[0]) continue;
            $player = [100, $weapon[2] + $ring1[2] + $ring2[2], $ring1[3] + $ring2[3]];
            $price = $weapon[1] + $ring1[1] + $ring2[1];
            if (win($player, $boss)) {
                $min_price = min($min_price, $price);
            }
            else {
                $max_price = max($max_price, $price);
            }
        }
    }
}

echo "Part 1: $min_price\n";
echo "Part 2: $max_price\n";
