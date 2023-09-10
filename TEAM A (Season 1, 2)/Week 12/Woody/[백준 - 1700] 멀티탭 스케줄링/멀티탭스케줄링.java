import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * @author : hyunwoopark
 * @version : 1.0.0
 * @package : ADA_Algorithm
 * @name : 멀티탭스케줄링
 * @date : 2023/08/29 3:12 AM
 * @modifyed : $
 **/
public class 멀티탭스케줄링 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        boolean[] inserted;
        int[] sequence;
        int used = 0;
        int answer = 0;
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());


        inserted = new boolean[k+1];
        sequence = new int[k];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<k; i++){
            sequence[i] = Integer.parseInt(st.nextToken());
        }
        for(int i=0; i<k; i++){
            int device = sequence[i];
            if(inserted[device]){
                continue;
            }
            if(used<n){
                inserted[device] = true;
                used++;
                continue;
            }
            //다시 사용될 기기인지 확인
            List<Integer> temp = new ArrayList<>();
            for(int j=i; j<k; j++){
                if(inserted[sequence[j]]&&!temp.contains(sequence[j])){
                    temp.add(sequence[j]);
                }
            }
            //모두 나중에 쓰는 기기인 경우
            if(temp.size()==n){
                //마지막에 나오는걸 뺀다.
                inserted[temp.get(temp.size()-1)] = false;
            }
            //나중에 안쓰는 기기가 존재하는경우
            else{
                for(int j=1; j<k+1; j++){
                    if(inserted[j] && !temp.contains(j)){
                        inserted[j] = false;
                        break;
                    }
                }
            }
            inserted[device] = true;
            answer++;
        }
        bw.write(String.valueOf(answer));
        bw.close();
        br.close();
    }
}
