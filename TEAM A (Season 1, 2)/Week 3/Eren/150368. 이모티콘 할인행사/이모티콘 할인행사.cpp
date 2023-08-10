#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define ll long long
#define iii tuple<int, int, int>
#define ii pair<int, int>

int sum;
int emoCnt;
int emoDiscount[] = {10, 20, 30, 40};

vector<vector<int>> _users;
vector<int> _emoticons;

vector<int> gather; // 뭐했ㅡㄹ까?

priority_queue<ii, vector<ii>> pq;

int k;
void dfs(){
  if(gather.size() == emoCnt){
    int subscribe = 0;
    int sumPrice = 0;


    for(auto user: _users){
      int userPrice = 0;

      for(int i=0; i<emoCnt; i++){
        if(user[0] <= gather[i]){
          userPrice += _emoticons[i] * (double(100 - gather[i]) / 100.0);
        }
      }

      if(userPrice < user[1]) sumPrice += userPrice;
      else subscribe++;
    }

    pq.push({subscribe, sumPrice});
    return;
  }

  for(int i=0; i<4; i++){
    gather.push_back(emoDiscount[i]);
    dfs();
    gather.pop_back();
  }

}

vector<int> solution(vector<vector<int>> users, vector<int> emoticons) {
    _users = users;
    _emoticons = emoticons;

    emoCnt = emoticons.size();
    vector<int> answer;

    dfs();

    auto sub = pq.top().first;
    auto price = pq.top().second;
    answer.push_back(sub);
    answer.push_back(price);

    return answer;
}

int main() {
  auto a = solution({{40, 10000}, {25, 10000}}, { 7000, 9000});
  cout << endl;
  cout << a[0] << ' ';
  cout << a[1] << ' ';
}
