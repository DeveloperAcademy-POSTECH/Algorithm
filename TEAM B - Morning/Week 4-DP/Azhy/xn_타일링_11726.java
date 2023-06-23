package BOJ._23_06_07;

import java.util.*;

public class xn_타일링_11726 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();

        int[] arr = new int[N];
        arr[0] = 1;
        arr[1] = 2;

        for (int i = 2; i < N; i++) {
            int num = arr[i - 1] + arr[i - 2];
            arr[i] = num % 10007;
        }

        System.out.println(arr[N-1]);
    }
}
