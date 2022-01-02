<?php
$vessels = file('input.txt');
$vessels = array_map('intval', $vessels);
rsort($vessels);

$eggnog = 150;
$current = 0;

// $vessels = [20, 15, 10, 5, 5];
// $eggnog = 25;

function countEggnog(int $total, array $vessels, int $eggnog, $used = [], $needToUse = null): int
{
    if($total === $eggnog) {
        if(!$needToUse || $needToUse === count($used))
            return 1;
    }
    if(!$vessels || $total > $eggnog) return 0;
    $count = 0;
    
    do {
        $vessel = array_shift($vessels);
        if($total + $vessel <= $eggnog) {
            $used[] = $vessel;
            $count += countEggnog($total + $vessel, $vessels, $eggnog, $used, $needToUse);
            array_pop($used);
        }
    }
    while($vessels);
    return $count;
}
$count = countEggnog(0, $vessels, $eggnog);
echo "Part 1: $count\n";

function minUsedContainers(int $total, array $vessels, int $eggnog, $used = []): int
{
    if($total === $eggnog) {
        return count($used);
    }
    if(!$vessels || $total > $eggnog) return PHP_INT_MAX;
    $min_used = PHP_INT_MAX;
    
    do {
        $vessel = array_shift($vessels);
        if($total + $vessel <= $eggnog) {
            $used[] = $vessel;
            $min_used = min($min_used, minUsedContainers($total + $vessel, $vessels, $eggnog, $used));
            array_pop($used);
        }
    }
    while($vessels);
    return $min_used;
}
$min_used = minUsedContainers(0, $vessels, $eggnog);
$count = countEggnog(0, $vessels, $eggnog, [], $min_used);
echo "Part 2: $count\n";
