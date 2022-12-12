import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Day4 {
    public static void main(String[] args) throws FileNotFoundException {
        List<List<List<Integer>>> pairs = parseInput();

        long fullyContained = pairs.stream().filter(Day4::fullyContained).count();
        System.out.println("Fully contained pairs: " + fullyContained);

        long overlapping = pairs.stream().filter(Day4::isOverlap).count();
        System.out.println("Overlapping pairs: " + overlapping);
    }

    private static List<List<List<Integer>>> parseInput() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("Year2022/src/day4.txt"));
        List<List<List<Integer>>> pairs = new ArrayList<>();

        while(scanner.hasNextLine()) {
            String line = scanner.nextLine();
            String[] linePairs = line.split(",");
            List<Integer> first = Arrays.stream(linePairs[0].split("-")).map(Integer::parseInt).toList();
            List<Integer> second = Arrays.stream(linePairs[1].split("-")).map(Integer::parseInt).toList();
            pairs.add(List.of(first, second));
        }

        return pairs;
    }

    private static boolean fullyContained(List<List<Integer>> pair) {
        if(pair.get(0).get(0) <= pair.get(1).get(0) && pair.get(0).get(1) >= pair.get(1).get(1))
            return true;
        if(pair.get(1).get(0) <= pair.get(0).get(0) && pair.get(1).get(1) >= pair.get(0).get(1))
            return true;
        return false;
    }

    private static boolean isOverlap(List<List<Integer>> pair) {
        System.out.print(pair);
        if(pair.get(0).get(0) <= pair.get(1).get(0) && pair.get(0).get(1) >= pair.get(1).get(0)) {
            return true;
        }
        if(pair.get(1).get(0) <= pair.get(0).get(0) && pair.get(1).get(1) >= pair.get(0).get(0)) {
            return true;
        }
        return false;
    }
}
