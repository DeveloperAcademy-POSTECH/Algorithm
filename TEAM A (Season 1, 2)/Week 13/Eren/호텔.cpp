#include <iostream>
#include <vector>
#include <queue>
#include <iomanip>
using namespace std;

#define INF 1e9
#define ii pair<int, int>
#define iii tuple<int, int, int>

int c, n;
vector<ii> cities;

int cost[1400]; 

int block(int cur, int price) { 

  if(cost[cur] <= price) {
    return INF;
  }
  if(cur >= c) {
    return cost[cur] = min(cost[cur], price);
  }

  cost[cur] = min(cost[cur], price);

  int cal = INF;

  for(auto [city_cost, customer]: cities) {
    cal = min(cal, block(cur + customer, cost[cur] + city_cost));
  }

  return cal;
}

int main() {
  cin.tie(0)->ios_base::sync_with_stdio(0);
  cin >> c >> n;
  for(int i=0; i<n; i++){
    int a, b;
    cin >> a >> b;
    cities.push_back({a, b});
  }
  fill(cost, cost+1400, INF);
  cout << block(0, 0);

}
