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
        int minMeetingRooms = 0; // 최소 미팅룸 변수
        int Ptr = 0; // 미팅룸 끝나는 시간을 계산하기 위한 포인터처럼 사용하는 변수

        List<Integer> startMeetings = new ArrayList<>(); // 미팅룸 대여 시작시간 빈 List생성
        List<Integer> endMeetings = new ArrayList<>(); // 미팅룸 대여 종료시간 빈 List생성

        for(int i=0; i<meetingTimings.size(); i++){
            startMeetings.add(meetingTimings.get(i).get(0)); // 대여 시작시간 List에 add
            endMeetings.add(meetingTimings.get(i).get(1)); // 대여 종료시간 List에 add
        }

        startMeetings.sort(Comparator.naturalOrder()); // 오름차순sorting
        endMeetings.sort(Comparator.naturalOrder()); // 오름차순sorting

        for (int i=0; i<startMeetings.size(); i++){
            if(startMeetings.get(i) >= endMeetings.get(Ptr)){ // 가장 빠른시간에 종료하는 미팅시간보다 시작시간이 나중인 경우
                Ptr++; // 이미 종료한 미팅룸이 있으므로 minMeetingRooms는 그대로두고, 다음 종료시간을 가리키도록 한다.
            }else{ // 가장 빠른시간에 종료하는 미팅시간보다 시작시간이 이른 경우, 빈 미팅룸이 없는 것으로 판단
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
