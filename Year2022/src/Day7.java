import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day7 {
    public static void main(String[] args) {

    }

    private static FileSystemNode parseInput() throws FileNotFoundException {
        Scanner scanner = new Scanner(new java.io.File("Year2022/src/day7.txt"));
        Directory root = new Directory("/", null);
        Directory current = root;

        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (line.equals("$ cd /")) {
                current = root;
            } else if (line.equals("$ cd ..")) {
                current = (Directory) current.parent();
            } else if (line.startsWith("$ cd")) {
                String newDir = line.substring(5);
                current = current.findChild(newDir);
            } else if (!line.equals("$ ls")) {
                String[] parts = line.split(" ");
                if (parts[0].equals("dir")) {
                    Directory newDir = new Directory(parts[1], current);
                    current.addChild(newDir);
                }
                else {
                    int size = Integer.parseInt(parts[0]);
                    File newFile = new File(parts[1], size, current);
                    current.addChild(newFile);
                }
            }
        }

        return root;
    }
}

interface FileSystemNode {
    int size();

    void addChild(FileSystemNode child);

    FileSystemNode parent();

    String name();
}

class Directory implements FileSystemNode {
    private int calculatedSize = 0;
    private final List<FileSystemNode> children = new ArrayList<>();
    private final FileSystemNode parent;
    private final String name;

    public Directory(String name, FileSystemNode parent) {
        this.name = name;
        this.parent = parent;
    }

    @Override
    public int size() {
        if (calculatedSize == 0) {
            calculatedSize = children.stream().mapToInt(FileSystemNode::size).sum();
        }
        return calculatedSize;
    }

    @Override
    public void addChild(FileSystemNode child) {
        children.add(child);
    }

    @Override
    public FileSystemNode parent() {
        return parent;
    }

    @Override
    public String name() {
        return name;
    }

    public Directory findChild(String child) {
        return (Directory) children.stream()
            .filter(c -> c.getClass() == Directory.class && c.name().equals(child))
            .findFirst().orElseThrow();
    }
}

record File(String name, int size, FileSystemNode parent) implements FileSystemNode {
    @Override
    public void addChild(FileSystemNode child) {
    }
}