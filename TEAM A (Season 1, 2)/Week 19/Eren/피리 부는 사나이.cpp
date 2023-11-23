#include <bits/stdc++.h>
using namespace std;
#define init cin.tie(0)->sync_with_stdio(0)

#define INF 2e9
#define ii pair<int, int>
#define iii tuple<int, int, int>

int n, m;

int board[1005][1005];
bool chk[1005][1005];

int c2i(char c) { // +2 % 4 하면 반대방향이 나오게끔
  if(c == 'U') return 0;
  if(c == 'L') return 1;
  if(c == 'D') return 2;
  if(c == 'R') return 3;
  return -1;
}
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, -1, 0, 1};

bool canGo(int nx, int ny) {
  if(nx < 1 || ny < 1 || nx > n || ny > m) return false;
  if(chk[nx][ny]) return false;

  return true;
}

void bfs(int i, int j) {
  queue<ii> q;
  q.push({i, j});
  chk[i][j] = true;

  while(q.size()) {
    auto [x, y] = q.front();
    q.pop();

    for(int i=0; i<4; i++){
      int nx = x + dx[i];
      int ny = y + dy[i];

      if(canGo(nx, ny)) {
        int dir = board[nx][ny];

        if(i == (dir+2) % 4) {
          q.push({nx, ny});
          chk[nx][ny] = true;
        }
      }
    }
  }
}

ii travel(int i, int j) {
  int x = i;
  int y = j;


  while(true) {
    chk[x][y] = true;

    bfs(x, y);

    int dir = board[x][y];

    int nx = x + dx[dir];
    int ny = y + dy[dir];

    if(canGo(nx, ny) == false) break;

    x = nx;
    y = ny;
  }

  chk[x][y] = true;

  return {x, y};
}

int ans;


int main() {
  init;
  cin >> n >> m;

  for(int i=0; i<n; i++){
    string s;
    cin >> s;
    for(int j=0; j<m; j++) {
      int dir = c2i(s[j]);
      board[i+1][j+1] = dir;
    }
  }

  for(int i=1; i<=n; i++){
    for(int j=1; j<=m; j++){

      if(chk[i][j] == false) {
        auto a = travel(i, j);
        ans++;
      }

    }
  }
  cout << ans;
}
