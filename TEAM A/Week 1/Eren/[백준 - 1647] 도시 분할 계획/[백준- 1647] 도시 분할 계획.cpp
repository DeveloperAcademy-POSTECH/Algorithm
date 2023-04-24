#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define ll long long
#define iii tuple<int, int, int>
#define ii pair<int, int>

int v, e;
ll p, q, s;

vector<ii> adj[100'004];
bool chk[100'004];

int ans;

int cnt;
int lastCost;

void prim(){
  priority_queue<ii, vector<ii>, greater<ii>> pq;
  for(auto [c, b] : adj[1])
    pq.push({c, b});
  
  chk[1] = true;
  
  while(pq.size()){
    auto [cost, here] = pq.top();
    pq.pop();

    if(chk[here]) continue;
    chk[here] = true;
    ans += cost;
    lastCost = max(lastCost, cost);

    for(auto [d, there] : adj[here]){
      if(chk[there] == false){
        pq.push({d, there});
      }
    }
  }



}

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);
  cin >> v >> e;

  for(int i=0;i < e; i++){
    cin >> p >> q >> s;
    adj[p].push_back({s, q});
    adj[q].push_back({s, p});
  }
  prim();
  cout << ans - lastCost;

}
