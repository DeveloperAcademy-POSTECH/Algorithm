package BOJ._23_06_03;

import java.util.*;
import java.io.*;
public class 설탕_배달_2839 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int result = 0;

        while (N >= 3) {
            if (N % 5 == 0) {
                N -= 5;
                result += 1;
            } else {
                N -= 3;
                result += 1;
            }
        }
        System.out.println(N == 0 ? result : -1);
    }
}
