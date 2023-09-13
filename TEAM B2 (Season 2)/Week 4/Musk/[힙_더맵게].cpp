#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(vector<int> scoville, int K) {
    priority_queue<int, vector<int>, greater<int> > q(scoville.begin(), scoville.end());
    
    int answer = 0;
    while(q.top()<K && q.size() > 1) {
        int oneFood = q.top();
        q.pop();

        int twoFood = q.top();
        q.pop();
    
        q.push(oneFood + (twoFood*2));
        answer++;
    }
    
    if(q.top() < K) { return -1; }
    return answer;
}