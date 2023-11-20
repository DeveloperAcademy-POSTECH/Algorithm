#include <iostream>
#include <vector>
#include <map>
using namespace std;

#define INF 2e9

int n, m;



int word[10004];

int remember = 0;

int main() {
  for(int i=0; i<26; i++) {
    remember += (1 << i); // 10진법에서  9자리인거지, 2진법에서는 훨씬 많다.
  }

  cin >> n >> m;
  for(int i=0; i<n; i++){
    string str; cin >> str;
    for(auto& c: str) {
      word[i] |= 1 << (c - 'a');
    }
  }

  for(int i=0; i<m; i++) {
    int cnt = 0;
    int command;
    char c;
    cin >> command >> c;
    int c2i = c - 'a';

    remember ^= (1 << c2i);

    for(int j=0; j<n; j++) {
      if((remember & word[j]) != word[j]) continue;
      cnt++;
    }
    cout << cnt << '\n';
  }
}