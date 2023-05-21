#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <cstring>
#include <set>
using namespace std;
#define init ios_base::sync_with_stdio(false); cout.tie(0); cin.tie(0);
#define ii pair<int, int>
#define ll long long
int t;

int a, b;
int A[1002];
int B[1002];

map<int, int> aMap;
map<int, int> bMap;

int main() {
	init;
	cin >> t;

	cin >> a;
	for (int i = 0; i < a; i++)
		cin >> A[i];
	cin >> b;
	for (int i = 0; i < b; i++)
		cin >> B[i];

	for (int i = 0; i < a; i++) {
		int sum = 0;
		for (int j = i; j < a; j++) {
			sum += A[j];
			aMap[sum]++;
		}
	}
	for (int i = 0; i < b; i++) {
		int sum = 0;
		for (int j = i; j < b; j++) {
			sum += B[j];
			bMap[sum]++;
		}
	}
	long long ans = 0;
	for (auto ele : aMap) {
		if (bMap.count(t - ele.first)) {
			ans += (ll)ele.second * (ll)bMap[t - ele.first];
		}
	}

	cout << ans;
}