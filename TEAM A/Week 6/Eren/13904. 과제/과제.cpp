#include <iostream>
#include <tuple>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

#define ii pair<int, int>

int n;

vector<ii> v;

priority_queue<int> pq;

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		int a, b; cin >> a >> b;
		v.push_back({ a, b });
	}

	sort(v.begin(), v.end(), greater<ii>());
	int i = 0;
	int ans = 0;

	for (int day = v[0].first; day >= 1; day--) {
		while (i < n && v[i].first >= day) {
			pq.push(v[i].second);
			i++; 
		}
		if (pq.size()) {
			ans += pq.top();
			pq.pop();
		}
	}
	cout << ans;

}