#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define INF 2e9
#define ii pair<int, int>

int n, l;

vector<ii> water;

int main() {
  cin >> n >> l;
  for(int i=0; i<n; i++){
    int st, en;
    cin >> st >> en;
    water.push_back({st, en});
  }
  sort(water.begin(), water.end());
  int ans = 0;

  int last = -2;

  for(int i=0; i<water.size(); i++) {

    int st = water[i].first;
    int en = water[i].second;

    st = max(st, last);

    int length = en - st;

    if(length <= 0) continue;

    int cnt = length / l;
    if(length % l != 0) cnt++;
    ans += cnt;
    last = st + cnt * l;
  }
  cout << ans;


}