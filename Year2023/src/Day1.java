import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.OptionalInt;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class Day1 {
    public static void main(String[] args) throws IOException {
        List<String> lines = FileParser.readFile("Day1.txt");
        int sum1 = lines.stream().mapToInt(Day1::extractCalibrationValue).sum();
        System.out.println(sum1);

        int sum2 = lines.stream().mapToInt(Day1::alphanumericCalibrationValue).sum();
        System.out.println(sum2);
    }

    private static int extractCalibrationValue(String input) {
        String digits = input.replaceAll("[^0-9]", "");
        String value = String.valueOf(digits.charAt(0)) + digits.charAt(digits.length() - 1);
        return Integer.parseInt(value);
    }

    private static int alphanumericCalibrationValue(final String input) {
        Map<String, Integer> DIGIT_WORDS = Map.of(
                "one", 1,
                "two", 2,
                "three", 3,
                "four", 4,
                "five", 5,
                "six", 6,
                "seven", 7,
                "eight", 8,
                "nine", 9
        );


        // create dictionary with both string and digit representations of 1-9.
        final Map<String, Integer> compositeDigitMap = new HashMap<>();
        compositeDigitMap.putAll(DIGIT_WORDS);
        compositeDigitMap.putAll(DIGIT_WORDS.entrySet()
                .stream()
                .collect(Collectors.toMap(digit -> String.valueOf(digit.getValue()), Map.Entry::getValue)));

        return (firstOccurrence(input, compositeDigitMap) * 10) + lastOccurrence(input, compositeDigitMap);
    }

    private static int firstOccurrence(final String input, final Map<String, Integer> dictionary) {
        for (int i = 0, j = 1; j <= input.length(); j++) {
            OptionalInt digit = findDigitMatch(input.substring(i, j), dictionary);
            if (digit.isPresent()) {
                return digit.getAsInt();
            }
        }

        throw new IllegalArgumentException("First occurrence not found within " + input);
    }

    private static int lastOccurrence(final String input, final Map<String, Integer> dictionary) {
        for (int i = input.length(), j = input.length() - 1; j >= 0; j--) {
            OptionalInt digit = findDigitMatch(input.substring(j, i), dictionary);
            if (digit.isPresent()) {
                return digit.getAsInt();
            }
        }

        throw new IllegalArgumentException("Last occurrence not found within " + input);
    }

    private static OptionalInt findDigitMatch(final String input, final Map<String, Integer> dictionary) {
        return dictionary.entrySet().stream().filter(key -> input.contains(key.getKey())).mapToInt(Map.Entry::getValue).findFirst();
    }
}