import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class 백준_1644_소수의_연속합 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        List<Integer> primes = sieveOfEratosthenes(4000000);
        int s = 0;
        int e = 0;
        int currentSum = 2;
        int result = 0;
        while (s < primes.size() && e < primes.size()) {
            if (currentSum == N) {
                result++;
                currentSum -= primes.get(s);
                s++;
            } else if (currentSum > N) {
                currentSum -= primes.get(s);
                s++;
            } else {
                e++;
                if(e>= primes.size())
                    break;
                currentSum += primes.get(e);
            }
        }
        bw.write(String.valueOf(result));
        bw.close();
        br.close();
    }

    public static List<Integer> sieveOfEratosthenes(int n) {
        boolean[] primes = new boolean[n + 1];
        List<Integer> primeList = new ArrayList<>();
        Arrays.fill(primes, true);
        primes[0] = false;
        primes[1] = false;
        for (int i = 2; i * i <= n; i++) {
            if (primes[i]) {
                for (int j = i * i; j <= n; j += i) {
                    primes[j] = false;
                }
            }
        }
        for (int i = 0; i < primes.length; i++) {
            if (primes[i])
                primeList.add(i);
        }
        return primeList;
    }
}
