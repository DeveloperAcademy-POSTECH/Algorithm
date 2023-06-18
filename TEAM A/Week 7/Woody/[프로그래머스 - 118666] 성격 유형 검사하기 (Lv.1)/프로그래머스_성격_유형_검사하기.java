public class 프로그래머스_성격_유형_검사하기 {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }

    class Solution {
        static final int[] scores = new int[]{0, -3, -2, -1, 0, 1, 2, 3};

        public String solution(String[] survey, int[] choices) {
            StringBuilder sb = new StringBuilder();
            int[] result = new int[4];
            for (int i = 0; i < survey.length; i++) {
                char c1 = survey[i].charAt(0);
                char c2 = survey[i].charAt(1);
                int type = getType(c1);
                int choice = choices[i];
                if(c1>c2){
                    result[type] -= scores[choice];
                }else{
                    result[type] += scores[choice];
                }
            }
            //
            sb.append(result[0]<1? "R":"T");
            sb.append(result[1]<1? "C":"F");
            sb.append(result[2]<1? "J":"M");
            sb.append(result[3]<1? "A":"N");

            return sb.toString();
        }
        // 성격 유형 타입 분류
        public int getType(char c) {
            switch (c) {
                case 'R', 'T': {
                    return 0;
                }
                case 'C', 'F': {
                    return 1;
                }
                case 'J', 'M': {
                    return 2;
                }
                case 'A', 'N': {
                    return 3;
                }
                default: {
                    return -1;
                }
            }
        }
    }
}
