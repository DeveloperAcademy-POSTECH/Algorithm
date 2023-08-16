#include <iostream>
#include <vector>
#include <queue>
#include <map>
using namespace std;
#define init ios_base::sync_with_stdio(false); cout.tie(0); cin.tie(0);

vector<int> graph[32'003];
queue<int> q;
int cnt[32'003];

int n, m;

void topologicalSort() {
	while (q.size()) {
		int here = q.front(); q.pop(); 
		cout << here << ' ';

		for (auto there : graph[here]) {
			cnt[there]--;
			if (cnt[there] == 0) {
				q.push(there);
			}
		}
	}
}

int main() {
	init;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		graph[a].push_back(b);
		cnt[b]++;
	}

	for (int i = 1; i <= n; i++) {
		if (cnt[i] == 0) q.push(i);
	}
	topologicalSort();

}