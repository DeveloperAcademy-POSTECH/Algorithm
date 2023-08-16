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

int n;
int map[17][17];
int chkBit;

int cost[16][1 << 16];

int dfs(int cur, int visited){
    if(visited == chkBit){
        if(map[cur][0] == 0) return INF;
        else return map[cur][0];
    }

    if(cost[cur][visited] != -1) return cost[cur][visited];
    cost[cur][visited] = INF;

    for(int i=0; i<n; i++){
        if(map[cur][i] == 0) continue;
        if((visited & (1 << i)) == (1 << i)) continue;

        cost[cur][visited] = min(cost[cur][visited], map[cur][i] + dfs(i, visited | (1 << i)));
    }
    return cost[cur][visited];
}


int main(){
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> map[i][j];
        }
    }
    chkBit = (1 << n) - 1;
    memset(cost, -1, sizeof(cost));

    cout << dfs(0, 1);
}