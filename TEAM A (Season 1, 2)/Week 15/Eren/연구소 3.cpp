#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
#define ii pair<int, int>
#define INF 987654321

int board[55][55];
int n, m;
int zr = 0;
bool chk[55][55];

vector<ii> virus;
vector<ii> actVirus;



int dx[] = {1,0,-1,0};
int dy[] = {0,-1,0,1};

int ans = INF;

bool canGo(int x, int y){
  if(x < 1 || y < 1 || x > n || y > n) return false;
  if(board[x][y] == 1) return false;
  if(chk[x][y]) return false;

  return true;

}

void bfs() {
  queue<ii> q;
  for(int i=0; i<53; i++) fill(chk[i], chk[i]+55, false);
  int zrSize = zr;
  for(auto v: actVirus){ q.push(v); chk[v.first][v.second] = true; }

  int t = 0;

  while(q.size()){
    if(zrSize == 0) break;

    int qSize = q.size();
    for(int k=1; k<=qSize; k++){
      auto [x, y] = q.front(); q.pop();

      for(int i=0; i<4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(canGo(nx, ny)){
          q.push({nx, ny});
          chk[nx][ny] = true;
          if(board[nx][ny] == 0) zrSize--;
        }
      }
    }
    t++;
  }
  if(zrSize == 0)
    ans = min(ans, t);
}

void comb(int here) {

  if(actVirus.size() == m){
    bfs();
    return;
  }

  for(int i=here+1; i< virus.size(); i++){
    actVirus.push_back(virus[i]);
    comb(i);
    actVirus.pop_back();
  }
  
}

int main() {
  cin.tie(0) -> ios_base::sync_with_stdio(0);
  cin >> n >> m;

  for(int i=1; i<=n; i++){
    for(int j=1; j<=n; j++){
      cin >> board[i][j];
      if(board[i][j] == 0) zr++;
      else if(board[i][j] == 2) virus.push_back({i, j}); 
    }
  }

  comb(-1);
  
  if(ans == INF) cout << -1;
  else cout << ans;

}
