import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;


class Result {

    /*
     * Complete the 'countWaysToColorHouses' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER n as parameter.
     */

    public static int countWaysToColorHouses(int n) {
        int[][]ways = new int[n][3];
        int totalWays = 0;

        ways[0][0]=1;
        ways[0][1]=1;
        ways[0][2]=1;

        for(int i=0;i<n-1; i++){
            ways[i+1][0] = ways[i][1] + ways[i][2];
            ways[i+1][1] = ways[i][0] + ways[i][2];
            ways[i+1][2] = ways[i][0] + ways[i][1];
        }

        totalWays = ways[n-1][0] + ways[n-1][1] + ways[n-1][2];

        return totalWays;
    }
}
public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        int result = Result.countWaysToColorHouses(n);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
