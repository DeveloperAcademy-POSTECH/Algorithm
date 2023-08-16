import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 벽_부수고_이동하기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        //시작점도 포함하므로
        if (N == 1 && M == 1) {
            bw.write("1");
            bw.close();
            return;
        }
        //dx dy
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};

        int[][] map = new int[N][M];
        int[][] count = new int[N][M];
        //벽을 부순 경우를 구별하기 위해
        boolean[][][] visited = new boolean[N][M][2];
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0,0,0});

        for(int i=0; i<N; i++){
            String input = br.readLine();
            for(int j=0; j<M; j++){
                map[i][j] = input.charAt(j)-'0';
            }
        }
        while (!queue.isEmpty()){
            int[] current = queue.poll();
            int curX = current[0];
            int curY = current[1];

            for(int i=0; i<4; i++){
                int nx = curX+dx[i];
                int ny = curY+dy[i];
                if(nx<0||ny<0||nx>=N||ny>=M){
                    continue;
                }
                //벽이 있다면
                if(map[nx][ny] == 1){
                    //벽을 부수지 않았고, 부수고 방문하지 않았으면
                    if(current[2] == 0 && !visited[nx][ny][1]){
                        visited[nx][ny][1] = true;
                        count[nx][ny] = count[curX][curY] +1;
                        queue.offer(new int[]{nx,ny,1});
                    }
                } else {
                    //방문한 적이 있는지 체크
                    if(!visited[nx][ny][current[2]]){
                        visited[nx][ny][current[2]] = true;
                        count[nx][ny] = count[curX][curY] +1;
                        queue.offer(new int[]{nx,ny,current[2]});
                    }
                }
                if(nx == N-1 && ny == M-1){
                    bw.write(String.valueOf(++count[nx][ny]));
                    bw.close();
                    System.exit(0);
                }
            }
        }
        bw.write("-1");
        bw.close();
    }
}
