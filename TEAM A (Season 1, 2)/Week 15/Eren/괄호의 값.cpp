#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <stack>
using namespace std;

#define INF 2e9
#define ii pair<int, int>

string str;
vector<char> v;
int ans;
bool possible = true;

void onFail() {
	possible = false;
}

vector<ii> score;

void sum() {
	auto last = score.rbegin();
	auto [num, dep] = *last;
	
	int sum = 0;
	while(dep == (*score.rbegin()).second) {
		sum += (*score.rbegin()).first;
		score.pop_back();
	}
	score.push_back({sum, dep});
}

int main() {
	cin.tie(0)->ios_base::sync_with_stdio(0);
	cin >> str;
	
	score.push_back({-2, -2});
	
	for(char x: str) {
		if(x == '(' or x == '[') {
			v.push_back(x);
			continue;
		}
		
		if(x == ')') {
			if(v.empty()) { onFail(); break; }
			if(*v.rbegin() != '(') { onFail(); break; }
			v.pop_back();
			
			auto last = score.rbegin();
			auto [num, dep] = *last;
			
			
			if(dep == v.size() + 1) {
				score.pop_back();
				score.push_back({num * 2, v.size()});
			}
			else {
				score.push_back({2, v.size()});
			}
			
			sum();
		}
		
		if(x == ']') {
			if(v.empty()) { onFail(); break; }
			if(*v.rbegin() != '[') { onFail(); break; }
			v.pop_back();
			
			auto last = score.rbegin();
			auto [num, dep] = *last;
			
			if(dep == v.size() + 1) {
				score.pop_back();
				score.push_back({num * 3, v.size()});
			}
			else {
				score.push_back({3, v.size()});
			}
			
			sum();
		}
	}
	if(score.size() != 2) possible = false;
	
	if(possible == false) cout << 0;
	else cout << (*score.rbegin()).first;
	
}
