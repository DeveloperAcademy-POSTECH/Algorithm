#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// https://velog.io/@yuiop1029/프로그래머스-체육복

int solution(int n, vector<int> lost, vector<int> reserve) {
    // 본인 체육복 먼저 하고
    for(int i=0; i<lost.size();i++){
        for(int j=0; j<reserve.size();j++){
            if(lost[i]==reserve[j]){
                lost.erase(lost.begin()+i);
                reserve.erase(reserve.begin()+j);
                i=-1;
                break;
            }
        }
    }

    int answer = n-lost.size();
    sort(lost.begin(), lost.end());
    sort(reserve.begin(), reserve.end());
    // 적은 학생꺼를 
    for(int i=0; i<lost.size();i++){
        for(int j=0; j<reserve.size();j++){
            if(lost[i]-1==reserve[j] || lost[i]+1 == reserve[j]) {
                answer++;
                reserve.erase(reserve.begin()+j);
                break;
            }
        }
    }
    
    return answer;
}
