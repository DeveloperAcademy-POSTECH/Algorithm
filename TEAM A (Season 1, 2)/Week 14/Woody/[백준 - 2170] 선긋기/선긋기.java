/**
 * @package : ADA_Algorithm
 * @name : 선긋기
 * @date : 2023/09/11 4:19 AM
 * @author : hyunwoopark
 * @version : 1.0.0
 * @modifyed : $
 **/

import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;

public class 선긋기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Line> lines = new ArrayList<>();
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            lines.add(new Line(br.readLine()));
        }
        lines.sort(Comparator.comparingInt(o -> o.start));
        int start = -1000000001;
        int end = -1000000001;
        int sum = 0;
        for(Line line: lines){
            if(line.start>end){
                sum += end-start;
                start = line.start;
                end = line.end;
            }else{
                if(end<line.end)
                    end = line.end;
            }
        }
        sum+= end-start;
        System.out.println(sum);
    }

    public static class Line {
        int start;
        int end;

        Line(String initStr) {
            String[] numbers = initStr.split(" ");
            this.start = Integer.parseInt(numbers[0]);
            this.end = Integer.parseInt(numbers[1]);
        }
    }
}

