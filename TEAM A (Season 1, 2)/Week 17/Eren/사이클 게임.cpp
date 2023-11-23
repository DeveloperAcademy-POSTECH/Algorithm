#include <iostream>
#include <vector>
using namespace std;

#define INF 2e9

int n, m;

int par[500'005];

int find(int x) {
  if(x == par[x]) return x;
  
  return par[x] = find(par[x]);
}


int main() {
  for(int i=0; i<500'005; i++){
    par[i] = i;
  }

  cin >> n >> m;
  int ans = 0;

  for(int i=0; i<m; i++) {
    int a, b;
    cin >> a >> b;

    int par_a = find(a);
    int par_b = find(b);

    if(par_a != par_b) {
      par[par_b] = par_a;
    }
    else if(par_a == par_b) {
      ans = i; 
      break;
    }
  }
  if(ans == 0) cout << 0;
  else cout << ans + 1;
}