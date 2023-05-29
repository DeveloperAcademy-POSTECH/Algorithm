import java.io.*;
import java.util.*;

public class 백준_2143_두_배열의_합 {
    static private int T, N, M;
    static private int[] A, B;
    static private long result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//        StringTokenizer st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(br.readLine());
        N = Integer.parseInt(br.readLine());
        A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++)
            A[i] = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(br.readLine());
        B = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++)
            B[i] = Integer.parseInt(st.nextToken());
        findPrefixSum();
        bw.write(String.valueOf(result));
        bw.close();
        br.close();

    }

    public static void findPrefixSum() {
        List<Integer> subArrayA = new ArrayList<>();
        List<Integer> subArrayB = new ArrayList<>();
        int temp = 0;
        //A 부분 배열의 합 구하기
        for (int i = 0; i < N; i++) {
            temp = 0;
            for (int j = i; j < N; j++) {
                temp += A[j];
                subArrayA.add(temp);
            }
        }
        temp = 0;
        //B 부분 배열의 합 구하기
        for (int i = 0; i < M; i++) {
            temp = 0;
            for (int j = i; j < M; j++) {
                temp += B[j];
                subArrayB.add(temp);
            }
        }
        Collections.sort(subArrayA);
        Collections.sort(subArrayB);

        //투포인터 기법사용
        int aPointer = 0;
        int bPointer = subArrayB.size() - 1;

        while (aPointer < subArrayA.size() && bPointer >= 0) {
            int aValue = subArrayA.get(aPointer);
            int bValue = subArrayB.get(bPointer);
            int sum = aValue + bValue;
            //sum == T 이면 부분배열의 합이 같은것이 몇개 있는지 확인후 곱하여 result 증가
            if (sum == T) {
                long dupACnt = 0;
                long dupBCnt = 0;
                //같은 값이 몇 개 인지 확인.
                while (aPointer < subArrayA.size()) {
                    if (subArrayA.get(aPointer) != aValue)
                        break;
                    dupACnt++;
                    aPointer++;
                }
                while (bPointer >=0) {
                    if (subArrayB.get(bPointer) != bValue)
                        break;
                    dupBCnt++;
                    bPointer--;
                }
                result += dupACnt * dupBCnt;
            } else if (sum > T) {
                bPointer--;
            } else {
                aPointer++;
            }
        }

    }
}
