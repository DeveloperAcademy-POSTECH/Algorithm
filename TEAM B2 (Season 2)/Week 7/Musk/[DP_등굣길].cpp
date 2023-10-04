#include <string>
#include <vector>
#include <iostream>
#define MAX 101
using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int dp[MAX][MAX] = {0,0};
    
    for(auto item: puddles) {
        dp[item[0]][item[1]] = -1;
    }
    
    dp[1][1] = 1;
    
    for(int i=1;i<=m;i++) {
        for(int j=1;j<=n;j++) {
            if(dp[i][j] == -1) { continue; }
            dp[i][j] += (dp[i-1][j]==-1) ? 0 : dp[i-1][j];
            dp[i][j] += (dp[i][j-1]==-1) ? 0 : dp[i][j-1];
            dp[i][j] %= 1000000007;
        }
    }
    
    return dp[m][n];
}

// 1트 - 뇌코딩
// 분기점을 저장해둬서 경로를 완성해두면 분기점으로 다시 돌아가 다시 탐색하는 방법
// Stack의 느낌이 더 강했고, 분기점을 저장해둔다 해도 말이 안되었음.
// 분기점이 언제 나올지 모른다는 예외도 있었음.
// 집 - - - - - - - - - - - - - - -
// x x x x x x x x x x x x x x x - 
// 대충 이런 경우를 어떻게 분기가 있다는걸 알수 있고 측정하는지 모르겠음.