import java.io.*;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 줄세우기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        //정점의 개수
        int n = Integer.parseInt(st.nextToken());
        //간선의 개수
        int m = Integer.parseInt(st.nextToken());
        //그래프와 차수를 기록하기 위한 변수
        ArrayList<Integer>[] graph = new ArrayList[n+1];
        int[] degree = new int[n+1];
        //위상 정렬을 위한 Queue
        Queue<Integer> queue = new LinkedList<>();
        //graph init
        for(int i=0; i<=n; i++){
            graph[i] = new ArrayList<>();
        }
        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            //먼저 올 사람 번호
            int x = Integer.parseInt(st.nextToken());
            //나중에 올 사람 번호
            int y = Integer.parseInt(st.nextToken());
            graph[x].add(y);
            //degree ++
            degree[y]++;
        }
        for(int i=1; i<=n; i++){
            //차수가 0이면 offer
            if(degree[i]==0){
                queue.offer(i);
            }
        }
        while(!queue.isEmpty()){
            int temp = queue.poll();
            //temp 와 연결된 정점 degree --
            for(int i: graph[temp]){
                if(--degree[i]==0){
                    queue.offer(i);
                }
            }
            //result에 temp 추가
            sb.append(temp).append(" ");
        }
        bw.write(sb.toString());
        bw.close();
        br.close();
    }
}
