<?php
$replacements = [];
$molecule = '';
$file = fopen('input.txt', 'r');
while ($line = fgets($file)) {
    $parts = explode(' => ', $line);
    if (count($parts) === 2) {
        $replacements[$parts[0]][] = trim($parts[1]);
    } elseif (strlen($line > 1)) $molecule = trim($line);
}

function getPossibleResults($molecule, $replacements)
{
    $possible_results = [];
    foreach ($replacements as $from => $to_arr) {
        foreach ($to_arr as $to) {
            $offset = 0;
            $length = strlen($from);
            $pos = strpos($molecule, $from, $offset);
            while ($pos !== false) {
                $possible_results[] = substr_replace($molecule, $to, $pos, $length);
                $offset = $pos + 1;
                $pos = strpos($molecule, $from, $offset);
            }
        }
    }
    $unique = array_unique($possible_results);
    return $unique;
}

$unique = getPossibleResults($molecule, $replacements);
$num = count($unique);
echo "Part 1: $num\n";

$file = file('input.txt', FILE_IGNORE_NEW_LINES);
$target = array_pop($file);
array_pop($file);

$repl = array_map(function($x) {return explode(' => ', $x);}, $file);
$z = 0;

while ($target != 'e')
	foreach ($repl as $r)
		if (($pos = strpos($target, $r[1])) !== false AND @++$z)
			$target = substr_replace($target, $r[0], $pos, strlen($r[1]));

echo "Part 2: $z\n";
