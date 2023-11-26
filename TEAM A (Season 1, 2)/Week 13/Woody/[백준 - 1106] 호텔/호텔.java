import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * @author : hyunwoopark
 * @version : 1.0.0
 * @package : ADA_Algorithm
 * @name : 호텔
 * @date : 2023/09/05 1:09 AM
 * @modifyed : $
 **/
public class 호텔 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int[] dp = new int[c + 101];
        Arrays.fill(dp, 100001);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int cost = Integer.parseInt(st.nextToken());
            int people = Integer.parseInt(st.nextToken());
            for(int j=people; j<c+101; j++){
                dp[j]=Math.min(dp[j],cost+dp[j-people]);
            }
        }
        System.out.println(dp[c]);
    }
}
