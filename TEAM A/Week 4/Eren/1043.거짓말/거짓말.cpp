#include<bits/stdc++.h>
using namespace std;

bool chk[55];
int p[55];
int n, m, k;
vector<int> party[51];

int Find(int x){
  if(p[x] == x) return x;
  else return p[x] = Find(p[x]);
}

bool Union(int x, int y){
  x = Find(x);
  y = Find(y);
  if(x == y) return false;

  if(chk[y] == true) swap(x, y);
  p[y] = x;
  return true;
}

int main(){
  cin.tie(0) -> ios_base::sync_with_stdio(0);
  cin >> n >> m;
  cin >> k;
  for(int i=1; i<=k; i++){
    int a; 
    cin >> a;
    chk[a] = true;
  }
  for(int i=1; i<=m; i++){ 
    int num;// 변수명 뭐라할까.
    cin >> num;
    for(int j=1; j<=num; j++){
      int id;
      cin >> id;
      party[i].push_back(id);
    }
  }
  for(int i=1; i<=50; i++) p[i] = i;

  for(int i=1; i<=m; i++){
    for(int j=0; j<party[i].size()-1; j++){
      int prev = party[i][j];
      int nxt = party[i][j+1];
      Union(prev, nxt);
    }
  }

  int ans = m;

  for(int i=1; i<=m; i++){
    for(int j=0; j<party[i].size(); j++){
      int id = party[i][j];
      int root = Find(id);
      if(chk[root]) { ans--; break; }
    }
  }

  cout << ans;
}