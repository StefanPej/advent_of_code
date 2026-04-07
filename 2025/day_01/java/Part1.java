
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Part1 {

    public static void main(String[] args) {
        File inputFile;
        inputFile = new File("input.txt");

        ArrayList<String> input = new ArrayList<>();

        try (Scanner reader = new Scanner(inputFile)) {
            while (reader.hasNextLine()) {
                String line = reader.nextLine();
                input.add(line);

            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        int dial = 50;
        int ans = 0;

        for (int i = 0; i < input.size(); i++) {
            String instruction = input.get(i);
            char direction = instruction.charAt(0);
            int amount = Integer.parseInt(instruction.substring(1));

            if (direction == 'L') {
                dial -= amount;
            }
            if (direction == 'R') {
                dial += amount;
            }

            dial = dial % 100;

            if (dial == 0) {
                ans += 1;
            }
        }

        System.out.println(ans);
    }

}
