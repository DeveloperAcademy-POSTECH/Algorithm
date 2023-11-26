import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * @author : hyunwoopark
 * @version : 1.0.0
 * @package : ADA_Algorithm
 * @name : 게임개발
 * @date : 2023/09/03 9:39 PM
 * @modifyed : $
 **/
public class 게임개발 {
    static Building[] buildings;

    public static void main(String[] arg) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        buildings = new Building[n + 1];

        for (int i = 1; i <= n; i++) {
            buildings[i] = new Building(br.readLine());
        }
        for (int i = 1; i <= n; i++) {
            System.out.println(buildings[i].getCost());
        }

    }

    static class Building {
        private int cost;
        private List<Integer> needBuildings;
        private int minBuildCost = 0;

        Building(String buildStr) {
            StringTokenizer st = new StringTokenizer(buildStr);
            this.cost = Integer.parseInt(st.nextToken());
            this.needBuildings = new ArrayList<>();
            int currentInteger = Integer.parseInt(st.nextToken());
            while (currentInteger != -1) {
                needBuildings.add(currentInteger);
                currentInteger = Integer.parseInt(st.nextToken());
            }
            if (needBuildings.size() == 0)
                minBuildCost = cost;
        }

        public int getCost() {
            if (minBuildCost == 0) {
                int maxCost = Integer.MIN_VALUE;
                for (int buildingNum : needBuildings) {
                    //building 중 짓는데 시간이 가장 오래걸리는 건물 찾기
                    maxCost = Math.max(buildings[buildingNum].getCost(), maxCost);
                }
                minBuildCost = maxCost;
                minBuildCost += cost;
            }
            return minBuildCost;


        }
    }

}
