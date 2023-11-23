#include <iostream>
#include <vector>
using namespace std;

#define INF 2e9

int n;
string s;
int energy[1003];

bool canGo(char a, char b) {
  if(a == 'B' and b == 'O') return true;
  if(a == 'O' and b == 'J') return true;
  if(a == 'J' and b == 'B') return true;
  return false;
}

void dfs(int cur) {
  

  for(int nxt=cur + 1; nxt<n; nxt++) {
    if(canGo(s[cur], s[nxt])) {
        if(energy[nxt] > energy[cur] + (nxt - cur) * (nxt - cur)) {
          energy[nxt] = min(energy[nxt], energy[cur] + (nxt - cur) * (nxt - cur));
          dfs(nxt);
        }
    }
  }
}

int main() {
  cin >> n;
  cin >> s;
  fill(energy, energy + 1003, INF);
  energy[0] = 0;

  dfs(0);

  if(energy[s.size() - 1] == INF) cout << -1;
  else cout << energy[s.size() - 1];

  return 0;
}