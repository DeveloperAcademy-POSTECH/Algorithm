#include <iostream>
#include <tuple>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int n;
vector<int> v;
vector<int> twoSum;

int main() {

	cin >> n;
	for (int i = 0; i < n; i++) {
		int a; cin >> a; 
		v.push_back(a);
	}
	sort(v.begin(), v.end());

	for (int i = 0; i < n; i++) {
		for (int j = i; j < n; j++) {
			twoSum.push_back(v[i] + v[j]);
		}
	}
	sort(twoSum.begin(), twoSum.end());

	for (int i = v.size() - 1; i >= 0; i--) {
		bool possible = false;
		for (int j = 0; j < v.size(); j++) {
			int wanted = v[i] - v[j];
			auto iter = lower_bound(twoSum.begin(), twoSum.end(), wanted);
			if (*iter == wanted) {
				possible = true;
				break;
			}
		}
		if (possible) {
			cout << v[i];
			break;
		}
	}
}