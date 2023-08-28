import java.io.*;
import java.util.StringTokenizer;

/**
 * @author : hyunwoopark
 * @version : 1.0.0
 * @package : ADA_Algorithm
 * @name : 직사각형나누기
 * @date : 2023/08/29 4:43 AM
 * @modifyed : $
 **/
public class 직사각형나누기 {
    static long maximum = Integer.MIN_VALUE;
    static int[][] map;
    static long[][] sum;
    static int row, cell;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        row = Integer.parseInt(st.nextToken());
        cell = Integer.parseInt(st.nextToken());
        map = new int[row][cell];
        for (int r = 0; r < row; r++) {
            String rowString = br.readLine();
            for (int c = 0; c < cell; c++) {
                map[r][c] = rowString.charAt(c) - '0';
            }
        }

        //누적합 구하기
        sum = new long[row][cell];
        sum[0][0] = map[0][0];
        for (int r = 1; r < row; r++)
            sum[r][0] = sum[r - 1][0] + map[r][0];
        for (int c = 1; c < cell; c++)
            sum[0][c] = sum[0][c - 1] + map[0][c];
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < cell; j++) {
                sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + map[i][j];
            }
        }

        //세로로 나누는 경우
        for (int p1 = 0; p1 < cell-2; p1++) {
            for(int p2=p1+1; p2<cell-1; p2++){
                long s1 = sum[row-1][p1];
                long s2 = sum[row-1][p2]-sum[row-1][p1];
                long s3 = sum[row-1][cell-1]-sum[row-1][p2];
                maximum = Math.max(maximum,s1*s2*s3);
            }
        }
        //가로로 나누는 경우
        for(int p1=0; p1 < row -2; p1++){
            for(int p2 = p1+1; p2<row-1; p2++){
                long s1 = sum[p1][cell-1];
                long s2 = sum[p2][cell-1]-sum[p1][cell-1];
                long s3 = sum[row-1][cell-1]-sum[p2][cell-1];
                maximum = Math.max(maximum,s1*s2*s3);
            }
        }
        //1번째
        for(int r=0; r<row-1; r++){
            for(int c=0; c<cell-1; c++){
                long s1 = sum[r][c];
                long s2 = sum[row-1][cell-1]-sum[row-1][c];
                long s3 = sum[row-1][c]-sum[r][c];
                maximum = Math.max(maximum,s1*s2*s3);
            }
        }

        //2번째
        for(int r=0; r<row-1; r++){
            for(int c=0; c<cell-1; c++){
                long s1 = sum[r][cell-1];
                long s2 = sum[row-1][c]-sum[r][c];
                long s3 = sum[row-1][cell-1]-s1-s2;
                maximum = Math.max(maximum,s1*s2*s3);
            }
        }
        //3번째
        for(int r=0; r<row-1; r++){
            for(int c=0; c<cell-1; c++){
                long s1 = sum[row-1][c];
                long s2 = sum[r][cell-1]-sum[r][c];
                long s3 = sum[row-1][cell-1]-s1-s2;
                maximum = Math.max(maximum,s1*s2*s3);
            }
        }
        //4번째
        for(int r=0; r<row-1; r++){
            for(int c=0; c<cell-1; c++){
                long s1 = sum[r][c];
                long s2 = sum[r][cell-1]-sum[r][c];
                long s3 = sum[row-1][cell-1]-s1-s2;
                maximum = Math.max(maximum,s1*s2*s3);
            }
        }
        bw.write(String.valueOf(maximum));
        bw.close();
        br.close();
    }

}
