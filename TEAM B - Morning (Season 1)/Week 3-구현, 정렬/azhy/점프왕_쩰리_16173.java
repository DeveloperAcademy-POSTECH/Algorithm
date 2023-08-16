package BOJ._23_05_27;

import java.util.*;

public class 점프왕_쩰리_16173 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[][] area = new int[n][n];
        boolean[][] visited = new boolean[n][n];

        for (int i = 0; i < area.length; i++) {
            for (int j = 0; j < area.length; j++) {
                area[i][j] = sc.nextInt();
                visited[i][j] = false;
            }
        }
        BFS(area, visited);
        sc.close();
    }

    static void BFS(int[][] area, boolean[][] visited) {
        int leng = area.length;
        boolean result = false;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0});

        while (!q.isEmpty()) {
            int[] now = q.poll();
            int row = now[0];
            int col = now[1];

            visited[row][col] = true;

            if (area[row][col] == -1) {
                result = true;
                break;
            }

            int bottom = row + area[row][col];
            int right = col + area[row][col];

            if (bottom < leng && !visited[bottom][col]) {
                q.add(new int[]{bottom, col});
                visited[bottom][col] = true;
            }
            if (right < leng && !visited[row][right]) {
                q.add(new int[]{row, right});
                visited[row][right] = true;
            }
        }

        if (result) {
            System.out.println("HaruHaru");
        } else {
            System.out.println("Hing");
        }
    }
}

