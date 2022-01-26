<?php
ini_set('memory_limit', '2g');
$packages = file('input.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
$packages = array_map('intval', $packages);
rsort($packages);

function createGroups($packages, $num_groups) {
    $total = array_sum($packages);
    $each_group = $total / $num_groups;

    $allGroups = [];
    $len = PHP_INT_MAX;
    createGroup($each_group, [], $packages, $len, $allGroups);
    return $allGroups;
}

function createGroup(int $total, array $current, array $packages, &$len, &$groups) {
    if(count($current) >= $len) return;
    $current_sum = array_sum($current);
    foreach($packages as $i=>$package) {
        if($current_sum + $package === $total) {
            $groups[] = array_merge($current, [$package]);
            $len = count($current)+1;
            return;
        }
        if($current_sum + $package < $total) {
            $left_packages = array_slice($packages, $i + 1);
            if($left_packages) {
                createGroup($total, array_merge($current, [$package]), $left_packages, $len, $groups);
            }
        }
    }
}

function getSmallestEntanglement($groups) {
    $smallest_group_count = count($groups[0]);
    $entanglements = [];
    foreach($groups as $group) {
        if(count($group) === $smallest_group_count) {
            $entanglements[] = array_product($group);
        }
    }
    return min($entanglements);
}

$groups = createGroups($packages, 3);
$min_entanglement = getSmallestEntanglement($groups);
echo "Part 1: $min_entanglement\n";

$groups = createGroups($packages, 4);
$min_entanglement = getSmallestEntanglement($groups);
echo "Part 2: $min_entanglement\n";

