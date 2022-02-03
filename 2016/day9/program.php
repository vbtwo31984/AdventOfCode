<?php
function marker(string $str, int $pos): array {
    $pos_end = strpos($str, ')', $pos);
    $sub = substr($str, $pos, $pos_end - $pos);
    $matches = [];
    preg_match_all('/[\d]+/', $sub, $matches);
    return [
        'num_chars'=>intval($matches[0][0]),
        'repetitions'=>intval($matches[0][1]),
        'end_pos'=>$pos_end 
    ];
}

function decompress(string $str): string {
    $decompressed = '';
    $num_chars = 0;
    $num_repetitions = 0;

    $len = strlen($str);
    for($i = 0; $i < $len; $i++) {
        $char = $str[$i];
        if($char === '(') {
            $marker = marker($str, $i);
            $sub = substr($str, $marker['end_pos']+1, $marker['num_chars']);
            for($rep = $marker['repetitions']; $rep > 0; $rep--) {
                $decompressed .= $sub;
            }
            $i = $marker['end_pos'] + $marker['num_chars'];
        }
        else $decompressed .= $char;
    }

    return $decompressed;
}

$input = trim(file_get_contents('input.txt'));
$str = decompress($input);
$len = strlen($str);
echo "Part 1: $len\n";

function getDecompressedLength(string $str): int {
    $len = strlen($str);
    $total = 0;
    for($i = 0; $i < $len; $i++) {
        $char = $str[$i];
        if($char !== '(') $total++;
        else {
            $marker = marker($str, $i);
            $sub = substr($str, $marker['end_pos']+1, $marker['num_chars']);
            $sub_len = getDecompressedLength($sub);
            $total += $marker['repetitions'] * $sub_len;
            $i = $marker['end_pos'] + $marker['num_chars'];
        }
    }
    return $total;
}
$len = getDecompressedLength($input);
echo "Part 2: $len\n";