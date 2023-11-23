#include "bits/stdc++.h"
using namespace std;

struct Node {
    int n;
    double cost;
};
struct compare {
    bool operator()(const Node l,const Node r) {
        return l.cost>r.cost;
    }
};

#define MX 5000000000

int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int N, W; cin>>N>>W;
    double M; cin>>M;
    int locx[N+1];
    int locy[N+1];
    double nodes[N+1][N+1];
    double dp[N+1];
    for (int i = 1 ; i<=N; ++i) {
        int x,y; cin>>x>>y;
        locx[i] = x; locy[i] = y;
    }
    for(int i=1; i<=N; ++i) {
        dp[i] = MX;
        for(int j=1;j<=N;++j) {
            double x = (locx[i]-locx[j]);
            double y = (locy[i]-locy[j]);
            double dist = sqrt(x*x+y*y);
            if(dist<=M) {
                nodes[i][j] = dist;
            } else {
                nodes[i][j] = MX;
            }
        }
    }
    
    for(int i=0;i<W;++i) {
        int x,y; cin>>x>>y;
        nodes[x][y]=0; nodes[y][x]=0;
    }
    priority_queue<Node,vector<Node>,compare> que;
    que.push({1,0.0});
    dp[1] = 0;
    
    while(!que.empty()) {
        Node f = que.top(); que.pop();
        if(dp[f.n] < f.cost) { continue; }
        if(f.n == N) { break; }
        for (int i =1; i<=N; ++i) {
            if(nodes[f.n][i] == MX) { continue;}
            double nextCost = f.cost + nodes[f.n][i];
            if(dp[i] > nextCost ) {
                dp[i] = nextCost;
                que.push({i,nextCost});
            }
        }
    }
    cout<<(long long)(floor(dp[N]*1000));
}
