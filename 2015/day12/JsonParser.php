<?php
namespace Year15\Day12;

class JsonParser {
    public function __construct(private string $json) {}

    public function getNumbers(): array {
        return $this->getNumbersImpl($this->json);
    }

    private function getNumbersImpl(string $json) {
        $matches = [];
        preg_match_all('/-?[0-9]+/', $json, $matches);
        $numbers = array_map('intval', $matches[0]);
        return $numbers;
    }

    public function getNonRedNumbers(): array {
        $json = json_decode($this->json, true);
        $no_red = $this->removeRed($json);
        return $this->getNumbersImpl(json_encode($no_red));
    }

    private function removeRed(array $arr) {
        $newArr = [];
        foreach($arr as $k=>$v) {
            if(!is_int($k) && $v === 'red') return [];
            if(is_array($v)) {
                $newArr[$k] = $this->removeRed($v);
            }
            else $newArr[$k] = $v;
        }
        return $newArr;
    }
}