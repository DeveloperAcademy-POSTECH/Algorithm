package BOJ._23_05_31;

import java.util.*;
import java.io.*;

public class 숫자_정사각형 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int M = scan.nextInt();
        int[][] arr = new int[N][M];

        int flag = N < M ? N : M;
        int max = 1;

        for (int i = 0; i < N; i++) {
            String str = scan.next();
            for (int j = 0; j < M; j++) {
                arr[i][j] = str.charAt(j) - '0';
            }
        }

        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                for(int k=0; k<flag; k++) {
                    if(i+k < N && j+k < M) {
                        if(arr[i][j] == arr[i][j+k] && arr[i][j] == arr[i+k][j] && arr[i][j] == arr[i+k][j+k]) {
                            max = max > k+1 ? max : k+1;
                        }
                    }
                }
            }
        }

        System.out.println(max * max);
    }
}