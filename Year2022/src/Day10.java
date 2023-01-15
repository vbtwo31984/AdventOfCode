import java.io.File;
import java.io.FileNotFoundException;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Day10 {
    public static void main(String[] args) throws FileNotFoundException {
        part1();
        part2();
    }

    private static void part1() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("Year2022/src/day10.txt"));

        int cycle = 1;
        int register = 1;
        int signalStrengths = 0;
        LinkedList<Integer> interestedCycles = new LinkedList<>(List.of(20, 60, 100, 140, 180, 220));

        int currentInterestedCycle = interestedCycles.remove(0);
        while (cycle < currentInterestedCycle) {
            String line = scanner.nextLine();
            if (line.equalsIgnoreCase("noop")) {
                cycle++;
            } else {
                int add = Integer.parseInt(line.substring(5));
                register += add;
                cycle += 2;
            }
            if (currentInterestedCycle - cycle <= 1) {
                signalStrengths += currentInterestedCycle * register;
                if (interestedCycles.size() > 0) {
                    currentInterestedCycle = interestedCycles.remove(0);
                } else
                    break;
            }
        }
        System.out.println("Part 1: " + signalStrengths);
    }

    private static void part2() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("Year2022/src/day10.txt"));

        int cycle = 0;
        int register = 1;

        while (scanner.hasNextLine()) {
            print(register, cycle);

            String line = scanner.nextLine();
            if (line.equalsIgnoreCase("noop")) {
                cycle++;
            } else {
                int add = Integer.parseInt(line.substring(5));
                print(register, cycle + 1);
                register += add;
                cycle += 2;
            }
        }
    }

    private static void print(int register, int cycle) {
        if (cycle % 40 == 0)
            System.out.println();
        if (Math.abs(register - cycle % 40) <= 1) {
            System.out.print("🁢");
        } else {
            System.out.print(" ");
        }
    }
}
