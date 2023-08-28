import java.io.*;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/**
 * @author : hyunwoopark
 * @version : 1.0.0
 * @package : ADA_Algorithm
 * @name : 아기상어
 * @date : 2023/08/21 12:53 AM
 * @modifyed : $
 **/
public class 아기상어 {
    public static int n;
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};
    public static int[] shark;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        int[][] map = new int[n][n];
        //init map
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 9) {
                    shark = new int[]{i, j};
                    map[i][j] = 0;
                }
            }
        }
        //상어 크기
        int size = 2;
        int eat = 0; // 먹은 물고기 수
        int move = 0; // 움직인 총 거리

        while (true) {
            PriorityQueue<int[]> queue = new PriorityQueue<>(
                    (o1, o2) -> {
                        //거리가 같지 않다면 거리 작은거 우선
                        if (o1[2] != o2[2]) {
                            return o1[2] - o2[2];
                            //x 좌표 작은거 우선
                        } else if (o1[0] != o2[0]) {
                            return o1[0] - o2[0];
                        } else {
                            //y좌표 작은거 우선
                            return o1[1] - o2[1];
                        }
                    }
            );
            boolean[][] visited = new boolean[n][n];

            queue.add(new int[]{shark[0], shark[1], 0}); // x(세로), y(가로), 거리
            visited[shark[0]][shark[1]] = true;

            boolean flag = false; // 상어가 먹이를 먹었는지 체크할 변수

            while (!queue.isEmpty()) {
                shark = queue.poll();

                if (map[shark[0]][shark[1]] != 0 && map[shark[0]][shark[1]] < size) {
                    map[shark[0]][shark[1]] = 0; // 물고기 갱신
                    eat++;
                    //움직인 거리 추가
                    move += shark[2];
                    //먹이 flag 변경
                    flag = true;
                    //먹이 먹으면 break
                    break;
                }

                for (int k = 0; k < 4; k++) {
                    int ny = shark[0] + dy[k];
                    int nx = shark[1] + dx[k];

                    if (ny < 0 || nx < 0 || nx >= n || ny >= n || visited[ny][nx] || map[ny][nx] > size) continue;

                    queue.add(new int[]{ny, nx, shark[2] + 1});
                    visited[ny][nx] = true;
                }
            }
            //먹은게 없으면 엄마 콜
            if (!flag)
                break;

            if (size == eat) {
                size++;
                eat = 0;
            }
        }

        bw.write(String.valueOf(move));
        bw.close();
        br.close();

    }
}
