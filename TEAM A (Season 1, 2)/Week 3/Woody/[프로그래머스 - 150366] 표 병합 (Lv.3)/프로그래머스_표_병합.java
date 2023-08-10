import java.util.*;

public class 프로그래머스_표_병합 {
    public static void main(String[] args){
        Solution solution = new Solution();
        for(String str: solution.solution(new String[]{"UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"})){
            System.out.println(str);
        }
    }

    static class Solution {

        static final int ROW=50;
        static final int CELL=50;

        static Cell[][] table = new Cell[ROW][CELL];
        static HashMap<String, HashSet<Cell>> textMap;
        class Cell{
            private String value;
            public void updateValue(String value){
                if(value!=null){
                    if(this.value!=null){
                        HashSet<Cell> originalSet = textMap.get(this.value);
                        originalSet.remove(this);
                    }
                    HashSet<Cell> cellsBySameValue = textMap.get(value);
                    if(cellsBySameValue==null){
                        cellsBySameValue = new HashSet<>();
                        textMap.put(value, cellsBySameValue);
                    }
                    this.value = value;
                    if(value!=null)
                        cellsBySameValue.add(this);
                }
            }
            public String getValue(){
                return value;
            }
            public String print(){
                return value==null?"EMPTY":value;
            }
        }

        public String[] solution(String[] commands) {
            StringBuilder sb=  new StringBuilder();
            textMap = new HashMap<>();
            for(String cmdStr: commands){
                StringTokenizer st = new StringTokenizer(cmdStr);
                String cmd = st.nextToken();
                switch(cmd){
                    case "UPDATE":{
                        String param1 = st.nextToken();
                        String param2 = st.nextToken();
                        //UPDATE r c value
                        if(st.hasMoreTokens()){
                            String param3 = st.nextToken();
                            int r=Integer.parseInt(param1)-1;
                            int c = Integer.parseInt(param2)-1;
                            Cell selectedCell = table[r][c];
                            if(selectedCell==null) {
                                selectedCell = new Cell();
                                table[r][c] = selectedCell;
                            }
                            selectedCell.updateValue(param3);
                        }
                        //UPDATE value1 value2
                        else{
                            HashSet<Cell> cellListByText = textMap.get(param1);
                            if(cellListByText==null)
                                continue;
                            else{
                                List<Cell> cells = new ArrayList<>(cellListByText);
                                for(Cell cell:cells) {
                                    cell.updateValue(param2);
                                }
                            }
                            textMap.put(param1,null);

                        }

                        break;
                    }
                    case "MERGE":{
                        int r1,c1,r2,c2;
                        r1 = Integer.parseInt(st.nextToken())-1;
                        c1 = Integer.parseInt(st.nextToken())-1;
                        r2 = Integer.parseInt(st.nextToken())-1;
                        c2 = Integer.parseInt(st.nextToken())-1;
                        Cell cell1 = table[r1][c1];
                        Cell cell2 = table[r2][c2];
                        if(cell1==null&&cell2==null){
                            Cell cell = new Cell();
                            table[r1][c1] = cell;
                            table[r2][c2] = cell;
                        }else if(cell1==null&&cell2!=null){
                            table[r1][c1] = cell2;
                        }else if(cell1!=null && cell2==null){
                            table[r2][c2] = cell1;
                        }else{
                            if(cell1.getValue()!=null){
                                for(int i=0; i<50; i++){
                                    for(int j=0; j<50; j++){
                                        if(table[i][j]==cell2)
                                            table[i][j]=cell1;
                                    }
                                }
                            }else{
                                for(int i=0; i<50; i++){
                                    for(int j=0; j<50; j++){
                                        if(table[i][j]==cell1)
                                            table[i][j]=cell2;
                                    }
                                }
                            }
                        }
                        break;
                    }
                    case "UNMERGE":{
                        int r = Integer.parseInt(st.nextToken())-1;
                        int c = Integer.parseInt(st.nextToken())-1;
                        Cell cell = table[r][c];
                        if(cell!=null){
                            for(int i=0; i<50; i++){
                                for(int j=0; j<50; j++){
                                    if(i==r&&j==c)
                                        continue;
                                    else if(table[i][j]==cell)
                                            table[i][j]=null;

                                }
                            }
                        }
                        break;
                    }
                    case "PRINT":{
                        int r = Integer.parseInt(st.nextToken())-1;
                        int c = Integer.parseInt(st.nextToken())-1;
                        Cell cell = table[r][c];

                        if(cell!=null)
                            sb.append(cell.print());
                        else
                            sb.append("EMPTY");
                        sb.append(" ");
                        break;
                    }
                }

                System.out.println(cmdStr);

            }

            String[] answer = sb.toString().trim().split(" ");
            return answer;
        }
    }
}
