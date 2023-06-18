#define ii pair<int, int>
#include<vector>
#include<algorithm>
using namespace std;
int solution(vector<int> queue1, vector<int> queue2) {
	int answer = INT32_MAX;
	long long sum = 0;
	int dataCnt = queue2.size();
	for (int i = 0; i < dataCnt; i++) {
		sum += queue1[i];
		sum += queue2[i];
		queue1.push_back(queue2[i]);
	}
	long long half = sum / 2;
	vector<ii> candidate;
	long long part = 0;
	int a = 0;
	int b = 0;
	while (b < queue1.size()) {
		if (part < half)
			part += queue1[b++];
		else if (part > half)
			part -= queue1[a++];
		else {
			candidate.push_back({ a,b - 1 });
			part -= queue1[a++];
		}
	}
	if (candidate.size() == 0)
		return -1;

	for (auto p : candidate) {
		if (p.second < dataCnt) {
			if (p.second == dataCnt - 1) answer = min(answer, p.first);
			else answer = min(answer, dataCnt + p.first + p.second + 1);
		}
		else if (p.first >= dataCnt) {
			if (p.second == dataCnt * 2 - 1) answer = min(answer, p.first + 1 - dataCnt);
			else answer = min(answer, p.second + 1 + p.first - dataCnt);
		}
		else {
			answer = min(answer, p.first + p.second + 1 - dataCnt);
		}
	}

	return answer;
}