<?php
namespace Year15\Day5;

class StringChecker {
    private static $naughtySubstrings = 'ab|cd|pq|xy';
    public static function isStringNicePart1(string $string): bool {
        return self::containsThreeVowels($string)
            && self::containsDoubleLetter($string)
            && !self::containsNaughtySubstring($string);
    }

    private static function containsThreeVowels(string $string): bool {
        $numMatches = preg_match_all('/[aeiou]/', $string);
        return $numMatches >= 3;
    }

    private static function containsDoubleLetter(string $string): bool {
        $containsDoubleLetter = preg_match('/(.)\1/', $string);
        return $containsDoubleLetter === 1;
    }

    private static function containsNaughtySubstring(string $string): bool {
        $naughty = self::$naughtySubstrings;
        $containsNaughtySubstring = preg_match("/$naughty/", $string);
        return $containsNaughtySubstring === 1;
    }

    public static function isStringNicePart2(string $string): bool {
        return self::containsDoublePair($string)
            && self::containsRepeatingLetter($string);
    }

    private static function containsDoublePair(string $string): bool {
        $containsDoublePair = preg_match('/(..).*\1/', $string);
        return $containsDoublePair === 1;
    }

    private static function containsRepeatingLetter(string $string): bool {
        $containsRepeatingLetter = preg_match('/(.).\1/', $string);
        return $containsRepeatingLetter === 1;
    }
}