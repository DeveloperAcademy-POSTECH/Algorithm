package BOJ._23_06_10;

import java.util.*;

public class 부녀회장이_될테야_2775 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        int[][] arr = new int[15][15];

        for (int i = 1; i <= 14; i++) {
            arr[0][i] = i;
        }

        for (int i = 1; i <= 14; i++) {
            for (int j = 1; j <= 14; j++) {
                arr[i][j] = arr[i][j-1] + arr[i-1][j];
            }
        }

        for (int i = 0; i < t; i++) {
            int k = scan.nextInt();
            int n = scan.nextInt();
            System.out.println(arr[k][n]);
        }
    }
}
