/**
 * @package : ADA_Algorithm
 * @name : 세친구
 * @date : 11/9/23 6:04 AM
 * @author : hyunwoopark
 * @version : 1.0.0
 * @modifyed : $
 **/

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 세친구 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        int answer = Integer.MAX_VALUE;
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        List<Integer>[] friends = new List[n];
        for (int i = 0; i < n; i++) {
            friends[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x, y;
            x = Integer.parseInt(st.nextToken()) - 1;
            y = Integer.parseInt(st.nextToken()) - 1;
            friends[x].add(y);
            friends[y].add(x);
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (!friends[i].contains(j))
                    continue;
                for (int k = j + 1; k < n; k++) {
                    if (!(friends[k].contains(i) && friends[k].contains(j)))
                        continue;
                    int sum = friends[i].size() + friends[j].size() + friends[k].size() - 6;
                    answer = Math.min(sum, answer);
                }
            }
        }
        if (answer == Integer.MAX_VALUE)
            answer = -1;
        bw.write(String.valueOf(answer));
        bw.close();
        br.close();

    }
}
