import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Day9 {
    public static void main(String[] args) throws FileNotFoundException {
        int part1 = tailVisited(1);
        System.out.println("\nPart 1: " + part1);
        int part2 = tailVisited(9);
        System.out.println("Part 2: " + part2);
    }

    private static int tailVisited(int numTails) throws FileNotFoundException {
        int[][] positions = new int[numTails + 1][2];
        for (int i = 0; i <= numTails; i++)
            positions[i] = new int[] { 0, 0 };
        Set<String> visited = new HashSet<>();
        visited.add(getCoord(positions[numTails]));

        Scanner scanner = new Scanner(new File("Year2022/src/day9.txt"));
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            System.out.println();
            System.out.println(line);
            var parts = line.split(" ");
            int howMuch = Integer.parseInt(parts[1]);
            for (int i = 0; i < howMuch; i++) {
                positions[0] = moveHead(positions[0], parts[0]);
                for (int j = 1; j <= numTails; j++) {
                    positions[j] = moveTail(positions[j - 1], positions[j]);
                }
                System.out.println("Head: " + getCoord(positions[0]) + " Tail: " + getCoord(positions[numTails]));
                visited.add(getCoord(positions[numTails]));
            }
        }

        return visited.size();
    }

    private static int[] moveHead(int[] pos, String dir) {
        switch (dir) {
            case "R":
                pos[0]++;
                break;
            case "L":
                pos[0]--;
                break;
            case "U":
                pos[1]++;
                break;
            case "D":
                pos[1]--;
                break;
        }
        return pos;
    }

    private static int[] moveTail(int[] headPosition, int[] tailPosition) {
        if (headPosition[0] - tailPosition[0] >= 2) {
            tailPosition[0]++;
            if (tailPosition[1] < headPosition[1])
                tailPosition[1]++;
            if (tailPosition[1] > headPosition[1])
                tailPosition[1]--;
        }
        if (tailPosition[0] - headPosition[0] >= 2) {
            tailPosition[0]--;
            if (tailPosition[1] < headPosition[1])
                tailPosition[1]++;
            if (tailPosition[1] > headPosition[1])
                tailPosition[1]--;
        }
        if (headPosition[1] - tailPosition[1] >= 2) {
            tailPosition[1]++;
            if (tailPosition[0] < headPosition[0])
                tailPosition[0]++;
            if (tailPosition[0] > headPosition[0])
                tailPosition[0]--;
        }
        if (tailPosition[1] - headPosition[1] >= 2) {
            tailPosition[1]--;
            if (tailPosition[0] < headPosition[0])
                tailPosition[0]++;
            if (tailPosition[0] > headPosition[0])
                tailPosition[0]--;
        }
        return tailPosition;
    }

    private static String getCoord(int[] pos) {
        return String.format("%d:%d", pos[0], pos[1]);
    }
}
