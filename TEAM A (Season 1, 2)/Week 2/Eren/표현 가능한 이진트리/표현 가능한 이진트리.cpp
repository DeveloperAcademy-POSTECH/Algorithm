#include <iostream>
#include <vector> 
#include <queue>
using namespace std;

#define ii pair<int, int>

int par[200];

bool chk(vector<int>& gogo){
  int n = gogo.size(); // 1 3 7 15 31 63
  if(!gogo[n/2]) return false;
  for(int i=0; i<n; i++){
    if(i == n/2) continue;
    if(!gogo[i]) continue;
    if(gogo[i] && !gogo[par[i+1]-1]) return false;
  }
  return true;
}

vector<int> solution(vector<long long> numbers){
  par[1] = 2;
  par[3] = 2;
  int cur = 3;
  while(cur <= 31){
    for(int i=1; i<=cur; i++){
      par[i + cur + 1] = par[i] + (cur+1);
    }

    par[(cur+1)/2] = cur + 1;
    par[3*(cur+1)/2] = cur + 1;

    cur = cur * 2 + 1;
  }

  vector<int> ret;
  for(auto num: numbers){
    vector<int> z;
    while(num){
      z.push_back(num%2);
      num/=2;
    }

    bool possible = false;
    for(auto sz : {1,3,7,15,31,63}){
      if(z.size() > sz) continue;
      vector<int> gogo = z;
      while(gogo.size() < sz) gogo.push_back(0);
      if(chk(gogo)){
        possible = true;
        break;
      }
      else{ break;}
        
    }
    if(possible) ret.push_back(1);
    else ret.push_back(0);
  }
    

    return ret;
}