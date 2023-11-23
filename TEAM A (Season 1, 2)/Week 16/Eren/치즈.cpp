#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <iomanip>
using namespace std;

#define INF 2e9
#define ii pair<int, int>

int n, m;
int board[103][103];
int adj[103][103];
bool chk[103][103];
const int dx[] = {1, 0 ,-1, 0};
const int dy[] = {0 ,-1, 0, 1};

vector<ii> air;
queue<ii> q;
bool canGo(int nx, int ny) {
  if(nx < 1 || ny < 1 || nx > n || ny > m) return false;
  if(chk[nx][ny] == true) return false;
  if(board[nx][ny] == 1) return false;

  return true;
}

bool isCheese(int nx, int ny) {
  if(nx < 1 || ny < 1 || nx > n || ny > m) return false;
  if(board[nx][ny] == 1) return true;

  return false;
}

int ans;

void init() {
  for(int i=0; i<102; i++) fill(chk[i], chk[i] + 102, false);
  for(int i=0; i<102; i++) fill(adj[i], adj[i] + 102, 0);
  for(auto& [x, y]: air) {
    q.push({x, y});
    chk[x][y] = true;
  }
}

bool onMeltingCheese() {
  vector<ii> melting;

  while(q.size()) {
    auto [x, y] = q.front(); 
    q.pop();

    for(int i=0; i<4; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if(isCheese(nx, ny)) {
        adj[nx][ny]++;
        if(adj[nx][ny] == 2) 
          melting.push_back({nx, ny});
      }
      if(canGo(nx, ny)) {
        chk[nx][ny] = true;
        q.push({nx ,ny});
      }
    }
  }
  if(melting.size() == 0) return false;
  air = melting;

  for(auto& [x, y]: melting) {
    board[x][y] = 0;
  }
  ans++;
  return true;
}

void Print() {
  cout << "------------------------------------" << endl;
  for(int i=1; i<=n; i++) {
    for(int j=1; j<=m; j++) {
      cout << setw(2) << board[i][j] ;
    }
    cout << endl;
  }
}

int main() {
  cin >> n >> m;
  for(int i=1; i<=n; i++){
    for(int j=1; j<=m; j++){
      cin >> board[i][j];
    }
  }

  for(int i=1; i<=n; i++) {
    if(board[i][1] == 0) air.push_back({i, 1});
    if(board[i][m] == 0) air.push_back({i, m});
  }
  for(int j=1; j<=m; j++){
    if(board[1][j] == 0) air.push_back({1, j});
    if(board[n][j] == 0) air.push_back({n, j});
  }

  bool result = true;

  while(result) { 
    init();
    result = onMeltingCheese();
    // Print();
  }
  cout << ans;

}
