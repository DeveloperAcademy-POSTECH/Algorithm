#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#define init cin.tie(0)->ios_base::sync_with_stdio(0);

using namespace std;

int main() {
    init;

    set<int> s;
    vector<int> v;

    int N, Q, a, q, x, p;
    int DH = 1;
    cin >> N >> Q;
    for (int i = 1; i < N + 1; i++) {
        cin >> a;
        if (a) s.insert(i);
    }

    set<int>::iterator iter;

    for (int i = 0; i < Q; i++) {
        cin >> q;
        if (q == 1) {
            cin >> x;
            if (s.count(x))
                s.erase(x);
            else
                s.insert(x);
        } else if (q == 2) {
            cin >> x;
            DH = (DH - 1 + x) % N + 1;
        } else {
            if (s.empty()) {
                v.push_back(-1);
            } else {
                auto p = s.lower_bound(DH);
                if (p != s.end())
                    v.push_back(*p - DH);
                else
                    v.push_back(*s.begin() - DH + N);
            }
        }
    }
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << "\n";
    }
}
