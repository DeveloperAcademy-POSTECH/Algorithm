#include <iostream>
#include <queue>
#include <vector>
#include <map>
using namespace std;

int n, m;
bool arr[60];
vector<vector<int>> v(60);
vector<vector<int>> map(60);
int result;
int unf[55];
vector<int> vv;
bool check[60];

int Find(int v)
{
	if (v == unf[v]) return unf[v];
	else return Find(unf[v]);
}

void Union(int a, int b)
{
	a = Find(a);
	b = Find(b);
	if (a != b) unf[a] = b;
}

void Infect(int a)
{
	if (arr[a] == false) {
		arr[a] = true;
		for (int i = 1; i <= n; i++)
		{
			if (unf[i] == a)
				Infect(i);
		}
		Infect(unf[a]);
	}
}


int main()
{
	ios_base::sync_with_stdio(false);
	cin >> n >> m;
	result = m;

	for (int i = 1; i <= n; i++)
		unf[i] = i;

	int known = 0;
	cin >> known;
	for (int i = 1; i <= known; i++) {
		int num;
		cin >> num;
		vv.push_back(num);
	}

	for (int i = 1; i <= m; i++)
	{
		int personCount;
		cin >> personCount;
		int prev;
		for (int j = 1; j <= personCount; j++) 
		{
			int num;
			cin >> num;
			v[i].push_back(num);
			if (j >= 2) {
				Union(prev, num);
			}
			prev = num;
		}
	}

	for (int i = 0; i < vv.size(); i++)
	{
		if (arr[vv[i]] == true)
			continue;
		Infect(vv[i]);
	}

	for (int i = 1; i <= m; i++)
	{
		for (int j = 0; j < v[i].size(); j++)
		{
			if (arr[v[i][j]])
			{
				result--;
				break;
			}
		}
	}

	cout << result;

}
