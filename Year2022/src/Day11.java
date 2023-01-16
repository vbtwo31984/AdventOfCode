import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Day11 {
    public static void main(String[] args) {
        List<Monkey> monkeys = generateInputMonkeys();

        for (int round = 0; round < 10000; round++) {
            for (Monkey monkey : monkeys) {
                monkey.takeTurn(monkeys);
            }
        }

        long monkeyBusiness = monkeys.stream()
                .map(m -> m.getNumInspected())
                .sorted(Comparator.reverseOrder())
                .limit(2)
                .reduce(1l, (a, b) -> a * b);

        System.out.println("Part 1: " + monkeyBusiness);
    }

    private static List<Monkey> generateSampleMonkeys() {
        return List.of(
                new Monkey(List.of(79l, 98l), i -> i * 19, i -> i % 23 == 0, 2, 3),
                new Monkey(List.of(54l, 65l, 75l, 74l), i -> i + 6, i -> i % 19 == 0, 2, 0),
                new Monkey(List.of(79l, 60l, 97l), i -> i * i, i -> i % 13 == 0, 1, 3),
                new Monkey(List.of(74l), i -> i + 3, i -> i % 17 == 0, 0, 1));
    }

    private static List<Monkey> generateInputMonkeys() {
        return List.of(
                new Monkey(List.of(56l, 56l, 92l, 65l, 71l, 61l, 79l),
                        i -> i * 7, i -> i % 3 == 0, 3, 7),
                new Monkey(List.of(61l, 85l),
                        i -> i + 5, i -> i % 11 == 0, 6, 4),
                new Monkey(List.of(54l, 96l, 82l, 78l, 69l),
                        i -> i * i, i -> i % 7 == 0, 0, 7),
                new Monkey(List.of(57l, 59l, 65l, 95l),
                        i -> i + 4, i -> i % 2 == 0, 5, 1),
                new Monkey(List.of(62l, 67l, 80l),
                        i -> i * 17, i -> i % 19 == 0, 2, 6),
                new Monkey(List.of(91l),
                        i -> i + 7, i -> i % 5 == 0, 1, 4),
                new Monkey(List.of(79l, 83l, 64l, 52l, 77l, 56l, 63l, 92l),
                        i -> i + 6, i -> i % 17 == 0, 2, 0),
                new Monkey(List.of(50l, 97l, 76l, 96l, 80l, 56l),
                        i -> i + 3, i -> i % 13 == 0, 3, 5));
    }
}

class Monkey {
    private Queue<Long> items;
    private Operateable operation;
    private Testable test;
    private int trueResult;
    private int falseResult;
    private long inspected = 0;
    private int toMod = 3 * 11 * 7 * 2 * 19 * 5 * 17 * 13;

    public Monkey(List<Long> items, Operateable operation, Testable test, int trueResult, int falseResult) {
        this.items = new LinkedList<>(items);
        this.operation = operation;
        this.test = test;
        this.trueResult = trueResult;
        this.falseResult = falseResult;
    }

    public void catchItem(Long item) {
        items.add(item);
    }

    public void takeTurn(List<Monkey> monkeys) {
        inspected += items.size();
        while (!items.isEmpty()) {
            long item = items.remove();
            item = operation.operate(item) % toMod;
            if (test.test(item)) {
                monkeys.get(trueResult).catchItem(item);
            } else {
                monkeys.get(falseResult).catchItem(item);
            }
        }
    }

    public long getNumInspected() {
        return inspected;
    }
}

interface Operateable {
    public long operate(Long item);
}

interface Testable {
    public boolean test(Long item);
}
