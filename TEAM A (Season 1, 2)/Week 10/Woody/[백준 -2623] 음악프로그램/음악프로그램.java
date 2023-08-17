import java.io.*;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 음악프로그램 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        //가수의 수
        int n = Integer.parseInt(st.nextToken());
        //PD의 수
        int m = Integer.parseInt(st.nextToken());

        //Graph
        ArrayList<Integer>[] graph = new ArrayList[n + 1];
        //queue for Topology Sort
        Queue<Integer> queue = new LinkedList<>();
        //node degree
        int[] degree = new int[n + 1];
        int resultCnt = 0;
        //Init Graph
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int len = Integer.parseInt(st.nextToken());
            int temp = 0;
            for (int j = 0; j < len; j++) {
                int num = Integer.parseInt(st.nextToken());
                if (j == 0) {
                    temp = num;
                    continue;
                }
                graph[temp].add(num);
                degree[num]++;
                temp = num;
            }
        }
        for (int i = 1; i <= n; i++) {
            if (degree[i] == 0)
                queue.offer(i);
        }
        while (!queue.isEmpty()) {
            int num = queue.poll();
            for (int i : graph[num]) {
                if (--degree[i] == 0) {
                    queue.offer(i);
                }
            }
            resultCnt++;
            sb.append(num).append("\n");
        }
        if(resultCnt!=n)
            bw.write("0");
        else
            bw.write(sb.toString());
        bw.close();
        br.close();

    }
}
