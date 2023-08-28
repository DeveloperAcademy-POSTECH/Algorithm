#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

// Stack / Queue를 이용한 방법이 아니라 일단 재껴놓고 다시 풀 예정
vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size());
    
    
    for(int i=0;i<prices.size();i++) {
        for(int j=i+1; j<prices.size(); j++) {
            answer[i]++;
            if(prices[i] > prices[j]) break;
        }
    }
    return answer;
}