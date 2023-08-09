public class 프로그래머스_양궁대회 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 5;
        int[] info = new int[]{2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0};
        int[] answer = solution.solution(n, info);
        for (int i : answer) {
            System.out.println(i);
        }
    }

    static class Solution {
        //점수차가 최대일때 라이언 배열
        static private int[] maxLionInfo = new int[11];
        static private int[] answer;
        static private int maxDiff = Integer.MIN_VALUE;

        public static int[] solution(int n, int[] info) {
            dfs(0, n, info);
            //라이언 패배
            if (maxDiff == -1) {
                answer = new int[1];
                answer[0] = -1;
            }
            return answer;
        }

        public static void dfs(int depth, int n, int[] info) {
           //화살 다 쏜 경우
            if (depth == n) {
                int diff = getDiff(info);
                //갱신
                //낮은 점수를 더많이 맞춘경우가 우선이기때문에 같은 경우도 교체
                if (maxDiff <= diff) {
                    maxDiff = diff;
                    //깊은 복사
                    answer = maxLionInfo.clone();
                }
                return;
            }
            //라이언이 1발만 더쏘면 점수를 얻으므로
            //과녁에 라이언이 어피치보다 더 많이 맞추면 break
            for (int i = 0; i < info.length && maxLionInfo[i] <= info[i]; i++) {
                maxLionInfo[i] += 1;
                dfs(depth + 1, n, info);
                maxLionInfo[i] -= 1;
            }
        }

        //점수차 구하기
        public static int getDiff(int[] info) {
            int apeachScore = 0;
            int lionScore = 0;
            for (int i = 0; i < maxLionInfo.length; i++) {
                // 둘 다 못 맞춘경우 continue
                if (info[i] == 0 && maxLionInfo[i] == 0)
                    continue;
                //어피치가 라이언이랑 같거나 많이 맞춘 경우
                if (info[i] >= maxLionInfo[i])
                    apeachScore += (10 - i);
                    //라이언이 어피치보다 많이 맞춘 경우
                else
                    lionScore += (10 - i);
            }

            int diff = lionScore - apeachScore;

            //diff 가 0보다 작거나 같으면 라이언이 이길 수 없으므로 -1 return
            return diff <= 0 ? -1 : diff;

        }
    }
}
