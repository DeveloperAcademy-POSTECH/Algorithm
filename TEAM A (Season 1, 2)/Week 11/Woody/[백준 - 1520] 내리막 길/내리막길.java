import java.io.*;
import java.util.StringTokenizer;

/**
 * @author : hyunwoopark
 * @version : 1.0.0
 * @package : ADA_Algorithm
 * @name : 내리막길
 * @date : 2023/08/21 5:15 AM
 * @modifyed : $
 **/
public class 내리막길 {
    static int n,m;
    static int[][] map, dp;
    static int[] dx = new int[]{1,-1,0,0};
    static int[] dy = new int[]{0,0,-1,1};
    public static void main(String[] arg) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        dp = new int[n][m];
        for(int i=0; i<n; i++){
            st= new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
                dp[i][j] = -1;
            }
        }
        System.out.println(dfs(0,0));
    }
    public static int dfs(int x, int y){
        if(x==n-1&& y== m-1)
            return 1;
        else if(dp[x][y]!=-1)
            return dp[x][y];
        dp[x][y] = 0;
        for(int i=0; i<4; i++){
            int nx = x+ dx[i];
            int ny = y + dy[i];
            //범위 초과 및 가려는곳의 높이 체크
            if(nx<0||ny<0||nx==n||ny==m||map[x][y]<=map[nx][ny]){
                continue;
            }
            dp[x][y]+=dfs(nx,ny);
        }
        return dp[x][y];
    }

}
