import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.Stack;
import java.util.StringTokenizer;

class 크게_만들기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int count=0;
        char[] numbers = br.readLine().toCharArray();
        Stack<Character> stack = new Stack<>();
        for(int i=0;i<numbers.length;i++) {
            //맨위에 있는 숫자가 현재 숫자보다 작으면 pop 하고 count++
            while (count < k&&!stack.isEmpty()&&stack.peek()< numbers[i] ) {
                count++;
                stack.pop();
            }
            stack.push(numbers[i]);
        }
        while(!stack.isEmpty()){
            sb.append(stack.pop());
        }
        bw.write(sb.reverse().toString().substring(0,n-k));
        bw.close();
        br.close();
    }
}
