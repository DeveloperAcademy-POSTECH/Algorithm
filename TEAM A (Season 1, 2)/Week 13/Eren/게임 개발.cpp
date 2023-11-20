#include<iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n;
int dep[505];
bool done[505];

vector<int> childs[505];
int buildingTime[505];
int result[505];
queue<int> q;

void bfs() {
	while (q.size()) {
		auto here = q.front(); q.pop();
		// result[here] = max(result[here], buildingTime[here]);

		for (auto there : childs[here]) {
			result[there] = max(result[there], result[here] + buildingTime[there]);
			dep[there]--;

			if (dep[there] == 0)
				q.push(there);
		}
	}
}

int main()
{
	cin >> n;
	for (int i = 1; i <= n; i++) {
		int buildTime, num;
		cin >> buildTime;
		buildingTime[i] = buildTime;
		result[i] = buildTime;
		while (cin >> num) {
			if (num == -1) break;
			dep[i]++;
			childs[num].push_back(i);
		}
	}

	for (int i = 1; i <= n; i++) {
		if (dep[i] == 0)
			q.push(i);
	}
	bfs();
	for (int i = 1; i <= n; i++) {
		cout << result[i] << endl;
	}

}