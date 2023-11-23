#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <queue>
#include <set>
#include <string>
#include <stack>
#include <map>
using namespace std;

int arr[1'000'002];
int result[1'000'002];


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	memset(result, -1, sizeof(result));

	int n;
	cin >> n;
	stack<int> s;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		while (s.size() && arr[s.top()] < arr[i]) {
			result[s.top()] = arr[i];
			s.pop();
		}
		s.push(i);
	}
	for (int i = 0; i < n; i++) {
		cout << result[i] << " ";
	}
}
