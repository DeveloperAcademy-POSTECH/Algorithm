#include <iostream>
#include <queue>
#include <vector>
using namespace std;
#define ii pair<int, int>
#define iii tuple<int, int, int>

vector<ii> mst[50'005];
vector<ii> adj[50'005];
bool vis[50'005];
bool isGate[50'005];
bool isSummit[50'005];
int _n;
vector<ii> ans;

void getMST(){
    priority_queue<iii, vector<iii>, greater<iii>> pq;
    for(auto [c, there]: adj[1]){
        pq.push({c, 1, there});
    }
    vis[1] = true;
    
    int cnt = 1;
    while(pq.size() and cnt<_n){
        auto [c, here, there] = pq.top(); pq.pop();
        if(vis[there]) continue;
        
        mst[here].push_back({c, there});
        mst[there].push_back({c, here});
        vis[there] = true;
        cnt++;
        
        for(auto [cost, next]: adj[there]){
            pq.push({cost, there, next});
        }
    }
}

void dfs(int id, int val){
    if(isSummit[id]) {
        ans.push_back({val, id});
        return;
    }
    vis[id] = true;
    
    for(auto [cost, there]: mst[id]){
        if(vis[there]) continue;
        if(isGate[there]) continue;
        dfs(there, max(val, cost));
    }
}

vector<int> solution(int n, vector<vector<int>> paths, vector<int> gates, vector<int> summits) {
    _n = n;
    vector<int> answer;
    for(auto path: paths){
        int a = path[0]; int b = path[1]; int c = path[2];
        adj[a].push_back({c, b});
        adj[b].push_back({c, a});
    }
    getMST();
    
    for(auto gateId: gates) isGate[gateId] = true;
    for(auto summitId: summits) isSummit[summitId] = true;
    
    for(auto gateId: gates){
        fill(vis, vis+ 50'005, false);
        dfs(gateId, 0);
    }
    sort(ans.begin(), ans.end());
    
    answer.push_back(ans[0].second);
    answer.push_back(ans[0].first);
    
    return answer;
}