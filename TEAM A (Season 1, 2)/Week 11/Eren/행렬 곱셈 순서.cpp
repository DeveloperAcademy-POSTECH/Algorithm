#include<iostream>
#include<algorithm>
#include<vector>
#include <iomanip>
using namespace std;
#define INF 1000000000

int N, r, c;
int sum[501], matrix[501][2], dp[501][501];
int recur(int x, int y) {
  if(x == y) return 0;
  if(dp[x][y] != 0) return dp[x][y];
  dp[x][y] = INF;

  for(int sp = x; sp < y; sp++){
    dp[x][y] = min(dp[x][y], recur(x, sp) + recur(sp+1, y) + matrix[x][0] * matrix[sp][1] * matrix[y][1]);
  }

  return dp[x][y];
}

int main()
{
	cin >> N;

	for (int i = 1; i <= N; i++)
	{
		cin >> r >> c;
		matrix[i][0] = r;
		matrix[i][1] = c;
	}
  
	cout << recur(1, N);

}
