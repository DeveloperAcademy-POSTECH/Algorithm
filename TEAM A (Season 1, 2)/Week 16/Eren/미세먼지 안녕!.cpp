#include <iostream>
#include <vector>
#include <memory.h>
#include <algorithm>
using namespace std;

#define row 53
#define col 53
int n, m;
int map[row][col];
int addition[row][col];
int t;

int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,1,0,-1 };
vector<pair<int, int>> v;

void counterClockWise()
{
	int a = v[0].first;
	for (int i = a-1; i >= 2; i--)
	{
		swap(map[i][1], map[i - 1][1]);
	}
	for (int j = 1; j < m; j++)
	{
		swap(map[1][j], map[1][j + 1]);
	}
	for (int i = 1; i < a; i++)
	{
		swap(map[i][m], map[i + 1][m]);
	}
	for (int j = m; j >= 3; j--)
	{
		swap(map[a][j], map[a][j - 1]);
	}
	map[a][2] = 0;
}
void clockWise()
{
	int a = v[1].first;
	for (int i = a + 1; i <= n-1; i++)
	{
		swap(map[i][1], map[i + 1][1]);
	}
	for (int j = 1; j <= m-1; j++)
	{
		swap(map[n][j], map[n][j + 1]);
	}
	for (int i = n; i >= a+1; i--)
	{
		swap(map[i][m], map[i - 1][m]);
	}
	for (int j = m; j >= 3; j--)
	{
		swap(map[a][j], map[a][j - 1]);
	}
	map[a][2] = 0;
}

void diffusion(int a, int b)
{
	int amount = map[a][b] / 5;

	int cnt = 0;
	for (int i = 0; i < 4; i++)
	{
		int xx = a + dx[i];
		int yy = b + dy[i];
		if (map[xx][yy] >= 0) {
			addition[xx][yy] += amount;
			cnt++;
		}
	}
	map[a][b] -= amount * cnt;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin >> n >> m >> t;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++) {
			cin >> map[i][j];
			if (map[i][j] == -1)
				v.push_back({ i,j });
		}

	for (int i = 0; i <= n; i++)
	{
		map[i][0] = -2;
		map[i][m+1] = -2;
	}
	for (int i = 0; i <= m; i++)
	{
		map[0][i] = -2;
		map[n+1][i] = -2;
	}


	while (t-- > 0)
	{
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				if (map[i][j] >= 5)
				{
					diffusion(i, j);
				}
			}
		}
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				if (addition[i][j] > 0)
				{
					map[i][j] += addition[i][j];
				}
			}
		}
		memset(addition, 0, sizeof(addition));
		counterClockWise();
		clockWise();
	}
	int sum = 0;
	for(int i=1; i<=n; i++)
		for (int j = 1; j <= m; j++)
		{
			if (map[i][j] > 0)
				sum += map[i][j];
		}
	cout << sum;
}
