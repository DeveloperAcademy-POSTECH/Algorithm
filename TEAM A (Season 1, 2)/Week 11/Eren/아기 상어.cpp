#include <iostream>
#include <stack>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cstring>
#include <set>
using namespace std;
#define init ios_base::sync_with_stdio(false); cout.tie(0); cin.tie(0);

#define ii pair<int, int>

int map[22][22];
bool check[22][22];
queue<ii> q;
int result = 0;

int n;

const int dx[] = { -1,0,1,0 };
const int dy[] = { 0,-1,0,1 };

struct zzz {
	bool operator()(const ii& a, const ii& b) {
		if (a.first == b.first)
			return a.second > b.second;

		return a.first > b.first;
	}
};

class mini {
public:
	int level = 2;
	int food = 0;
	ii pos = { 0,0 };

	void Eat(int x, int y) {

		food++;
		map[x][y] = 0;
		pos = { x,y };
		if (food == level) {
			level++;
			food = 0;
		}
	}
};

mini m;
bool canGo(int nx, int ny) {
	if (check[nx][ny] == true) return false;
	if (nx <1 || ny < 1 || nx>n || ny > n) return false;
	if (map[nx][ny] > m.level) return false;

	return true;
}

int bfs() {
	int time = 0;
	while (q.size()) {
		int qSize = q.size();
		priority_queue<ii, vector<ii>, zzz> pq;
		time++;
		for (int i = 0; i < qSize; i++) {
			ii here = q.front(); q.pop();
			int x = here.first;
			int y = here.second;

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (canGo(nx, ny) == false) { continue; }
				check[nx][ny] = true;

				int there = map[nx][ny];

				if (there != 0 && there < m.level) {
					pq.push({ nx, ny });
				}
				q.push({ nx, ny });
			}
		}

		if (pq.size()) {
			ii go = pq.top();
			m.Eat(go.first, go.second);
			while (q.size()) q.pop();
			q.push(go);
			return time;
		}
	}
	return -1;
}



int main() {
	init;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> map[i][j];
			if (map[i][j] == 9) {
				m.pos = { i,j };
				q.push({ i,j });
				map[i][j] = 0;
			}
		}
	}

	while (true) {
		memset(check, false, sizeof(check));
		check[m.pos.first][m.pos.second] = true;

		int time = bfs();
		if (time == -1) // 못찾을때
			break;

		result += time;
	}
	cout << result;

}
