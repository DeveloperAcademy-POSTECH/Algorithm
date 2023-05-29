import java.io.*;
import java.util.*;

public class 백준_17142_연구소 {
    static private int[][] map;
    static private int min = Integer.MAX_VALUE;
    static private int empty = 0;
    static private List<Virus> virusList;
    static private Virus[] activeVir;
    static private int[] dx = {0, 0, 1, -1};
    static private int[] dy = {1, -1, 0, 0};
    static private int n, m;

    static class Virus {
        int x;
        int y;
        int val;

        public Virus(int x, int y, int val) {
            this.x = x;
            this.y = y;
            this.val = val;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        //virus 를 놓을 수 있는 Point List
        virusList = new ArrayList<>();
        //map size
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        activeVir = new Virus[m];
        map = new int[n][n];


        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int temp = Integer.parseInt(st.nextToken());
                if (temp == 2)
                    virusList.add(new Virus(i, j, 0));
                else if (temp == 0)
                    empty++;
                map[i][j] = temp;

            }
        }
        if(empty==0)
            bw.write("0");
        else {
            combinationVirus(0, 0);
            bw.write(min == Integer.MAX_VALUE ? "-1" : String.valueOf(min));
        }
        bw.close();
        br.close();

    }
    //경우의 수 조합 선택
    static void combinationVirus(int start, int currentCnt) {
        if (currentCnt == m) {
            infection();
            return;
        }

        for (int i = start; i < virusList.size(); i++) {
            activeVir[currentCnt] = virusList.get(i);
            combinationVirus(i + 1, currentCnt + 1);
        }
    }

    //bfs virus infection
    static void infection() {
        boolean[][] infectedCell = new boolean[n][n];
        int remainCellCnt = empty;
        Queue<Virus> queue = new LinkedList<>();
        for (Virus v : activeVir) {
            queue.offer(v);
            infectedCell[v.x][v.y] = true;
        }
        while (!queue.isEmpty()) {
            Virus v = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = v.x + dx[i];
                int ny = v.y + dy[i];
                if(nx<0||ny<0||nx>=n||ny>=n)
                    continue;
                if(infectedCell[nx][ny] || map[nx][ny]== 1)
                    continue;
                if (map[nx][ny] == 0) {
                    remainCellCnt--;
                }

                if (remainCellCnt == 0) {
                    min = Math.min(min, v.val + 1);
                    return;
                }
                infectedCell[nx][ny] = true;
                Virus temp = new Virus(nx,ny,v.val+1);
                queue.offer(temp);
            }
        }

    }

}
