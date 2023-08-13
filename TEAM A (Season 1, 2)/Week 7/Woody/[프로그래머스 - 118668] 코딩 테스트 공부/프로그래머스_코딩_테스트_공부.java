import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class 프로그래머스_코딩_테스트_공부 {
    public static void main(String[] args) {
        Solution solution = new Solution();
//        int ans1 = solution.solution(10, 10, new int[][]{
//                {10, 15, 2, 1, 2},
//                {20, 20, 3, 3, 4}
//        });
        int ans2 = solution.solution(0, 0, new int[][]{{0,0,2,1,2},{4,5,3,1,2},{4,11,4,0,2},{10,4,0,4,2}});
//        System.out.println("ans1: "+ ans1);
        System.out.println("ans2: "+ ans2);
    }

    static class Solution {
        //알고력, 코딩력에 도달하는 최소시간 dp
        int dp[][];

        public int solution(int alp, int cop, int[][] problems) {
            int answer = 0;
            int alpMax = 0;
            int copMax = 0;
            //알고력, 코딩력 Max 구하기
            for (int[] problem : problems) {
                alpMax = Math.max(alpMax, problem[0]);
                copMax = Math.max(copMax, problem[1]);
            }

            dp = new int[alpMax + 1][copMax + 1];

            alp = Math.min(alp,alpMax);
            cop = Math.min(cop,copMax);
            for (int i = 0; i < alpMax + 1; i++) {
                for (int j = 0; j < copMax + 1; j++)
                    dp[i][j] = 1000000;
            }
            dp[alp][cop] = 0;
            for (int i = alp; i <= alpMax; i++) {
                for (int j = cop; j <= copMax; j++) {
                    //알고력 공부 1시간
                    if(i+1 <= alpMax)
                        dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j] + 1);
                    //코딩력 공부 1시간
                    if(j+1 <= copMax)
                        dp[i][j + 1] = Math.min(dp[i][j + 1], dp[i][j] + 1);

                    for (int[] problem : problems) {
                        int alp_req = problem[0];
                        int cop_req = problem[1];
                        int alp_rwd = problem[2];
                        int cop_rwd = problem[3];
                        int cost = problem[4];
                        if (alp_req<=i && cop_req<=j) {
                            //prevent index out of range
                            int tempAlp = Math.min(i + alp_rwd, alpMax);
                            int tempCop = Math.min(j + cop_rwd, copMax);
                            dp[tempAlp][tempCop] = Math.min(dp[tempAlp][tempCop], dp[i][j] + cost);
                        }
                    }
                }
            }


            return dp[alpMax][copMax];
        }
    }
}
