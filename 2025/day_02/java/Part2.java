
import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Part2 {

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
                    for (long id = rangeArr[0]; id < rangeArr[1] + 1; id++) {
                        String stringId = Long.toString(id);

                        for (int idx = 1; idx < stringId.length(); idx++) {

                            int amtTimes = Math.floorDiv(stringId.length(), idx);

                            String substring = stringId.substring(0, idx);

                            StringBuilder newString = new StringBuilder();

                            for (int j = 0; j < amtTimes; j++) {
                                newString.append(substring);
                            }

                            if (newString.toString().equals(stringId)) {
                                invalids.add(id);
                                break;
                            }

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
