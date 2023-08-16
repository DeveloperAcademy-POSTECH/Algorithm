#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;
#define ii pair<int, int>
#define INF 987654321


int n, m;

int cnt[1005];
vector<int> graph[1005];


int main(){
  cin.tie(0)->ios_base::sync_with_stdio(0);
  cin >> n >> m;
  for(int i =0; i<m; i++){
    int k; 
    cin >> k;
    int prevA = -1;
    while(k-->0) {
      int a; cin >> a;
      if(prevA != -1) {
         graph[prevA].push_back(a);
         cnt[a]++;
      }
      prevA = a;
    }
  }

  queue<int> q;
  for(int i=1; i<=n; i++){
    if(cnt[i] == 0) q.push(i);
  }

  vector<int> v;
  while(q.size()){
    auto here = q.front();
    q.pop();
    v.push_back(here);

    for(auto there: graph[here]){
      cnt[there]--;
      if(cnt[there] == 0) q.push(there);
    }
  }

  bool possible = true;
  for(int i=1; i<=n; i++){
    if(cnt[i] > 0) { possible = false; break; }
  }

  if(possible == false) cout << 0;
  else {
    for(auto ele: v) cout << ele << endl;
  }
}