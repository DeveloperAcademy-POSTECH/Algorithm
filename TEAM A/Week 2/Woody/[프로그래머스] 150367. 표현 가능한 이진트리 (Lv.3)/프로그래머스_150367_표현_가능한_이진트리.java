public class 프로그래머스_150367_표현_가능한_이진트리 {
    public static void  main(String[] args){
        long[] input = new long[]{7,42,5};
        new Solution().solution(input);

    }
    static class Solution {
        public int[] solution(long[] numbers) {
            int[] answer = new int[numbers.length];

            for(int i=0; i<numbers.length; i++){
                long temp = numbers[i];
                System.out.println(getBinary(temp));
                answer[i] = isValid(getBinary(temp))?1:0;
            }
            return answer;
        }
        private String getBinary(long number){
            String temp = Long.toBinaryString(number);
            StringBuilder sb = new StringBuilder();
            int cnt=1;
            int depth=1;
            while(temp.length()>cnt){
                depth <<=1;
                cnt += depth;
            }
            int offset = cnt-temp.length();
            for(int i=0; i<offset; i++){
                sb.append("0");
            }
            return sb.append(temp).toString();
        }
        private boolean isValid(String binary) {
            int length = binary.length();
            if (binary.length() == 0)
                return true;
            int root = length / 2;
            String left = binary.substring(0, root);
            String right = binary.substring(root + 1);

            if (binary.charAt(root) == '0') {
                return isBlank(left) && isBlank(right);
            }

            return isValid(left) && isValid(right);
        }
        private boolean isBlank(String binary) {
            int length = binary.length();
            if (binary.length() == 0)
                return true;
            int root = length / 2;
            String left = binary.substring(0, root);
            String right = binary.substring(root + 1);

            if (binary.charAt(root) == '1') {
                return false;
            }
            return isBlank(left) && isBlank(right);
        }
    }
}
