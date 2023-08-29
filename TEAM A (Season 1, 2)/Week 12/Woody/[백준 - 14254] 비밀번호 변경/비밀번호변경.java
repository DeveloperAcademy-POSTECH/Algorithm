import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

/**
 * @author : hyunwoopark
 * @version : 1.0.0
 * @package : ADA_Algorithm
 * @name : 비밀번호변경
 * @date : 2023/08/29 7:00 AM
 * @modifyed : $
 **/
public class 비밀번호변경 {


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out    ));
        String str = br.readLine();
        int k = Integer.parseInt(br.readLine());

        int answer = 0;
        int gap = str.length()-k;

        for (int i = 0; i < gap; i++) {
            int sum = 0;
            int max = 0;
            int[] cnt = new int[26];

            for (int j = i; j < str.length(); j+=gap) {
                sum++;
                max = Math.max(max, ++cnt[str.charAt(j)-'a']);
            }

            answer += sum-max;
        }

        bw.write(String.valueOf(answer));
        bw.close();
    }

}
