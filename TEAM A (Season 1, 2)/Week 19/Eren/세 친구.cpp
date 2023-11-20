#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <map>
using namespace std;
#define init cin.tie(0)->sync_with_stdio(0)


#define INF 2e9
#define iii tuple<int, int, int>

int n, m;

vector<int> adj[4002];
vector<vector<int>> friends;

void dfs(vector<int> v) {
  int cur = *v.rbegin();

  if(v.size() == 3) {
    for(auto x: adj[cur]) {
      if(x == v[0]) {
        friends.push_back(v);
        break;
      }
    }
    return;
  }

  for(auto x: adj[cur]) {
    if(x > cur) {
      v.push_back(x);
      dfs(v);
      v.pop_back();
    }
  }

}

int main() {
  init;
  cin >> n >> m;
  for(int i=0; i<m; i++) {
    int a, b;
    cin >> a >> b;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  for(int i=1; i<=n; i++) {
    dfs({i});
  }
  int ans = INF;

  for(auto f: friends) {
    int cnt = 0;
    for(int x: f) {
      cnt += adj[x].size() - 2;
    }
    ans = min(ans, cnt);
  }
  if(ans == INF) cout << -1;
  else cout << ans;
}