#include <string>
#include <vector>
#include <iostream>

using namespace std;


vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int isComplete = 0;
    
    while(isComplete < progresses.size()) {
        int temp = 0;
        
        for(int i=isComplete;i<progresses.size();i++) {
            if(progresses[i] >= 100 && isComplete == i) { 
                temp++;
                isComplete++;
            }
            progresses[i] += speeds[i];
        }
        
        if(temp > 0) { answer.push_back(temp); }
    }
    
    
    
    return answer;
}

// vector<int> solution(vector<int> progresses, vector<int> speeds) {
//     vector<int> answer;
//     int isComplete = 0;
    
//     while(isComplete < progresses.size()) {
//         int temp = 0;
        
//         for(int i=0;i<progresses.size();i++) {
//             if((progresses[i] < 100) && (progresses[i] + speeds[i] >= 100)) {
//                 temp++;
//                 isComplete++;
//             }
//             progresses[i] += speeds[i];
//         }
//         if(temp > 0) { answer.push_back(temp); }
//     }
//     return answer;
// }