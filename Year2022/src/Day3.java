import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.stream.Collectors;

public class Day3 {
    public static void main(String[] args) throws FileNotFoundException {
        List<String> lines = parseInput();
        List<Integer> priorities = lines.stream().map(Day3::findPriority).toList();
        int prioritiesSum = priorities.stream().reduce(0, Integer::sum);
        System.out.println("Priorities sum: " + prioritiesSum);

        List<List<String>> sublists = new ArrayList<>();
        int startIndex = 0;
        while (startIndex < lines.size()) {
            int endIndex = Math.min(startIndex + 3, lines.size());
            sublists.add(lines.subList(startIndex, endIndex));
            startIndex += 3;
        }
        int groupPrioritiesSum = sublists.stream().map(Day3::findPriorityOfGroup).reduce(0, Integer::sum);
        System.out.println("Priorities of groups: " + groupPrioritiesSum);
    }

    private static List<String> parseInput() throws FileNotFoundException {
        List<String> lines = new ArrayList<>();
        Scanner scanner = new Scanner(new File("Year2022/src/day3.txt"));
        while (scanner.hasNextLine()) {
            lines.add(scanner.nextLine());
        }
        return lines;
    }

    private static int findPriority(String line) {
        int length = line.length();
        String first = line.substring(0, length / 2);
        String second = line.substring(length / 2);

        Map<Character, Boolean> seenMap = new HashMap<>();
        for (char c : first.toCharArray()) {
            seenMap.put(c, true);
        }

        for (char c : second.toCharArray()) {
            if (seenMap.containsKey(c)) {
                int priority = findPriority(c);
                System.out.println("Char: " + c + " - Priority: " + priority);
                return priority;
            }
        }
        return 0;
    }

    private static int findPriorityOfGroup(List<String> groupLines) {
        List<Set<Character>> seenChars = new ArrayList<>();
        for (String line : groupLines) {
            Set<Character> charsSet = line.chars()
                .mapToObj(e -> (char) e).collect(Collectors.toSet());
            seenChars.add(charsSet);
        }
        Set<Character> set = seenChars.get(0);
        set.retainAll(seenChars.get(1));
        set.retainAll(seenChars.get(2));
        char c = set.iterator().next();
        int priority = findPriority(c);
        System.out.println("Char: " + c + " - Priority: " + priority);
        return priority;
    }

    private static int findPriority(char c) {
        if (c >= 'a' && c <= 'z') {
            return c - 'a' + 1;
        }
        return c - 'A' + 27;
    }
}