import java.io.*;
import java.util.*;
public class 백준_1043_거짓말 {
    static private int N,M;
    //진실을 아는 사람
    static private int K;
    static private boolean[] knowPeople;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        K = Integer.parseInt(st.nextToken());
        if(K==0)
            bw.write(String.valueOf(M));
        else{
            knowPeople = new boolean[N];
            for(int i=0; i<K; i++){
                int personIdx = Integer.parseInt(st.nextToken());
                knowPeople[personIdx] = true;
            }

        }
    }
}
