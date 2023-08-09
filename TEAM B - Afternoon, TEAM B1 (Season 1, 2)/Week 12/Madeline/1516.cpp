//
//  main.cpp
//  1516
//  게임 개발
//  Created by 신정연 on 2023/07/26.
//

#include <iostream>
#include <vector>
#include <queue>

#define MAX 502

using namespace std;

int N;
int inDegree[MAX];
//시간!! 추가
int Time[MAX];
vector<int> building[MAX];
int result[MAX];
queue<int> q;

void topologysort(){
    for(int i=1;i<=N;i++){
        if(inDegree[i]==0){
            q.push(i);
            result[i] = Time[i];
        }
    }
    while(!q.empty()){
        int x = q.front();
        q.pop();
        for(int i=0;i<building[x].size();i++){
            int y = building[x][i];
            
            result[y] = max(result[y], Time[y] + result[x]);
            inDegree[y]--;
            
            if(inDegree[y]==0){
                q.push(y);
            }
        }
    }
//    for(int i=1;i<=N;i++){
//        if(q.empty()){
//            return;
//        }
//        int x = q.front();
//        q.pop();
//
//        result[i] = Time[x];
//
//        for(int i=0;i<building[x].size();i++){
//            int y = building[x][i];
//
//            result[y] = max(result[y], Time[y] + result[x]);
//            inDegree[i]--;
//
//            if(inDegree[i]==0){
//                q.push(y);
//            }
//        }
//    }
    for(int i=1;i<=N;i++){
        cout << result[i] << "\n";
    }
}

int main(){
    cin >> N;
    
    int x, time;
    for(int i=1;i<=N;i++){
        cin >> time;//time
        while(1){
            cin >> x;
            if(x == -1){
                break;
            }
            Time[i]=time;
            building[x].push_back(x);
            inDegree[i]++;//진입차수 ++
        }
    }
    topologysort();
    
    return 0;
}

