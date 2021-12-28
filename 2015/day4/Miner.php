<?php
namespace Year15\Day4;

class Miner {
    public function __construct(private string $input) {}

    public function mineNumber($numberOfZeroes): int {
        $number = 1;
        while(!$this->hashStartsWithZeroes($number, $numberOfZeroes)) {
            $number++;
        }
        return $number;
    }

    private function hashStartsWithZeroes(int $number, int $numberOfZeroes): bool {
        $hash = md5("{$this->input}$number");
        return $this->checkHashStartsWithFiveZeroes($hash, $numberOfZeroes);
    }

    private function checkHashStartsWithFiveZeroes(string $hash, int $numberOfZeroes): bool {
        for($i = 0; $i < $numberOfZeroes; $i++) {
            if($hash[$i] !== '0') {
                return false;
            }
        }
        return true;
    }
}