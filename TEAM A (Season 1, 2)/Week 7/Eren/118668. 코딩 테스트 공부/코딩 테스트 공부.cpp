#include <iostream>
#include <vector>
using namespace std;
int dp[303][303];
#define INF 987654321

int solution(int alp, int cop, vector<vector<int>> problems) {
    int answer = 0;
    int mxAlp = 0;
    int mxCop = 0;
    for(auto problem: problems){
        mxAlp = max(mxAlp, problem[0]);
        mxCop = max(mxCop, problem[1]);
    }
    
    if(mxAlp <= alp and mxCop <= cop) return 0;
    
    for(int i=0; i<303; i++) std::fill(dp[i], dp[i] +303, INF);

    if(alp > mxAlp) alp = mxAlp;
    if(cop > mxCop) cop = mxCop;

    dp[alp][cop] = 0;

    for(int i=alp; i<=mxAlp; i++){
      for(int j=cop; j<=mxCop; j++){
        if(j+1 <= mxCop) 
          dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1);
        
        if(i + 1 <= mxAlp)
          dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1);

        for(auto problem : problems){
          if(i < problem[0] or j < problem[1]) { continue; }

          int a = min(i + problem[2], mxAlp);
          int b = min(j + problem[3], mxCop);

          dp[a][b] = min(dp[a][b], dp[i][j] + problem[4]);

        }
      }
    }

    answer = dp[mxAlp][mxCop];
    
    return answer;
}