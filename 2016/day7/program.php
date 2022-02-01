<?php
$lines = file('input.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

function hasAbba(string $ip, int $pos): bool {
    return $ip[$pos] === $ip[$pos+3]
      && $ip[$pos+1] === $ip[$pos+2]
      && $ip[$pos] !== $ip[$pos+1];
}

function supportsTLS(string $ip): bool {
    $len = strlen($ip);
    $hypernet = false;
    $hasAbba = false;
    for($i = 0; $i < $len-3; $i++) {
        $char = $ip[$i];
        if($char === '[') $hypernet = true;
        if($char === ']') $hypernet = false;
        $abba = hasAbba($ip, $i);
        if($hypernet && $abba) return false;
        $hasAbba = $hasAbba || $abba;
    }
    return $hasAbba;
}

$ips_with_tls = array_filter($lines, 'supportsTLS');
$num = count($ips_with_tls);
echo "Part 1: $num\n";

function hasAba(string $ip, int $pos): bool {
    return $ip[$pos] === $ip[$pos+2]
      && $ip[$pos] !== $ip[$pos+1];
}
function getCorrespondingBab(string $aba): string {
    return $aba[1].$aba[0].$aba[1];
}

function supportsSSL(string $ip): bool {
    $len = strlen($ip);
    $hypernet = false;
    $aba = [];
    $bab = [];
    for($i = 0; $i < $len - 2; $i++) {
        $char = $ip[$i];
        if($char === '[') $hypernet = true;
        if($char === ']') $hypernet = false;
        if(hasAba($ip, $i)) {
            $aba_bab = substr($ip, $i, 3);
            if($hypernet) $bab[] = $aba_bab;
            else $aba[] = $aba_bab;
        }
    }
    foreach($aba as $aba_instance) {
        $bab_instance = getCorrespondingBab($aba_instance);
        if(in_array($bab_instance, $bab)) return true;
    }
    return false;
}
$ips_with_ssl = array_filter($lines, 'supportsSSL');
$num = count($ips_with_ssl);
echo "Part 2: $num\n";