package BOJ._23_06_17;

import java.util.*;
import java.io.*;

public class 나무_자르기_2805 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];

        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        Arrays.sort(arr);
        System.out.println(binarySearch(arr, M));
        br.close();
    }

    public static long binarySearch(int[] arr, long M) {
        long mid = 0;
        long min = 0;
        long max = arr[arr.length - 1];
        while(min <= max) {
            long sum = 0;

            for(long tree : arr) {
                if(tree >= mid) {
                    sum += tree - mid;
                }
            }

            if(sum >= M) {
                min = mid + 1;
            }
            else {
                max = mid - 1;
            }
            mid = (max + min)/2;

        }

        return mid;
    }
}
