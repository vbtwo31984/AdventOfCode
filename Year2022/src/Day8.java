import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.File;

public class Day8 {
    public static void main(String[] args) throws FileNotFoundException {
        int cols = 99;
        int rows = 99;
        // int cols = 5;
        // int rows = 5;
        int[][] matrix = parseInput(cols, rows);
        char[][] visible = new char[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (i == 0 || i == rows - 1 || j == 0 || j == cols - 1) {
                    visible[i][j] = 'y';
                } else {
                    visible[i][j] = 'n';
                }
            }
        }

        for (int col = 1; col < cols - 1; col++) {
            int maxValue = matrix[0][col];
            for (int row = 1; row < rows - 1; row++) {
                if (matrix[row][col] > maxValue) {
                    visible[row][col] = 'y';
                    maxValue = matrix[row][col];
                }
            }

            maxValue = matrix[rows - 1][col];
            for (int row = rows - 2; row > 0; row--) {
                if (matrix[row][col] > maxValue) {
                    visible[row][col] = 'y';
                    maxValue = matrix[row][col];
                }
            }
        }
        for (int row = 1; row < rows - 1; row++) {
            int maxValue = matrix[row][0];
            for (int col = 1; col < cols - 1; col++) {
                if (matrix[row][col] > maxValue) {
                    visible[row][col] = 'y';
                    maxValue = matrix[row][col];
                }
            }

            maxValue = matrix[row][cols - 1];
            for (int col = cols - 2; col > 0; col--) {
                if (matrix[row][col] > maxValue) {
                    visible[row][col] = 'y';
                    maxValue = matrix[row][col];
                }
            }
        }

        print(visible);

        int numVisible = 0;
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (visible[row][col] == 'y') {
                    numVisible++;
                }
            }
        }
        System.out.println("Number visible: " + numVisible);

        int maxScenicScore = 0;
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                maxScenicScore = Integer.max(maxScenicScore, calculateScenicScore(matrix,
                        row, col));
            }
        }
        System.out.println("Max scenic score: " + maxScenicScore);
    }

    private static int calculateScenicScore(int[][] matrix, int row, int col) {
        int left = 0, right = 0, up = 0, down = 0;

        int val = matrix[row][col];

        // up
        for (int i = row - 1; i >= 0; i--) {
            int curTreeVal = matrix[i][col];
            up++;
            if (curTreeVal >= val)
                break;
        }
        // down
        for (int i = row + 1; i < matrix.length; i++) {
            int curTreeVal = matrix[i][col];
            down++;
            if (curTreeVal >= val)
                break;
        }
        // left
        for (int i = col - 1; i >= 0; i--) {
            int curTreeVal = matrix[row][i];
            left++;
            if (curTreeVal >= val)
                break;
        }
        // right
        for (int i = col + 1; i < matrix[row].length; i++) {
            int curTreeVal = matrix[row][i];
            right++;
            if (curTreeVal >= val)
                break;
        }

        return up * down * left * right;
    }

    private static int[][] parseInput(int cols, int rows) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("Year2022/src/day8.txt"));
        int[][] matrix = new int[rows][cols];
        int row = 0;
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            for (int col = 0; col < cols; col++) {
                matrix[row][col] = line.charAt(col) - '0';
                System.out.print(matrix[row][col]);
            }
            row++;
            System.out.println();
        }
        return matrix;
    }

    private static void print(char[][] matrix) {
        System.out.println();
        for (char[] chars : matrix) {
            for (char aChar : chars) {
                System.out.print(aChar);
            }
            System.out.println();
        }
    }
}
