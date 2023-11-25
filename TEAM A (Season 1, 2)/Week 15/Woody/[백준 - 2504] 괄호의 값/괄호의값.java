import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

/**
 * @author : hyunwoopark
 * @version : 1.0.0
 * @package : ADA_Algorithm
 * @name : 괄호의값
 * @date : 2023/09/25 5:32 AM
 * @modifyed : $
 **/
public class 괄호의값 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        Stack<String> stack = new Stack<>();
        int answer = 0;
        for(char c: input.toCharArray()){
            String s = String.valueOf(c);
            int res=0;
            if(c=='('||c=='[')
                stack.push(s);
            else if(c==')'){
                boolean isClose = false;
                while(!stack.isEmpty()){
                    String temp = stack.pop();
                    if(temp.equals("(")) {
                        isClose = true;
                        break;
                    }
                    else if(temp.equals("[")){
                        break;
                    }else{
                        res += Integer.parseInt(temp);
                    }
                }
                if(isClose==false){
                    break;
                }
                if(res==0)
                    res = 1;
                stack.push(String.valueOf(res*2));
            }else if(c==']'){
                boolean isClose = false;
                while(!stack.isEmpty()){
                    String temp = stack.pop();
                    if(temp.equals("[")) {
                        isClose = true;
                        break;
                    }
                    else if(temp.equals("(")){
                        break;
                    }else{
                        res += Integer.parseInt(temp);
                    }
                }
                if(isClose==false){
                    answer = -1;
                    break;
                }
                if(res==0)
                    res = 1;
                stack.push(String.valueOf(res*3));
            }
        }
        if(answer==-1)
            answer = 0;
        else {
            answer = 0;
            while(!stack.isEmpty()){
                try {
                    answer += Integer.parseInt(stack.pop());
                }catch(NumberFormatException e){
                    answer = 0;
                    break;
                }
            }
        }
        System.out.println(answer);
    }
}
