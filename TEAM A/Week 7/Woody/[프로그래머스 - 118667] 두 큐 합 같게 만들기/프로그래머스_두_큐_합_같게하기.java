import java.util.Queue;
import java.util.LinkedList;

public class 프로그래머스_두_큐_합_같게하기 {
    public static void main(String[] args) {

    }

    class Solution {
        public int solution(int[] queue1, int[] queue2) {
            Queue<Integer> q1 = new LinkedList<>();
            Queue<Integer> q2 = new LinkedList<>();
            long sum1 = 0;
            long sum2 = 0;
            int max=0;
            int count = 0;
            for (int num : queue1) {
                q1.offer(num);
                sum1 += num;
                max = Math.max(max,num);
            }
            for (int num : queue2) {
                q2.offer(num);
                sum2 += num;
                max = Math.max(max,num);
            }
            if((sum1+sum2)%2==1||(sum1+sum2-max)<max)
                return -1;
            int i=0;
            while(i<300000){
                if(sum1>sum2){
                    int temp = q1.poll();
                    q2.offer(temp);
                    sum2+=temp;
                    sum1-=temp;
                    count++;
                }else if(sum1<sum2){
                    int temp = q2.poll();
                    q1.offer(temp);
                    sum1+=temp;
                    sum2-=temp;
                    count++;
                }else
                    return count;
                i++;
            }
            return -1;
        }
    }
}
