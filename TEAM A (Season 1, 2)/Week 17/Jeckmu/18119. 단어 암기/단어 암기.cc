#include <algorithm>
#include <bitset>
#include <iostream>
#include <set>
#include <string>
#include <vector>
#define init cin.tie(0)->ios_base::sync_with_stdio(0);

using namespace std;

int main() {
    init;

    int N, M;
    cin >> N >> M;
    int s = 0;

    // 알파벳 26개 기억. (기억 -> 0 / 잊음 -> 1)
    s |= (1 << 26) - 1;

    // 문자열을 bitmasking하여 저장 (알파벳의 개수는 상관없으므로, 무슨 알파벳이 들어왔는지만.)
    vector<int> list;
    string temp = "";
    for (int i = 0; i < N; i++) {
        cin >> temp;
        int t = 0;
        for (int j = 0; j < temp.length(); j++) {
            t |= (1 << (temp[j] - 'a'));
        }
        list.push_back(t);
    }

    // 쿼리 실행
    int command;
    char ch;
    for (int i = 0; i < M; i++) {
        cin >> command >> ch;
        int cnt = 0;
        if (command == 1) {
            // 입력된 문자 잊기. (bitmask 삭제)
            s &= ~(1 << (ch - 'a'));
        } else {  // command == 2
            // 입력된 문자 기억하기. (bitmask 추가)
            s |= (1 << (ch - 'a'));
        }

        for (int j = 0; j < N; j++) {
            if ((s & list[j]) == list[j]) {
                cnt++;
            }
        }
        cout << cnt << "\n";
    }
}
