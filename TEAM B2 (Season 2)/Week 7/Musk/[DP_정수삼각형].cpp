#include <string>
#include <vector>
#define MAX 500

using namespace std;

// 아이디어 -> 똑같은 삼각형을 하나 더 만들어서 각각 칸마다의 최댓값을 저장해나가는것.

int solution(vector<vector<int>> triangle) {
    // vector는 동적할당이라 그냥 접근하려하면 오류남. 이런 곳에선 그냥 배열이 나을수도.
    int dp[MAX][MAX];
    int size = triangle.size();
    
    for(int i=0; i<size;i++) {
        for(int j = 0; j<=i; j++){
            if(j==0) { dp[i][j] = dp[i-1][0] + triangle[i][j]; }
            else if(j==i) { dp[i][j] = dp[i-1][i-1] + triangle[i][j]; }
            else { dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]; }
        }
    }
    
    int result = 0;
    for(auto item: dp[size-1]) {
        if(result < item) { result = item; }
    }
    
    return result;
}