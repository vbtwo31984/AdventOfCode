<?php
$input = 'uqwqemis';
$password = '';
$index = 0;
$password2 = [];
$num1 = 0;
$num2 = 0;

while($num2 < 8) {
    $hash = md5("$input$index");
    if(str_starts_with($hash, '00000')) {
        if($num1 < 8)
            $password .= $hash[5];
        $num1++;

        $char6 = $hash[5];
        if(is_numeric($char6) && intval($char6 < 8) && !array_key_exists($char6, $password2)) {
            $password2[$char6] = $hash[6];
            $num2++;
        }
    }
    $index++;
}

echo "Part 1: $password\n";
ksort($password2);
$password2 = implode('', $password2);
echo "Part 2: $password2\n";