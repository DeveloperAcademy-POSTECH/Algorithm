import java.io.*;
import java.util.Stack;
public class 되돌리기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        Stack<String[]> stack = new Stack<>();

        for (int i = 0; i < N; i++) {
            String[] strings = br.readLine().split(" ");

            stack.push(strings);

        }
        while (!stack.isEmpty()) {
            String[] temp = stack.peek();
            if (temp[0].equals("type"))
                sb.append(stack.pop()[1]);
            else {
                //되돌리기 할 시간
                int undoTime = Integer.parseInt(temp[2]) - Integer.parseInt(temp[1]);
                while (!stack.isEmpty() && Integer.parseInt(stack.peek()[2]) >= undoTime) {
                    stack.pop();
                }
            }
        }
        //거꾸로 누적된 type reverse하여 다시 원래대로
        bw.write(sb.reverse().toString());
        bw.close();
        br.close();
    }
}
