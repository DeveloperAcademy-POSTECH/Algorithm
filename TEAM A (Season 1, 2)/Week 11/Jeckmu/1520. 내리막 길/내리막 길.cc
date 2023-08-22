#include <algorithm>
#include <iostream>
#include <vector>
#define init cin.tie(0)->ios_base::sync_with_stdio(0);

typedef long long ll;
using namespace std;

int v[502][502];
ll dp[502][502];
int M, N;

int dfs(int i, int j) {
    if (i < 1 || i > M || j < 1 || j > N) return 0;
    if (i == M && j == N) return 1;
    if (dp[i][j] != -1) return dp[i][j];

    ll ret = 0;
    if (v[i][j] > v[i + 1][j]) ret += dfs(i + 1, j);
    if (v[i][j] > v[i][j + 1]) ret += dfs(i, j + 1);
    if (v[i][j] > v[i - 1][j]) ret += dfs(i - 1, j);
    if (v[i][j] > v[i][j - 1]) ret += dfs(i, j - 1);

    return dp[i][j] = ret;
}

int main() {
    init;

    cin >> M >> N;

    int h;
    for (int i = 1; i < M + 1; i++) {
        for (int j = 1; j < N + 1; j++) {
            cin >> h;
            v[i][j] = h;
        }
    }
    for (int i = 0; i < M + 2; i++) {
        v[i][N + 1] = 10001;
        v[i][0] = 10001;
    }
    for (int j = 0; j < N + 2; j++) {
        v[M + 1][j] = 10001;
        v[0][j] = 10001;
    }

    fill(&dp[0][0], &dp[M][N], -1);

    cout << dfs(1, 1);
}