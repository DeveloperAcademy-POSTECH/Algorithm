#include <iostream>
#include <vector>
#include <unordered_map>
#include <math.h>
using namespace std;

int n;
unordered_map<int, int> m;

bool isPrime(int n) {
    if(n<=1) {  return false;  }

    for(int i=2; i<=sqrt(n); i++) {
        if((n%i)==0) {
            return false;
        }
    }
    return true;
}

int main() {
  cin.tie(0)->ios_base::sync_with_stdio(0);

  cin >> n;
  vector<bool> v(n+1, 1); //0~n이 소수인지 아닌지 판별

  //에라토스테네스의 체
  for (int i = 2; i*i <= n; i++) {
    if (v[i] == 0) continue;
    for (int j = i+i; j <= n; j+=i) {
      v[j] = 0; //j는 i의 배수이기 때문에 소수가 아님
    }
  }
  vector<int> prime;
  for (int i = 2; i <= n; i++) {
    if(v[i]) prime.push_back(i);//v[i]가 1인 값만 prime 벡터에 추가하여 연속된 소수의 집합 생성
  }

  for(int i=0; i<prime.size(); i++){
    int sum = 0;
    for(int j=i; j<prime.size(); j++){
      sum += prime[j];
      if(sum > n) break;
      m[sum]++;
    }
  }

  cout << m[n];

  return 0;
}