public class 프로그래머스_150365_미로_탈출_명령어 {
    public static void main(String[] args) {
        new Solution();

    }

    static class Solution {
        static final int[] dx = {1, 0, 0, -1};
        static final int[] dy = {0, -1, 1, 0};
        static final char[] pathCharacter = new char[]{'d','l','r','u'};
        static int maxRow,maxCell;
        static int destinationX, destinationY;
        static int pathLength;
        static String answer = null;

        public String solution(int n, int m, int x, int y, int r, int c, int k) {
            maxRow = n;
            maxCell = m;
            int currentX = x-1;
            int currentY = y-1;
            destinationX = r-1;
            destinationY = c-1;
            pathLength = k;

            int distance = Math.abs(currentX-destinationX)+Math.abs(currentY-destinationY);
            if(distance>k | distance%2!=k%2)
                return "impossible";
            dfs(currentX,currentY,"",0);

            return answer==null?"impossible":answer;
        }
        public void dfs(int x, int y,String path,int currentPathLength){
            if(answer!=null)
                return;
            if(currentPathLength+Math.abs(x-destinationX)+Math.abs(y-destinationY)>pathLength)
                return;
            if(currentPathLength==pathLength) {
                answer = path;
                return;
            }
            for(int i=0; i<4; i++){
                int nx = x+dx[i];
                int ny = y+dy[i];
                if(nx<0 | ny<0 | nx>=maxRow | ny>=maxCell)
                    continue;
                dfs(nx,ny,path+pathCharacter[i],currentPathLength+1);
            }
        }
    }
    //사전순 
}
