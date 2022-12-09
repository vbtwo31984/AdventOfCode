import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day1 {
    public static void main(String[] args) throws FileNotFoundException {
        List<Elf> elves = parseInput();
        elves.sort(Comparator.comparingInt(Elf::getTotalCalories).reversed());
        Optional<Elf> maxElf = elves.stream().findFirst();
        //noinspection OptionalGetWithoutIsPresent
        System.out.println("Maximum calories elf is: " + maxElf.get());
        int totalOfThreeElves = elves.stream()
                .limit(3)
                .map(Elf::getTotalCalories)
                .reduce(0, Integer::sum);
        System.out.println("Total calories of first 3 elves are: " + totalOfThreeElves);
    }

    private static List<Elf> parseInput() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("Year2022/src/day1.txt"));
        List<Elf> elves = new ArrayList<>();

        List<Integer> currentElfFood = new ArrayList<>();
        while(scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if(line.isEmpty()) {
                elves.add(new Elf(currentElfFood));
                currentElfFood = new ArrayList<>();
            }
            else {
                currentElfFood.add(Integer.parseInt(line));
            }
        }
        elves.add(new Elf(currentElfFood));
        return elves;
    }
}

class Elf {
    private final List<Integer> food;

    public Elf(List<Integer> food) {
        this.food = food;
    }

    public int getTotalCalories() {
        return food.stream().reduce(0, Integer::sum);
    }

    @Override
    public String toString() {
        return "Total: " + getTotalCalories() +
                " Food: " + food;
    }
}