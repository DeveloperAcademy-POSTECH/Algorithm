#include <bits/stdc++.h>
using namespace std;
#define init cin.tie(0)->sync_with_stdio(0)

int n, k;
int arr[300'003];
int diff[300'003];

int main() {
  init;
  cin >> n >> k;
  for(int i=0; i<n; i++) cin >> arr[i];
  for(int i=0; i<n; i++) {
    diff[i] = arr[i+1] - arr[i];
  }

  sort(diff, diff+n-1);

  int ans = 0;
  for(int i=0; i<n-k; i++){
    ans += diff[i];
  }
  cout << ans;

}