public class PatternPermutations {
    public static int countPatternPermutations(String pattern) {
        // 문자열 패턴의 길이를 저장
        int n = pattern.length();

        // 방문한 알파벳을 체크하기 위한 배열
        boolean[] visited = new boolean[26];

        // 경우의 수를 저장할 변수
        int[] count = {0};

        // DFS 호출
        dfs(pattern, 0, visited, count);

        return count[0];
    }

    private static void dfs(String pattern, int index, boolean[] visited, int[] count) {
        // 기저 사례: 모든 문자에 대해 패턴을 결정한 경우
        if (index == pattern.length()) {
            count[0]++;
            return;
        }

        char ch = pattern.charAt(index);

        // 이미 방문한 알파벳이라면 다음 문자로 넘어감
        if (visited[ch - 'A']) {
            dfs(pattern, index + 1, visited, count);
        } else {
            // 방문하지 않은 알파벳이라면 경우의 수를 계산
            for (char c = 'A'; c <= 'Z'; c++) {
                visited[c - 'A'] = true;
                dfs(pattern, index + 1, visited, count);
                visited[c - 'A'] = false;
            }
        }
    }

    public static void main(String[] args) {
        String pattern = "ABA";
        int result = countPatternPermutations(pattern);
        System.out.println("경우의 수: " + result);
    }
}
