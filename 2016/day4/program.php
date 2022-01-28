<?php
$rooms = [];
$file = fopen('input.txt', 'r');
while($line = fgets($file)) {
    $matches = [];
    preg_match('/([a-z-]+)-([0-9]+)\[([a-z]+)]/', $line, $matches);
    $rooms[] = [
        'code'=>str_replace('-', ' ', $matches[1]),
        'sector'=>intval($matches[2]),
        'checksum'=>$matches[3]
    ];
}

function calculateCharacters($code) {
    $num = [];
    for($i = 0; $i < strlen($code); $i++) {
        $char = $code[$i];
        if($char !== ' ') {
            if(array_key_exists($char, $num)) $num[$char]++;
            else $num[$char] = 1;
        }
    }
    return $num;
}

function calculateChecksum($code) {
    $num_characters = calculateCharacters($code);
    arsort($num_characters);
    $len = current($num_characters);
    $checksum = '';
    $current = [];
    foreach($num_characters as $char=>$count) {
        if($len === $count) {
            $current[] = $char;
        }
        else {
            sort($current);
            $checksum .= implode('', $current);
            $len = $count;
            $current = [$char];
        }
    }
    sort($current);
    $checksum .= implode('', $current);

    return substr($checksum, 0, 5);
}

function isReal($room) {
    return $room['checksum'] === calculateChecksum($room['code']);
}

$real_rooms = array_filter($rooms, 'isReal');
$sectors = array_map(fn($room) => $room['sector'], $real_rooms);
$sum = array_sum($sectors);
echo "Part 1: $sum\n";

function rotate($char, $num) {
    if($char === ' ') return ' ';
    $ord = ord($char);
    $ord = ($ord + $num%26);
    if($ord > ord('z'))
        $ord -= 26;
    return chr($ord);
}

function decipherRoomName($room) {
    $name = '';
    for($i = 0; $i < strlen($room['code']); $i++) {
        $name.=rotate($room['code'][$i], $room['sector']);
    }
    $room['name'] = $name;
    return $room;
}
$deciphered_rooms = array_map('decipherRoomName', $real_rooms);
$filtered_room = array_filter($deciphered_rooms, fn($room) => strpos($room['name'], 'northpole') === 0);
foreach($filtered_room as $room) {
    echo "Part 2: {$room['name']} - {$room['sector']}\n";
}