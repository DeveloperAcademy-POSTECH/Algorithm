import java.util.ArrayList;
import java.util.Arrays;

public class 프로그래머스_주차_요금_계산 {
    public static void main(String[] args){
        Solution solution = new Solution();
        int fees[] = new int[]{
                180, 5000, 10, 600
        };
        String[] records = new String[]{
                "05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"
        };
        solution.solution(fees,records);
    }
    static class Solution {
        static int defaultTime;
        static int defaultFee;
        static int unitTime;
        static int unitFee;
        public int[] solution(int[] fees, String[] records) {
            //기본 시간
            defaultTime = fees[0];
            //기본 요금
            defaultFee = fees[1];
            //
            unitTime = fees[2];
            unitFee = fees[3];
            int[] parkTime = new int[10000];
            int[] totalTime = new int[10000];
            ArrayList<Integer> answer = new ArrayList<>();
            Arrays.fill(parkTime,-1);
            for(int i=0; i<records.length; i++){
                String[] record = records[i].split(" ");
                int time = timeToMinute(record[0]);
                int carNumber = Integer.parseInt(record[1]);
                boolean isIn = record[2].equals("IN");
                if(isIn){
                    parkTime[carNumber] = time;
                }else{
                    totalTime[carNumber]+= time-parkTime[carNumber];
                    parkTime[carNumber] = -1;
                }
            }
            //출차하지 않은 차량계산
            for(int carNum=0; carNum<10000; carNum++){
                //입차 시간이 존재 하는경우
                if(parkTime[carNum]!=-1) {
                    //23:59 -> 1439
                    totalTime[carNum]+=1439-parkTime[carNum];
                }
            }
            for(int time:totalTime){
                if(time!=0){
                    int totalFee=0;
                    totalFee+=defaultFee;
                    time-=defaultTime;
                    if(time>0){
                        totalFee += Math.ceil((double)time/unitTime)*unitFee;
                    }
                    answer.add(totalFee);
                }
            }

//            for(int fee: answer){
//                System.out.println(fee);
//            }
            return answer.stream().mapToInt(i -> i).toArray();
        }

        public int timeToMinute(String time){
            String[] temp = time.split(":");
            int hour = Integer.parseInt(temp[0]);
            int minute = Integer.parseInt(temp[1]);
            return hour*60+minute;
        }

    }
}
