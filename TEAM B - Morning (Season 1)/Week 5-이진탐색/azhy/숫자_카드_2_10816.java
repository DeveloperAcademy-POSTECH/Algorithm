package BOJ._23_06_15;

import java.util.*;
import java.io.*;

public class 숫자_카드_2_10816 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int N = in.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = in.nextInt();
        }
        Arrays.sort(arr);

        int M = in.nextInt();

        for (int i = 0; i < M; i++) {
            int target = in.nextInt();
            sb.append(upperBound(arr, target) - lowerBound(arr, target)).append(' ');
        }
        System.out.println(sb);
    }

    public static int lowerBound(int[] arr, int target) {
        int lo = 0;
        int hi = arr.length;

        while (lo < hi) {
            int mid = (lo + hi) / 2;

            if (target <= arr[mid]) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    public static int upperBound(int[] arr, int target) {
        int lo = 0;
        int hi = arr.length;

        while (lo < hi) {
            int mid = (lo + hi) / 2;

            if (target < arr[mid]) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
