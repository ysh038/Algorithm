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
     * Complete the 'findLargestSquareSize' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY samples as parameter.
     */

    public static int findLargestSquareSize(List<List<Integer>> samples) {
        int largestSize = 0;

        for(int i=1; i<samples.size(); i++){
            for(int j=1; j<samples.size(); j++){
                if(samples.get(i).get(j) == 1){ // 현재 인덱스의 값이 1일 때
                    int left = samples.get(i).get(j-1); // 현재 인덱스 왼쪽 값
                    int up = samples.get(i-1).get(j); //  현재 인덱스 위쪽 값
                    int leftUp = samples.get(i-1).get(j-1); // 현재 인덱스 왼쪽 위 값

                    int min = Math.min(left,Math.min(up, leftUp)); // 왼쪽,위,왼쪽위 값 중 최소값

                    samples.get(i).set(j, min+1);
                    // 최소값에 1을 더함
                    // 최소값이 0이라면 (왼쪽, 위, 왼쪽 위 중 0이 있다면) 그대로 1을 유지하도록 한다
                    // 전부 1이라면 크기 2의 정사각형이므로, 현재 인덱스 값을 2로 바꾼다.
                    // 전부 2라면 크기 3의 정사각형이므로, 현재 인덱스 값을 3으로 바꾼다.
                    // 마찬가지로 반복할 수 있도록 한다.

                    largestSize = Math.max(largestSize,min+1);
                }
            }
        }

        return largestSize;
    }

}
public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int samplesRows = Integer.parseInt(bufferedReader.readLine().trim());
        int samplesColumns = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<Integer>> samples = new ArrayList<>();

        IntStream.range(0, samplesRows).forEach(i -> {
            try {
                samples.add(
                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                .map(Integer::parseInt)
                                .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int result = Result.findLargestSquareSize(samples);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
