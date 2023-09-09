import java.io.*;
import java.util.StringTokenizer;

/**
 * @author : hyunwoopark
 * @version : 1.0.0
 * @package : ADA_Algorithm
 * @name : 빵집
 * @date : 2023/08/21 6:17 AM
 * @modifyed : $
 **/
public class 빵집 {
    static int n, m;
    static char[][] map;
    //우상, 우, 우하 (-1,1), (0,1), (1,1)
    static int[] dx = new int[]{-1, 0,1};
    static int[] dy = new int[]{1, 1,1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int ans = 0;
        map = new char[n][m];
        for (int i = 0; i < n; i++) {
            String row = br.readLine();
            for (int j = 0; j < m; j++) {
                map[i][j] = row.charAt(j);
            }
        }
        for (int i = 0; i < n; i++) {
            if (dfs(i, 0))
                ans++;
        }
        bw.write(String.valueOf(ans));
        bw.close();
        br.close();
    }

    public static boolean dfs(int x, int y) {
        if (y == m - 1)
            return true;
        char current = map[x][y];
        if (current == '.') {
            map[x][y] = '0';
            for (int i = 0; i < 3; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < n) {
                    if(dfs(nx, ny)){
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
