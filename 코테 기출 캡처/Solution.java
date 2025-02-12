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
     * Complete the 'getMinRooms' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY meetingTimings as parameter.
     */

    public static int getMinRooms(List<List<Integer>> meetingTimings) {
        int minMeetingRooms = 0;
        int Ptr = 0;

        List<Integer> startMeetings = new ArrayList<>();
        List<Integer> endMeetings = new ArrayList<>();

        for(int i=0; i<meetingTimings.size(); i++){
            startMeetings.add(meetingTimings.get(i).get(0));
            endMeetings.add(meetingTimings.get(i).get(1));
        }

        startMeetings.sort(Comparator.naturalOrder());
        endMeetings.sort(Comparator.naturalOrder());

        for (int i=0; i<startMeetings.size(); i++){
            if(startMeetings.get(i) >= endMeetings.get(Ptr)){
                Ptr++;
            }else{
                minMeetingRooms++;
            }
        }
        return minMeetingRooms;
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int meetingTimingsRows = Integer.parseInt(bufferedReader.readLine().trim());
        int meetingTimingsColumns = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<Integer>> meetingTimings = new ArrayList<>();

        IntStream.range(0, meetingTimingsRows).forEach(i -> {
            try {
                meetingTimings.add(
                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                .map(Integer::parseInt)
                                .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int result = Result.getMinRooms(meetingTimings);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
