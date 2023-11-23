#include <iostream>
#include <vector>
#include <map>
using namespace std;

#define INF 2e9

int n, m;

#define mod 1'234'567



int d[1004][10];

int main() {
  for(int i=0; i<10; i++) {
    d[1][i] = 1;
  }
  for(int i=2; i<1002; i++) {
        d[i][0] += (d[i-1][7]) % mod;
        d[i][1] += (d[i-1][4] + d[i-1][2]) % mod;
        d[i][2] += (d[i-1][1] + d[i-1][3] + d[i-1][5]) % mod;
        d[i][3] += (d[i-1][2] + d[i-1][6]) % mod;
        d[i][4] += (d[i-1][1] + d[i-1][5] + d[i-1][7]) % mod;
        d[i][5] += (d[i-1][2] + d[i-1][4] + d[i-1][6] + d[i-1][8]) % mod;
        d[i][6] += (d[i-1][3] + d[i-1][5] + d[i-1][9]) % mod;
        d[i][7] += (d[i-1][4] + d[i-1][8] + d[i-1][0]) % mod;
        d[i][8] += (d[i-1][5] + d[i-1][7] + d[i-1][9]) % mod;
        d[i][9] += (d[i-1][6] + d[i-1][8]) % mod;
  }

  int t;
  cin >> t;
  while(t-->0) {
    int n;
    cin >> n;
    int ans = 0;
    for(int i=0; i<10; i++) {
      ans += d[n][i];
    }
    ans %= mod;
    cout << ans << '\n';
  }
}