<?php
$spells = [
    ['name'=>'missile', 'mp'=>53, 'dmg'=>4],
    ['name'=>'drain', 'mp'=>73, 'dmg'=>2, 'heal'=>2],
    ['name'=>'shield', 'mp'=>113, 'effect'=>['duration'=>6, 'armor'=>7]],
    ['name'=>'poison', 'mp'=>173, 'effect'=>['duration'=>6, 'dmg'=>3]],
    ['name'=>'recharge', 'mp'=>229, 'effect'=>['duration'=>5, 'mana'=>101]]
];

$player = ['hp'=>50, 'mp'=>500];
$boss = ['hp'=>51, 'dmg'=>9];

function removeExpiredEffects($effects) {
    return array_filter($effects, fn($effect)=>$effect['duration'] > 0); 
}

function runEffects(&$player, &$boss, &$effects) {
    foreach($effects as $name=>&$effect) {
        $effect['duration']--;
        switch($name) {
            case 'poison':
                $boss['hp'] -= $effect['dmg'];
                break;
            case 'recharge':
                $player['mp'] += $effect['mana'];
                break;
        }
    }
    $effects = removeExpiredEffects($effects);
}

function canCast($player, $effects, $spell) {
    if($spell['mp'] > $player['mp']) return false;
    if(array_key_exists($spell['name'], $effects)) return false;
    return true;
}

function castSpell(&$player, &$boss, &$effects, $spell) {
    $player['mp'] -= $spell['mp'];
    if(array_key_exists('dmg', $spell)) {
        $boss['hp'] -= $spell['dmg'];
    }
    if(array_key_exists('heal', $spell)) {
        $player['hp'] += $spell['heal'];
    }
    if(array_key_exists('effect', $spell)) {
        $effects[$spell['name']] = $spell['effect'];
    }
}

function checkWinLose($player, $boss) {
    if($player['hp'] <= 0) return 'lose';
    if($boss['hp'] <= 0) return 'win';
    return null;
}

function simulate($player, $boss, $spells, $min_mana) {
    $spell_names = array_map(fn($spell) => $spell['name'], $spells);
    echo implode('->', $spell_names);
    $totalMana = 0;
    $effects = [];
    foreach($spells as $spell) {
        // comment this out for part 1
        $player['hp']--;
        if(checkWinLose($player, $boss) === 'lose') {
            echo " - lose\n";
            return -1;
        }
        
        if($totalMana > $min_mana) {
            echo " - used more than $min_mana mana, aborting\n";
            return -1;
        }

        runEffects($player, $boss, $effects);
        if(checkWinLose($player, $boss) === 'win') {
            echo " - win with $totalMana mana used\n";
            return $totalMana;
        }
        if(!canCast($player, $effects, $spell)) {
            echo " - can't cast\n";
            return -1;
        }

        castSpell($player, $boss, $effects, $spell);
        $totalMana += $spell['mp'];
        runEffects($player, $boss, $effects);
        if(checkWinLose($player, $boss) === 'win') {
            echo " - win with $totalMana mana used\n";
            return $totalMana;
        }
        $armor = array_key_exists('shield', $effects) ? $effects['shield']['armor'] : 0;
        $dmg = max($boss['dmg'] - $armor, 0);
        $player['hp'] -= $dmg;
        if(checkWinLose($player, $boss) === 'lose') {
            echo " - lose\n";
            return -1;
        }
    }
    echo " - continue\n";
    return 0;
}

function play($player, $boss, $prevSpells, $spells, &$min_mana = PHP_INT_MAX) {
    foreach($spells as $spell) {
        $simulation = array_merge($prevSpells, [$spell]);
        $mana = simulate($player, $boss, $simulation, $min_mana);
        if($mana > 0) {
            $min_mana = min($min_mana, $mana);
        }
        elseif($mana === 0) {
            play($player, $boss, $simulation, $spells, $min_mana);
        }
    }
    return $min_mana;
}

$mana = play($player, $boss, [], $spells);
echo "Part 1: $mana\n";