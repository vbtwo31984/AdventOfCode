import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class FileParser {
    public static List<String> readFile(String filename) throws IOException {
        return Files.readAllLines(Paths.get("Year2023/src/"+filename));
    }
}