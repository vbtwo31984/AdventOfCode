<?php
function say(string $number): string {
    $result = '';
    $num = 0;
    $length = strlen($number);
    for($i = 0; $i < $length; $i++) {
        $char = $number[$i];
        $num++;
        if($i === $length - 1 || $number[$i + 1] !== $char) {
            $result.="$num$char";
            $num = 0;
        }
    }
    return $result;
}

$number = '1113122113';
for($i = 0; $i < 40; $i++) {
    $number = say($number);
}
$length = strlen($number);
echo "Part 1: $length\n";

$number = '1113122113';
for($i = 0; $i < 50; $i++) {
    $number = say($number);
}
$length = strlen($number);
echo "Part 2: $length\n";