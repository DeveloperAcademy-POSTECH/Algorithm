/**
 * @package : ADA_Algorithm
 * @name : 행복유치원
 * @date : 11/9/23 4:27 AM
 * @author : hyunwoopark
 * @version : 1.0.0
 * @modifyed : $
 **/

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 행복유치원 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int answer = 0;
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] height = new int[n];
        for (int i = 0; i < n; i++) {
            height[i] = Integer.parseInt(st.nextToken());
        }
        List<Integer> diff = new ArrayList<>();
        for (int i = 0; i < n - 1; i++) {
            diff.add(height[i + 1] - height[i]);
        }
        diff.sort(Integer::compareTo);
        for (int i = 0; i < n - k; i++) {
            answer += diff.get(i);
        }
        bw.write(String.valueOf(answer));
        bw.close();
        br.close();
    }
    //ex 1 3 5 6 10
    //5 3
    //1 3 5 6 10
    //diff 는 각 2, 2, 1, 4
    //여기서 k개의 그룹으로 나눈다 했을때
    //가장 diff가 큰 k개를 뺄 수 있기 때문에
    //diff를 오름차순 정렬하고 이를 앞에서 부터 인덱스  부터 n-k-1 개 만큼 더해주면 답

}
