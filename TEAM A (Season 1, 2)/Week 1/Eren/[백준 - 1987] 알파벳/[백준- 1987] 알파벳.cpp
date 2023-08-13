#include <iostream>
#include <queue>

using namespace std;

int R, C;

const int dx[] = { 1,0,-1,0 };
const int dy[] = { 0,-1,0,1 };

int alpha[32];

int map[22][22];

bool canGo(int nx, int ny) {
    if (nx <1 || ny < 1 || nx > R || ny > C) return false;
    int a = map[nx][ny];
    if (alpha[a] > 0) return false;

    return true;
}
int result;

void dfs(int x, int y, int cnt) {
    bool stop = true;

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (canGo(nx, ny) == false)
            continue;

        stop = false;
        int a = map[nx][ny];
        alpha[a]++;
        dfs(nx, ny, cnt + 1);
        alpha[a] = 0;
    }

    if (stop) {
        result = max(result, cnt);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> R >> C;
    for (int i = 0; i < R; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < C; j++) {
            map[i + 1][j + 1] = s[j] - 'A';
        }
    }

    int first = map[1][1];
    alpha[first] = 1;
    dfs(1, 1, 1);

    cout << result;



    return 0;
}
