import java.io.*;
import java.util.StringTokenizer;

/**
 * @author : hyunwoopark
 * @version : 1.0.0
 * @package : ADA_Algorithm
 * @name : 빗물
 * @date : 10/29/23 6:19 PM
 * @modifyed : $
 **/

// 1번째 줄 2차원 세계의 세로길이 H, 가로길이 W
public class 빗물 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int result = 0;
        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int[][] matrix = new int[h][w];
        st = new StringTokenizer(br.readLine());
        //matrix에 세워진 벽을 기록한다.
        for (int i = 0; i < w; i++) {
            int height = Integer.parseInt(st.nextToken());
            for (int j = 0; j < height; j++) {
                matrix[j][i] = 1;
            }
        }

        for (int i = 0; i < h; i++) {
            boolean firstWall = false;
            int count = 0;
            for (int j = 0; j < w; j++) {
                int current = matrix[i][j];
                if (current == 1) {
                    if (firstWall == false) {
                        firstWall = true;
                    } else {
                        //첫번째 벽 이후 새로운 벽을 만난 경우
                        //count를 result에 더하고 초기화 한다.
                        result += count;
                        count = 0;
                    }
                } else {
                    //첫번째 벽이 세워진 경우
                    if (firstWall)
                        count++;
                }
            }
        }
        bw.write(String.valueOf(result));
        bw.close();
        br.close();
    }
}
