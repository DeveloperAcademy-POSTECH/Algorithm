import java.io.*;
import java.util.StringTokenizer;

class 백준_1987_알파벳 {
    public static int[] dr = {0, 0, 1, -1};
    public static int[] dc = {1, -1, 0, 0};
    public static int max = 0;
    public static int[][] map;
    public static int row, cell;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        row = Integer.parseInt(st.nextToken());
        cell = Integer.parseInt(st.nextToken());
        map = new int[row][cell];
        for (int i = 0; i < row; i++) {
            String str = br.readLine();
            for (int j = 0; j < cell; j++) {
                map[i][j] = str.charAt(j) - 'A';
            }
        }
        findMaximum(0, 0, 0, 0);
        bw.write(String.valueOf(max));
        bw.close();
        br.close();
    }

    public static void findMaximum(int r, int c, int visited, int count) {
        if (r < 0 | r >= row | c < 0 | c >= cell)
            return;

        int currentNumber = map[r][c];
        if (isVisited(visited, currentNumber))
            return;
        visited += 1 << currentNumber;
        count++;
        for (int i = 0; i < 4; i++) {
            findMaximum(r + dr[i], c + dc[i], visited, count);
        }
        if (max < count)
            max = count;
    }

    public static boolean isVisited(int visited, int num) {
        int temp = 1 << num;
        return (visited & temp) != 0;
    }
}