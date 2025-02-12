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
     * Complete the 'programmerStrings' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts STRING s as parameter.
     */

    public static int programmerStrings(String s) {
        // 왼쪽 검사
        int biggestLeftIndex = s.indexOf("p");

        if(s.indexOf("r") > biggestLeftIndex){
            biggestLeftIndex = s.indexOf("r");
        }
        if(s.indexOf("r",s.indexOf("r")+1) > biggestLeftIndex){
            biggestLeftIndex = s.indexOf("r",s.indexOf("r")+1);
        }
        if(s.indexOf("r",s.indexOf("r",s.indexOf("r")+1)+1) > biggestLeftIndex){
            biggestLeftIndex = s.indexOf("r",s.indexOf("r",s.indexOf("r")+1)+1);
        }
        if(s.indexOf("o") > biggestLeftIndex){
            biggestLeftIndex = s.indexOf("o");
        }
        if(s.indexOf("g") > biggestLeftIndex){
            biggestLeftIndex = s.indexOf("g");
        }
        if(s.indexOf("a") > biggestLeftIndex){
            biggestLeftIndex = s.indexOf("a");
        }
        if(s.indexOf("m") > biggestLeftIndex){
            biggestLeftIndex = s.indexOf("m");
        }
        if(s.indexOf("m",s.indexOf("m")+1) > biggestLeftIndex){
            biggestLeftIndex = s.indexOf("m",s.indexOf("m")+1);
        }
        if(s.indexOf("e") > biggestLeftIndex){
            biggestLeftIndex = s.indexOf("e");
        }

        // 오른쪽검사
        int smallestRightIndex = s.lastIndexOf("p");

        if(s.lastIndexOf("r") < smallestRightIndex){
            smallestRightIndex = s.lastIndexOf("r");
        }
        if(s.lastIndexOf("r",s.lastIndexOf("r")-1) < smallestRightIndex){
            smallestRightIndex = s.lastIndexOf("r",s.lastIndexOf("r")-1);
        }
        if(s.lastIndexOf("r",s.lastIndexOf("r",s.lastIndexOf("r")-1)-1) < smallestRightIndex){
            smallestRightIndex = s.lastIndexOf("r",s.lastIndexOf("r",s.lastIndexOf("r")-1)-1);
        }
        if(s.lastIndexOf("o") < smallestRightIndex){
            smallestRightIndex = s.lastIndexOf("o");
        }
        if(s.lastIndexOf("g") < smallestRightIndex){
            smallestRightIndex = s.lastIndexOf("g");
        }
        if(s.lastIndexOf("a") < smallestRightIndex){
            smallestRightIndex = s.lastIndexOf("a");
        }
        if(s.lastIndexOf("m") < smallestRightIndex){
            smallestRightIndex = s.lastIndexOf("m");
        }
        if(s.lastIndexOf("m",s.lastIndexOf("m")-1) < smallestRightIndex){
            smallestRightIndex = s.lastIndexOf("m",s.lastIndexOf("m")-1);
        }
        if(s.lastIndexOf("e") < smallestRightIndex){
            smallestRightIndex = s.indexOf("e");
        }
        return smallestRightIndex-biggestLeftIndex-1;
    }

}
public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        int result = Result.programmerStrings(s);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
