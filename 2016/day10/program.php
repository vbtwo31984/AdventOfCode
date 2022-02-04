<?php
$bots = [];
$file = fopen('input.txt', 'r');
while($line = fgets($file)) {
    $matches = [];
    if(str_starts_with($line, 'value')) {
        preg_match_all('/[\d]+/', $line, $matches);
        $val = intval($matches[0][0]);
        $bot = intval($matches[0][1]);
        
        $bots[$bot]['values'][] = $val;
    }
    else {
        preg_match('/bot ([\d]+) gives low to ([a-z]+) ([\d]+) and high to ([a-z]+) ([\d]+)/', $line, $matches);
        $giver = intval($matches[1]);
        $low_type = $matches[2];
        $low_to = intval($matches[3]);
        $high_type = $matches[4];
        $high_to = intval($matches[5]);

        $bots[$giver]['low'] = ['type'=>$low_type, 'to'=>$low_to];
        $bots[$giver]['high'] = ['type'=>$high_type, 'to'=>$high_to];
        if(!array_key_exists('values', $bots[$giver])) $bots[$giver]['values'] = [];
    }
}

function full(array $bot): bool {
    return !notFull($bot);
}

function notFull(array $bot): bool {
    return count($bot['values']) < 2;
}

$outputs = [];
$fullBots = array_filter($bots, 'full');
while(count($fullBots) < count($bots)) {
    foreach($fullBots as $bot) {
        $low = min($bot['values']);
        $high = max($bot['values']);

        $low_type = $bot['low']['type'];
        $low_to = $bot['low']['to'];

        $high_type = $bot['high']['type'];
        $high_to = $bot['high']['to'];

        if($low_type === 'bot' && !in_array($low, $bots[$low_to]['values'])) {
            $bots[$low_to]['values'][] = $low;
        }
        if($high_type === 'bot' && !in_array($high, $bots[$high_to]['values'])) {
            $bots[$high_to]['values'][] = $high;
        }
        if($low_type === 'output') $outputs[$low_to] = $low;
        if($high_type === 'output') $outputs[$high_to] = $high;
    }
    $fullBots = array_filter($bots, 'full');
}

function is61and17bot($bot) {
    return in_array(61, $bot['values']) && in_array(17, $bot['values']);
}

$goodBot = 0;
foreach($bots as $i=>$bot) {
    if(is61and17bot($bot)) {
        $goodBot = $i;
        break;
    }
}

echo "Part 1: $goodBot\n";
$product = $outputs[0] * $outputs[1] * $outputs[2];
echo "Part 2: $product\n";