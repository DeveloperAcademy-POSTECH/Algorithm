#include <bits/stdc++.h>
using namespace std;
#define init cin.tie(0)->sync_with_stdio(0)
#define ii pair<int, int>

int n, m;
int dist[10005];
vector<ii> adj[10005];
vector<int> prv[10005];
bool visited[10005];


int st, en;
void bfs() {
  queue<ii> q;
  q.push({st, 0});

  while(q.size()) {
    auto [cur, distance] = q.front();
    q.pop();

    for(auto [nxt, cost]: adj[cur]) {

      if(dist[nxt] < distance + cost) {
        dist[nxt] = distance + cost;
        prv[nxt].clear();
        prv[nxt].push_back(cur);
        q.push({nxt, distance + cost});
      }
      else if(dist[nxt] == distance + cost) {
        prv[nxt].push_back(cur);
      }

    }
  }
}
int cnt;
bool firstwhere = false;

void dfs(int cur) {
  if(visited[cur]) return;
  if(cur == st) return; 

  visited[cur] = true;
  cnt += prv[cur].size();

  for(auto x: prv[cur]) {
    dfs(x);
  }
}

int main() {
  init;
  cin >> n >> m;
  for(int i=0; i<m; i++){
    int a, b, c;
    cin >> a >> b >> c;
    adj[a].push_back({b, c});
  }
  cin >> st >> en;
  bfs();
  dfs(en);
  // for(auto x: prv[6]) { cout << x << ' '; }

  cout << dist[en] << '\n';
  cout << cnt;
}