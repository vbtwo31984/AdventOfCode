<?php
namespace Year15\Day8;

class CodeString {
    private string $string;

    public function __construct(string $string) {
        $this->string = trim($string);
    }

    public function getLength(): int {
        return strlen($this->string);
    }

    public function getCodeLength(): int {
        return strlen($this->reduceString());
    }

    public function getEncodedLength(): int {
        return strlen($this->encodeString());
    }

    private function reduceString(): string {
        $string = preg_replace(
            ['/^"/', '/"$/', preg_quote('/\\\\/'), preg_quote('/\\"/'), '/\\\x[0-9a-f]{2}/'],
            ['', '', '\\', '"', '.'],
            $this->string
        );
        return $string;
    }

    private function encodeString(): string {
        $string = str_replace(['\\', '"'], ['\\\\', '\\"'], $this->string);
        return "\"$string\"";
    }
}