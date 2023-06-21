#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

vector<vector<int>> graph;
vector<int> info_g;

int ans = 0;

void DFS(int cur, int sheep, int wolf, queue<int> q) {
    
    if (info_g[cur] == 0) {
        sheep++;
    } else {
        wolf++;
    }
    
    if (wolf >= sheep) return;
    if (ans < sheep) ans = sheep;
    
    // add new candid
    for (int i = 0; i < graph[cur].size(); i++) {
        q.push(graph[cur][i]);
    }
    
    for (int i = 0; i < q.size(); i++) {
        int next = q.front();
        q.pop();
        DFS(next, sheep, wolf, q);
        q.push(next);
    }
}


int solution(vector<int> info, vector<vector<int>> edges) {
    int n = info.size();
    
    graph.assign(n, vector<int>({}));
    info_g = info;
    
    for (int i = 0; i < n-1; i++) {
        int pi = edges[i][0];
        int ci = edges[i][1];
        graph[pi].push_back(ci);
    }
    queue<int> q;
    DFS(0, 0, 0, q);
    return ans;
}