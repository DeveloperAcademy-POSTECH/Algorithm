#include <bits/stdc++.h>
using namespace std;
#define init cin.tie(0)->sync_with_stdio(0)
#define ii pair<int, int>

int t, n;
int p[10005];

ii get_depth(int x, int y) {
    int depA = 0;
    int depB = 0;

    while(p[x] != -1) {
      x = p[x];
      depA++;
    }
    while(p[y] != -1) {
      y = p[y];
      depB++;
    }

    return {depA, depB};
}

int main() {
  init;
  cin >> t;
  while(t-- > 0) {
    cin >> n;
    fill(p, p+n+1, -1);

    int a, b;
    while(n-- > 1) {
      cin >> a >> b;
      p[b] = a;
    }
    cin >> a >> b;

    auto [depA, depB] = get_depth(a, b);

    while(depA < depB) {
      b = p[b]; 
      depB--;
    }
    while(depA > depB) {
      a = p[a];
      depA--;
    }

    for(int i=0; i<depA; i++) {
      if(a == b) break;
      a = p[a];
      b = p[b];
    }
    cout << a << '\n';

  }
}