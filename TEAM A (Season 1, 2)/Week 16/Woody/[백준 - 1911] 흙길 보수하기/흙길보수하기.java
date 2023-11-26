import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;

/**
 * @author : hyunwoopark
 * @version : 1.0.0
 * @package : ADA_Algorithm
 * @name : 흙길보수하기
 * @date : 10/17/23 1:59 AM
 * @modifyed : $
 **/
public class 흙길보수하기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int answer = 0;
        ArrayList<Point> points = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            points.add(new Point(start, end));
        }
        Collections.sort(points, Comparator.comparingInt(o -> o.start));
        int current = 0;
        for (Point point : points) {
            if (current <= point.start) {
                current = point.start;
                while (current < point.end) {
                    current += l;
                    answer++;
                }
            } else if (current > point.start) {
                while (current < point.end) {
                    current += l;
                    answer++;
                }
            }
        }

        System.out.println(answer);

    }

    static class Point {
        int start;
        int end;

        Point(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
}
