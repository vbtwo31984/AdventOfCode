import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Day2 {
    private static final Map<String, String> winnerMap = Map.of(
            "X", "C",
            "Y", "A",
            "Z", "B"
    );
    private static final Map<String, String> equalMap = Map.of(
            "X", "A",
            "Y", "B",
            "Z", "C"
    );
    private static final Map<String, Integer> scores = Map.of(
            "X", 1,
            "Y", 2,
            "Z", 3
    );
    private static final Map<String, Map<String, String>> playMap = Map.of(
            "X", Map.of("A", "Z", "B", "X", "C", "Y"),
            "Y", Map.of("A", "X", "B", "Y", "C", "Z"),
            "Z", Map.of("A", "Y", "B", "Z", "C", "X")
    );
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("Year2022/src/day2.txt"));
        int totalScore = 0;
        int totalScore2 = 0;
        while(scanner.hasNextLine()) {
            String line = scanner.nextLine();
            totalScore += getLineScore(line);
            totalScore2 += getLineScore2(line);
        }
        System.out.println("Total score: " + totalScore);
        System.out.println("Total score 2: " + totalScore2);
    }

    private static int getLineScore(String line) {
        String[] parts = line.split(" ");
        int score = scores.get(parts[1]);
        if(winnerMap.get(parts[1]).equals(parts[0])) {
            score += 6;
        }
        else if(equalMap.get(parts[1]).equals(parts[0])) {
            score += 3;
        }
        return score;
    }

    private static int getLineScore2(String line) {
        String[] parts = line.split(" ");
        String myPlay = playMap.get(parts[1]).get(parts[0]);
        return getLineScore(parts[0] + " " + myPlay);
    }
}
