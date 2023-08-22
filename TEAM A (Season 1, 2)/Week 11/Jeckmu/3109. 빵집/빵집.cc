#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>
#define init cin.tie(0)->ios_base::sync_with_stdio(0);

using namespace std;

bool M[10001][501] = {};

bool dfs(int i, int j, int R, int C) {
    // 칸을 넘어가면 false, 마지막 열일 시 true. (기저조건)
    if (i < 0 || i >= R || j < 0 || j >= C) return false;
    if (!M[i][j]) return false;
    if (j == C - 1) return true;

    // 우측 위, 우측, 우측 아래 순으로 dfs 호출.
    if (dfs(i - 1, j + 1, R, C)) {
        M[i][j] = false;
        return true;
    }
    if (dfs(i, j + 1, R, C)) {
        M[i][j] = false;
        return true;
    }
    if (dfs(i + 1, j + 1, R, C)) {
        M[i][j] = false;
        return true;
    }
    M[i][j] = false;
    return false;
}

int main() {
    init;

    int R, C;
    cin >> R >> C;
    char ch;

    int result = 0;

    // 입력
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> ch;
            if (ch == '.') M[i][j] = true;
        }
    }

    for (int i = 0; i < R; i++) {
        if (dfs(i, 0, R, C)) result++;
    }

    cout << result;
}