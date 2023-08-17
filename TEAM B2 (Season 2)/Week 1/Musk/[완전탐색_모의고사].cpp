#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    vector<int> temp1 = {1,2,3,4,5};
    vector<int> temp2 = {2,1,2,3,2,4,2,5};
    vector<int> temp3 = {3,3,1,1,2,2,4,4,5,5};
    vector<int> count = {0};
    
    for(int i=0;i<answers.size();i++) {
        if (answers[i] == temp1[i%temp1.size()]) { count[0]++; }
        if (answers[i] == temp2[i%temp2.size()]) { count[1]++; }
        if (answers[i] == temp3[i%temp3.size()]) { count[2]++; }
    }
    
    int high_score = *max_element(count.begin(), count.end());
    
    for(int i=0;i<count.size();i++) {
        if(high_score == count[i]) { answer.push_back(i+1); }
    }
    
    return answer;
}