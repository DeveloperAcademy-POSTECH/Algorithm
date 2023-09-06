#include <iostream>
using namespace std;

int arr[101][101] = { 0, };
long long MAX = 0;

long long sum(int sx, int sy, int ex, int ey) {
    long long ret = 0;
    for (int i = sy; i <= ey; i++) {
        for (int j = sx; j <= ex; j++) {
            ret += arr[i][j]; //합해준다.
        }
    }
    return ret;
}

int main() {
    int N, M;
    cin >> N >> M;
    string s;
    for (int i = 0; i < N; i++) {
        cin >> s;
        for (int j = 0; j < M; j++) {
            int num = s[j] - '0';
            arr[i][j] = num;
        }
    }
    //직사각형을 나누는 방법은 총 6가지이다.
    //각 꼭지점의 인덱스를 알고 sum에 들어가자

    // 1번 case
    for (int i = 0; i < M - 2; i++) {
        for (int j = i + 1; j < M - 1; j++) {
            long long a = sum(0, 0, i, N - 1);
            long long b = sum(i + 1, 0, j, N - 1);
            long long c = sum(j + 1, 0, M - 1, N - 1);
            if (MAX < a * b * c)
                MAX = a * b * c;
        }
    }

    // 2번 case
    for (int i = 0; i < N - 2; i++) {
        for (int j = i + 1; j < N - 1; j++) {
            long long a = sum(0, 0, M - 1, i);
            long long b = sum(0, i + 1, M - 1, j);
            long long c = sum(0, j + 1, M - 1, N - 1);
            if (MAX < a * b * c)
                MAX = a * b * c;
        }
    }

    // 3번 case
    for (int i = 0; i < M - 1; i++) {
        for (int j = 0; j < N - 1; j++) {
            long long a = sum(0, 0, i, N - 1);
            long long b = sum(i + 1, 0, M - 1, j);
            long long c = sum(i + 1, j + 1, M - 1, N - 1);
            if (MAX < a * b * c)
                MAX = a * b * c;
        }
    }

    // 4번 case
    for (int i = M - 1; i > 0; i--) {
        for (int j = 0; j < N - 1; j++) {
            long long a = sum(i, 0, M - 1, N - 1);
            long long b = sum(0, 0, i - 1, j);
            long long c = sum(0, j + 1, i - 1, N - 1);
            if (MAX < a * b * c)
                MAX = a * b * c;
        }
    }

    // 5번 case
    for (int i = 0; i < N - 1; i++) {
        for (int j = 0; j < M - 1; j++) {
            long long a = sum(0, 0, M - 1, i);
            long long b = sum(0, i + 1, j, N - 1);
            long long c = sum(j + 1, i + 1, M - 1, N - 1);
            if (MAX < a* b* c)
                MAX = a * b * c;
        }
    }

    // 6번 case
    for (int i = N - 1; i > 0; i--) {
        for (int j = 0; j < M - 1; j++) {
            long long a = sum(0, i, M - 1, N - 1);
            long long b = sum(0, 0, j, i - 1);
            long long c = sum(j + 1, 0, M - 1, i - 1);
            if (MAX < a * b * c)
                MAX = a * b * c;
        }
    }

    //만약 long long 타입을 출력하고자하면 lld로 써야한다.

    cout << MAX;
    return 0;

}
