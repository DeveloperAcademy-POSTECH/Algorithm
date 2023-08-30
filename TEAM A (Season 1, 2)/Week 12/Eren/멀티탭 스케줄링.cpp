//
//  main.cpp
//  algorithm
//
//  Created by moon on 2023/08/28.
//

#include <iostream>
#include <vector>
using namespace std;

int n, k;
vector<int> tasks;
int multitap[102];
int ans;

bool wasPlugged(int task) {
    for(int i=0; i<n; i++){
        if(multitap[i] == task) return true;
        if(multitap[i] == 0){ multitap[i] = task;  return true; }
    }
    return false;
}

void changePlug(int cur) {
    int idx = -1;
    int pos = -1;
    
    for(int i=0; i<n; i++){ // 멀티탭 다 확인
        int tmp = 0;
        for(int nxt = cur+1; nxt < k; nxt++){
            if(multitap[i] == tasks[nxt]) break;
            tmp++;
        }
        
        if(tmp > idx){
            pos = i;
            idx = tmp;
        }
    }
    multitap[pos] = tasks[cur];
    ans++;
}

int main(int argc, const char * argv[]) {
    cin.tie(0)-> ios_base::sync_with_stdio(0);
    
    cin >> n >> k;
    for(int i=0; i<k; i++){
        int t; cin >> t;
        tasks.push_back(t);
    }
    
    for(int& task: tasks) {
        // 이미 꽂혀있으면 넘기고 빈칸이 있다면 꽂아라
        if(wasPlugged(task))
            continue;
        
        int i = &task - &tasks[0];
        
        changePlug(i);
    }
    cout << ans;
    
    
    
}
