#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    
    for(int i=1;i<=yellow;i++) {
        if(yellow%i != 0) { continue; }
        int temp = yellow/i;
        
        if((temp+2) * (i+2) == brown+yellow && temp >= i) {
            answer.push_back(temp+2);
            answer.push_back(i+2);
            break;
        }
    }
    
    return answer;
}