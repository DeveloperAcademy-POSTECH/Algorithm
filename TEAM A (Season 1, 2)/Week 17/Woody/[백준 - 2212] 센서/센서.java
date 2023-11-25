import java.io.*;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

/**
 * @author : hyunwoopark
 * @version : 1.0.0
 * @package : ADA_Algorithm
 * @name : 센서
 * @date : 10/27/23 3:44 AM
 * @modifyed : $
 **/
public class 센서 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int result = 0;
        int n = Integer.parseInt(br.readLine());

        int k = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] sensors = new int[n];

        Integer[] diff = new Integer[n - 1];
        for (int i = 0; i < n; i++) {
            sensors[i] = Integer.parseInt(st.nextToken());
        }
        //각 센서 사이의 간격을 계산
        for (int i = 1; i < n; i++) {
            diff[i - 1] = sensors[i] - sensors[i - 1];
        }

        //내림차순 정렬을 해준다
        Arrays.sort(diff, Collections.reverseOrder());


        //가장 diff가 큰 k-1개를 제외하고 수를 더해준다
        for (int i = k - 1; i < n - 1; i++) {
            result += diff[i];
        }
        bw.write(String.valueOf(result));
        bw.close();
        br.close();

    }
}
