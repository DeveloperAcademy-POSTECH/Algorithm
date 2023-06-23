package BOJ._23_06_16;

import java.util.*;
import java.io.*;

public class 랜선_자르기_1654 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        long result = 0;
        long max = 0;

        long [] arr= new long[K];
        for(int i=0; i<K; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            max = Math.max(max, arr[i]);
        }

        result = binarySearch(arr, N, max);

        System.out.println(result);
        br.close();
    }

    public static long binarySearch(long[] arr, int target, long max) {
        long half = 0;
        long min = 1;

        while(min <= max) {
            half = (min + max)/2;
            long count = 0;

            for(long num : arr) {
                count += num / half;
            }

            if(count < target) {
                max = half-1;
            }

            else {
                min = half+1;
            }
        }
        return (max+min)/2;
    }

}
