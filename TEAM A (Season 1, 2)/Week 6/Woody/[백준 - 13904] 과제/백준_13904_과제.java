import java.io.*;
import java.util.*;

public class 백준_13904_과제 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        List<Work> works = new ArrayList<>();
        int max = 0;
        int result = 0;
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            int remainDays = Integer.parseInt(st.nextToken());
            int score = Integer.parseInt(st.nextToken());
            works.add(new Work(remainDays,score));
            max = Math.max(max,remainDays);
        }
        for(int i=max; i>0; i--){
            Work temp = new Work(0,0);
            for(Work w: works){
                if(w.remainDays >= i && w.score> temp.score)
                    temp = w;
            }
            result += temp.score;
            works.remove(temp);
        }
        System.out.println(result);
    }
    static class Work{
        int remainDays;
        int score;
        Work(int remainDays, int score){
            this.remainDays = remainDays;
            this.score = score;
        }
    }
}
