
import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Part1 {

    public static void main(String[] args) {
        File inputFile;
        inputFile = new File("input.txt");

        try (Scanner reader = new Scanner(inputFile)) {
            while (reader.hasNextLine()) {
                String line = reader.nextLine();
                String[] allRanges = line.split(",");

                ArrayList<Long> invalids = new ArrayList<>();

                for (String range : allRanges) {
                    long[] rangeArr = Arrays.stream(range.split("-")).mapToLong(Long::parseLong).toArray();
                    for (long id = rangeArr[0]; id < rangeArr[1]; id++) {
                        String stringId = Long.toString(id);
                        int halfway = Math.floorDiv(stringId.length(), 2);

                        String firstHalf = stringId.substring(0, halfway);
                        String secondHalf = stringId.substring(halfway);

                        if (firstHalf == null ? secondHalf == null : firstHalf.equals(secondHalf)) {
                            invalids.add(id);
                        }

                    }
                }

                long ans = 0;

                for (long id : invalids) {
                    ans += id;
                }

                System.out.println(ans);

            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
