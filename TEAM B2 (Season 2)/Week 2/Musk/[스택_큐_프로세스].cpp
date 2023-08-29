#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm> 
using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    int count = 0;
    queue<int> q;
    queue<int> index;
    for(int i=0;i<priorities.size();i++) { 
        q.push(priorities[i]);
        index.push(i);
    }
    
    while(!q.empty()) {
        int max = *max_element(priorities.begin(), priorities.end());
        
        int temp = q.front();
        q.pop();
        int index_temp = index.front();
        index.pop();
        
        if(max == temp) {
            count++;
            vector<int>::iterator maxElementIterator = max_element(priorities.begin(), priorities.end());
             priorities.erase(maxElementIterator);
            if(index_temp == location) {
                answer = count;
                break;
            }
        }
        else {
            q.push(temp);
            index.push(index_temp);
        }
        
    }
    return answer;
}


        // int temp = priorities.front();
        // priorities.erase(priorities.begin());
        // cout << temp;