import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day5 {
    public static void main(String[] args) throws FileNotFoundException {
        Stack<Character>[] stacks = parseStacks();
        System.out.println("Stacks at beginning");
        for(Stack<Character> stack : stacks) {
            System.out.println(stack);
        }

        List<List<Integer>> moves = parseMoves();
        System.out.println("Moves: " + moves);

        for(List<Integer> move : moves) {
            int howMany = move.get(0);
            int from = move.get(1) - 1;
            int to = move.get(2) - 1;
            for(int i = 0; i < howMany; i++) {
                char c = stacks[from].pop();
                stacks[to].push(c);
            }
        }

        System.out.print("Tops of stacks part 1: ");
        for(Stack<Character> stack : stacks) {
            System.out.print(stack.peek());
        }
        System.out.println();

        stacks = parseStacks();
        for(List<Integer> move : moves) {
            int howMany = move.get(0);
            int from = move.get(1) - 1;
            int to = move.get(2) - 1;
            Stack<Character> tempStack = new Stack<>();
            for(int i = 0; i < howMany; i++) {
                char c = stacks[from].pop();
                tempStack.push(c);
            }
            Collections.reverse(tempStack);
            stacks[to].addAll(tempStack);
        }

        System.out.print("Tops of stacks part 2: ");
        for(Stack<Character> stack : stacks) {
            System.out.print(stack.peek());
        }
        System.out.println();
    }

    private static Stack<Character>[] parseStacks() throws FileNotFoundException {
        int numStacks = 9;
        Stack<Character>[] stacks = new Stack[numStacks];
        for(int i = 0; i < numStacks; i++) {
            stacks[i] = new Stack<>();
        }

        Scanner scanner = new Scanner(new File("Year2022/src/day5.txt"));
        String line = scanner.nextLine();
        while(line.charAt(1) != '1') {
            for(int i = 0; i < numStacks; i++) {
                int start = i * 4 + 1;
                if(start < line.length()) {
                    char crate = line.charAt(start);
                    if (crate != ' ') {
                        stacks[i].push(crate);
                    }
                }
            }

            line = scanner.nextLine();
        }

        for(int i = 0; i < numStacks; i++) {
            Collections.reverse(stacks[i]);
        }

        return stacks;
    }

    private static List<List<Integer>> parseMoves() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("Year2022/src/day5.txt"));
        List<List<Integer>> moves = new ArrayList<>();
        while(scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if(line.startsWith("move")) {
                List<Integer> parts = Arrays.stream(line.split("\\D+")).filter(part -> !part.isEmpty()).map(Integer::parseInt).toList();
                moves.add(parts);
            }
        }
        return moves;
    }
}
