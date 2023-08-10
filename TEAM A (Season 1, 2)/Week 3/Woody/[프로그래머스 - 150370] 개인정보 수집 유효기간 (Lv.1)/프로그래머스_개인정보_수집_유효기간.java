import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 프로그래머스_개인정보_수집_유효기간 {
    public static void main(String[] args){
        Solution solution = new Solution();
        String today = "2022.05.19";
        String[] terms = new String[]{"A 6", "B 12", "C 3"};
        String[] pricacies = new String[]{"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"};
        int[] result = solution.solution(today,terms,pricacies);
        for(int i:result)
            System.out.println(i);
    }
    static class Solution {
        public int[] solution(String today, String[] terms, String[] privacies) {
            List<Integer> answer = new ArrayList<>();
            int[] termDay = new int[26];
            long todayLong = calDayLong(today);
            for(String term: terms){
                StringTokenizer st = new StringTokenizer(term);
                int type = st.nextToken().charAt(0)-'A';
                int day = Integer.parseInt(st.nextToken())*28;
                termDay[type] = day;
            }
            for(int i=0; i<privacies.length; i++){
                StringTokenizer st = new StringTokenizer(privacies[i]);
                long dayLong = calDayLong(st.nextToken());
                int type = st.nextToken().charAt(0)-'A';
                long limitDay = dayLong+termDay[type];
                if(limitDay<=todayLong)
                    answer.add(i+1);
            }
            return answer.stream().mapToInt(i->i).toArray();
        }
        public long calDayLong(String date){
            StringTokenizer st = new StringTokenizer(date,".");
            long dayLong = (Long.parseLong(st.nextToken())-2000)*12*28
                    + Long.parseLong(st.nextToken())*28
                    + Long.parseLong(st.nextToken());
            return dayLong;
        }
    }
}
