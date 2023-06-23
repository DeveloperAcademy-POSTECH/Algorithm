package BOJ._23_06_15;

import java.util.*;

public class 수_찾기_1920 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int N = in.nextInt();
        int[] arr = new int[N];
        for(int i = 0; i < N; i++) {
            arr[i] = in.nextInt();
        }
        Arrays.sort(arr);

        int M = in.nextInt();

        for (int i = 0; i < M; i++) {
            if (binarySearch(arr, in.nextInt()) >= 0) {
                sb.append(1 + "\n");
            } else {
                sb.append(0 + "\n");
            }
        }
        System.out.println(sb);
    }

    public static int binarySearch(int[] arr, int target) {
        int low = 0;
        int mid = 0;
        int high = arr.length - 1;

        while (low <= high) {
            mid = (low + high) / 2;
            if (target < arr[mid]) {
                high = mid - 1;
            } else if (target > arr[mid]) {
                low = mid + 1;
            }  else {
                return 1;
            }
        }
        return -1;
    }
}
