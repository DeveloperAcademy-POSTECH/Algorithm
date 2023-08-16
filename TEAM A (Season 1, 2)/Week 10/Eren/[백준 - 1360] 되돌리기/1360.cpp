#include<iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <set>
using namespace std;

int n;
struct Commit {
	string content;
	int t;
	Commit(string _content, int _t) {
		content = _content;
		t = _t;
	}
};

list<Commit> myLog;

int main()
{
	cin.tie(0)->ios_base::sync_with_stdio(0);
	cin >> n;
	int t;
	myLog.push_back(Commit("", 0));
	while (n-- > 0) {
		string cmd;
		char c;
		int undo;
		cin >> cmd;
		if (cmd == "type") {
			cin >> c >> t;
			auto iter = myLog.rbegin();
			string prevContent = (*iter).content;
			myLog.push_back(Commit(prevContent + c, t));
		}
		else {
			cin >> undo >> t;
			int pastTime = t - undo - 1;
			if (pastTime <= 0) {
				myLog.push_back(Commit("", t));
			}
			else {
				auto pastCommit = myLog.rbegin();
				for (; pastCommit != myLog.rend(); pastCommit++) {
					if ((*pastCommit).t <= pastTime) {
						break;
					}
				}
				Commit tmp = *pastCommit;
				tmp.t = t;
				myLog.push_back(tmp);
			}
		}
	}
	cout << (*myLog.rbegin()).content << endl;
}
