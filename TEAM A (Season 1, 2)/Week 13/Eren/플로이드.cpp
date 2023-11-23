#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <cstring>
using namespace std;
#define init ios_base::sync_with_stdio(false); cout.tie(0); cin.tie(0);
#define ii pair<int, int>

int T;
int N, M, Q;

int D[103][103];


int main() {
	init;
	cin >> N >> M;

	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= N; j++)
			D[i][j] = 987654321;

	for (int i = 1; i <= N; i++)
		D[i][i] = 0;

	for (int i = 0; i < M; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		D[a][b] = min(D[a][b], c);
	}

	for (int vpn = 1; vpn <= N; vpn++) {

		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				D[i][j] = min(D[i][j], D[i][vpn] + D[vpn][j]);
			}
		}

	}

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (D[i][j] == 987654321) cout << 0 << ' ';
			else cout << D[i][j] << ' ';
		}
		cout << '\n';
	}
}