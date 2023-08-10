package BOJ._23_05_31;

import java.util.*;
public class 요세푸스_문제 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int K = scan.nextInt();

        List<Integer> list = new ArrayList<Integer>();
        Queue<Integer> q = new LinkedList<Integer>();

        for (int i = 1; i <= N; i++) {
            q.add(i);
        }

        int cnt = 0;
        while(!q.isEmpty()) {
            cnt++;
            int temp = q.poll();
            if(cnt % K == 0) {
                list.add(temp);
            } else{
                q.add(temp);
            }
        }
        System.out.println(list.toString().replace("[", "<").replace("]", ">"));
    }
}
