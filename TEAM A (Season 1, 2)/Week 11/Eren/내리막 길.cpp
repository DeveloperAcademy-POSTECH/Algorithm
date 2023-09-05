#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int dx[] = {0, 1, 0, -1};
const int dy[] = {1, 0, -1, 0};

int n, m, ans;
int board[502][502];
int dp[502][502];

bool isInBound(int nx, int ny){
  if(nx < 1 || ny < 1 || nx > n || ny > m) return false;
  return true;
}

int dfs(int x, int y){
  if(x == n && y == m) return 1;
  if(dp[x][y] != -1) return dp[x][y];

  dp[x][y] = 0;
  for(int i=0; i<4; i++){
    int nx = x + dx[i];
    int ny = y + dy[i];
    if(isInBound(nx, ny) == false) continue;

    if(board[nx][ny] < board[x][y]) {
      dp[x][y] = dp[x][y] + dfs(nx, ny);
    }
  }
  return dp[x][y];
}

int main() {
  cin.tie(0) -> ios_base::sync_with_stdio(false);

  cin >> n >> m;
  for(int i=1; i<=n; i++){
    for(int j=1; j<=m; j++){
      cin >> board[i][j];
      dp[i][j] = -1;
    }
  }

  ans = dfs(1,1);
  if(ans == -1) cout << 0;
  else cout << ans;



}