#include <iostream>
#include <vector>
#include <queue>
#include <iomanip>
using namespace std;

int r, c;
int ans;
vector<string> board;

bool go(int x, int y){
  if(x < 0 || x >=r || y >= c) return false;
  if(board[x][y] == 'x') return false;
  if(y == c - 1) return true;

  board[x][y] = 'x';

  return go(x-1,y+1) || go(x,y+1) || go(x+1,y+1);
}

int main() {
  cin.tie(0) -> ios_base::sync_with_stdio(false);
  cin >> r >> c;
  for(int i=0; i<r; i++){
    string s; cin >> s;
    board.push_back(s);
  }

  for(int i=0; i<r; i++){
      if(go(i,0)) ans++;
  }
  cout << ans;
}