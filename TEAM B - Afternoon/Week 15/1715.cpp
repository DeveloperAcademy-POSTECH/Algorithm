//
//  main.cpp
//  1715
//  카드정렬하깅
//  Created by 신정연 on 2023/09/05.
//
//  걍 합 중에 제일 작은거부터 시작하면 되나??
// -> 우선순위 큐를 쓴다 왜냐면 작은 순서대로 정렬되니까

#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int N, result = 0;
priority_queue<int, vector<int>, greater<int>> PQ;

int main(){
    
    cin >> N;
    
    //예외처리 안해서 틀려따
    if(N==1){
        cout << 0;
        return 0;
    }
    
    int x;
    for(int i=0;i<N;i++){
        cin >> x;
        PQ.push(x);
    }
    
    while(!PQ.empty()){
        int cnt = 0;
        cnt += PQ.top();
        PQ.pop();
        if(!PQ.empty()){
            cnt += PQ.top();
            // PQ에서 제일 작은 묶음 꺼내서 cnt에 합쳐
            PQ.pop();
            if(!PQ.empty()){
                //아직도 묶음이 남아있으면 다시 PQ에 넣어
                PQ.push(cnt);
            }
        }
        //다 합쳤어
        result += cnt;
    }
    cout << result;
    
    return 0;
}
