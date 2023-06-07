import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 백준_2342_Dance_Dance_Revolution {

    static int[][] cost = {
            {0, 2, 2, 2, 2},
            {3, 1, 3, 4, 3},
            {3, 3, 1, 3, 4},
            {3, 4, 3, 1, 3},
            {3, 3, 4, 3, 1}
    };

    static int[][][] dp = new int[5][5][5];
    static List<Integer> path = new ArrayList<>();
    static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            int temp = Integer.parseInt(st.nextToken());
            path.add(temp);
        }
        dp = new int[path.size()-1][5][5];
        result = findOptimalCost(0,0,0);
        bw.write(String.valueOf(result));
        bw.close();
        br.close();
    }

    static public int findOptimalCost(int leftFootPosition, int rightFootPosition, int currentIdx) {
        int currentPad = path.get(currentIdx);
        if (currentPad == 0) {
            return 0;
        }
        if (dp[currentIdx][leftFootPosition][rightFootPosition] != 0) {
            return dp[currentIdx][leftFootPosition][rightFootPosition];
        }
        return dp[currentIdx][leftFootPosition][rightFootPosition] = Math.min(
                findOptimalCost(currentPad, rightFootPosition, currentIdx + 1) + cost[leftFootPosition][currentPad],
                findOptimalCost(leftFootPosition, currentPad, currentIdx + 1) + cost[rightFootPosition][currentPad]
        );
    }

}
