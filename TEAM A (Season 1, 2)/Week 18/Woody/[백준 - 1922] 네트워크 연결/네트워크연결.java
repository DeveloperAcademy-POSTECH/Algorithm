import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

/**
 * @author : hyunwoopark
 * @version : 1.0.0
 * @package : ADA_Algorithm
 * @name : 네트워크연결
 * @date : 10/31/23 2:33 AM
 * @modifyed : $
 **/
public class 네트워크연결 {
    static class Edge implements Comparable<Edge> {
        int start;
        int end;
        int weight;

        public Edge(int start, int end, int weight) {
            this.start = start;
            this.end = end;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge o) {
            return this.weight - o.weight;
        }
    }

    static int[] parent;
    static ArrayList<Edge> edgeList;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int answer = 0;
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        edgeList = new ArrayList<>();
        parent = new int[n + 1];

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            edgeList.add(new Edge(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            ));
        }
        for (int i = 1; i < n + 1; i++) {
            parent[i] = i;
        }
        edgeList.sort(Edge::compareTo);
        for (Edge edge : edgeList) {
            int start = edge.start;
            int end = edge.end;
            if (find(start) != find(end)) {
                answer += edge.weight;
                union(start, end);
            }
        }
        bw.write(String.valueOf(answer));
        bw.close();
        br.close();
    }

    public static int find(int x) {
        if (x == parent[x]) {
            return x;
        }

        return parent[x] = find(parent[x]);
    }

    public static void union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x != y) {
            parent[y] = x;
        }
    }
}
