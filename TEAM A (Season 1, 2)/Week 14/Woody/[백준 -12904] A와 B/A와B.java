/**
 * @author : hyunwoopark
 * @version : 1.0.0
 * @package : ADA_Algorithm
 * @name : A와B
 * @date : 2023/09/12 1:11 PM
 * @modifyed : $
 **/
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;

class A와B {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String start = br.readLine();
        StringBuilder sb = new StringBuilder(br.readLine());
        while(sb.length()!=start.length()){
            char c=sb.charAt(sb.length()-1);
            sb.deleteCharAt(sb.length()-1);
            if(c=='B'){
                sb.reverse();
            }
        }
        if(start.equals(sb.toString()))
            bw.write("1");
        else
            bw.write("0");
        bw.close();
        br.close();
    }

}
