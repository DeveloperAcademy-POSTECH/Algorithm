#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define ii pair<int, int>

int n, m;

vector<ii> adj[1005];
bool visited[1005];
int ans;

void mst() {
  priority_queue<ii, vector<ii>, greater<ii>> pq;
  pq.push({0, 1});
  int cnt = 0;

  while(pq.size()) {
    auto [cost, cur] = pq.top();
    pq.pop();

    if(visited[cur]) continue;

    visited[cur] = true;
    cnt++;
    ans += cost;
    if(cnt == n) break;

    for(auto [ncost, nxt]: adj[cur]) {
      if(visited[nxt] == true) continue; // 만약 도착한 적이 있다면
      pq.push({ncost, nxt});
    }
  }

}

int main() {
  cin >> n >> m;
  for(int i=0; i<m; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    if(a == b) continue;
    adj[a].push_back({c, b});
    adj[b].push_back({c, a});
  }
  mst();
  cout << ans;

}