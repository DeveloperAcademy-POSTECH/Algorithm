#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <string.h>
using namespace std;
 
typedef long long ll;
#define ii pair<int, int>
#define INF 987654321
 
typedef vector<int> VI;
VI v;
int n;
int dp[5][5][100'003];
int check(int from, int to){
    //처음에는 2
    if(from == 0) return 2;
    //다시 누르면 1
    if(from == to) return 1;
    //반대일 경우
    if(abs(from - to) == 2) return 4;
    //인접할 경우
    return 3;
}

int solve(int y, int x, int target){
    if(target == n) return 0;
    if(dp[y][x][target] != -1) return dp[y][x][target];

    int left = solve(v[target], x, target + 1) +check(y, v[target]);
    int right = solve(y, v[target], target + 1) + check(x, v[target]);
    return dp[y][x][target] = min(left,right);
}

int main(){
    while(true){
        int num;
        cin >> num;
        if(num == 0){ break; }
        v.push_back(num);
    }
    memset(dp, -1, sizeof(dp));
    n = v.size();
    cout << solve(0, 0, 0) << '\n';
    return 0;
}