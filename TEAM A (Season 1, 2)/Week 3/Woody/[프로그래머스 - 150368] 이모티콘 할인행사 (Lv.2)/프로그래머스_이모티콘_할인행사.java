public class 프로그래머스_이모티콘_할인행사 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] users = new int[][]{
                {40, 10000}, {25, 10000}
        };
        int[] emoticons = {7000, 9000};
        for (int i : solution.solution(users, emoticons)) {
            System.out.println(i);
        }
    }

    static class Solution {
        static int[] discount = {10, 20, 30, 40};
        static int maxSubscribe;
        static int maxCost;

        public int[] solution(int[][] users, int[] emoticons) {
            dfs(0, new int[emoticons.length], users, emoticons);
            return new int[]{maxSubscribe, maxCost};
        }

        public void dfs(int index, int[] discounts, int[][] users, int[] emoticons) {
            if (index == emoticons.length) {
                int subscribe = 0;
                int totalCost = 0;

                for (int[] user : users) {
                    int userDesireRatio = user[0];
                    int userSubscribeCost = user[1];
                    int sum = 0;
                    for (int i = 0; i < emoticons.length; i++) {
                        if (discounts[i] >= userDesireRatio) {
                            sum += emoticons[i] * (100 - discounts[i]) / 100;
                        }
                    }
                    if (sum >= userSubscribeCost)
                        subscribe++;
                    else
                        totalCost += sum;
                }
                if (subscribe > maxSubscribe) {
                    maxSubscribe = subscribe;
                    maxCost = totalCost;
                } else if (subscribe == maxSubscribe) {
                    maxCost = Math.max(maxCost, totalCost);
                }
                return;
            }
            for (int i = 0; i < 4; i++) {
                discounts[index] = discount[i];
                dfs(index + 1, discounts, users, emoticons);
            }
        }
    }

}
