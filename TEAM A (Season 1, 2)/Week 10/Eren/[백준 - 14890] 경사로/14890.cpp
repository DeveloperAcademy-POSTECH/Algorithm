#include <iostream>
#include <stack>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>
using namespace std;

int n, l;
int map[113][114];
bool check[113][114];
int result;

void checkRow(int r) {

	for (int i = 1; i < n; i++) {
		int here = map[r][i];
		int next = map[r][i + 1];
		if (here == next) continue;
		if (abs(here - next) > 1) return;

		if (here - next == 1) {
			for (int u = i + 1; u < i + 1 + l; u++) {
				if (u > n) return;
				if (map[r][u] != next) { return; }
				check[r][u] = true;
			}
		}
		else if (here - next == -1) {
			for (int u = i; u >= i - l + 1; u--) {
				if (u < 1) return;
				if (map[r][u] != here) return;
				if (check[r][u]) return;
			}
		}

	}
	result++;
}
void checkCol(int c) {

	for (int i = 1; i < n; i++) {
		int here = map[i][c];
		int next = map[i + 1][c];
		if (here == next) continue;
		if (abs(here - next) > 1) return;

		if (here - next == 1) {
			for (int u = i + 1; u < i + 1 + l; u++) {
				if (u > n) return;
				if (map[u][c] != next) { return; }
				check[u][c] = true;
			}
		}
		else if (here - next == -1) {
			for (int u = i; u >= i - l + 1; u--) {
				if (u < 1) return;
				if (map[u][c] != here) return;
				if (check[u][c]) return;
			}
		}

	}
	result++;
}


int main() {
	ios_base::sync_with_stdio(false); cout.tie(0); cin.tie(0);

	cin >> n >> l;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			cin >> map[i][j];

	for (int i = 1; i <= n; i++) {
		checkRow(i);
	}
	memset(check, false, sizeof(check));
	for (int i = 1; i <= n; i++) {
		checkCol(i);
	}
	cout << result;

}
