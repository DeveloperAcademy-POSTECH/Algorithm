//
//  main.cpp
//  2252
//
//  Created by 신정연 on 2023/07/26.
//

#include <iostream>
#include <vector>
#include <queue>

#define MAX 32001

using namespace std;

int N, M;
int inDegree[MAX];//진입차수
vector<int> students[MAX];//학생노드

void topologySort(){
    
    int result[MAX];//위상정렬 순서
    queue<int> q;
    //진입차수가 0인 학생 -> 큐에 넣어
    for(int i = 1;i<=N;i++){
        if(inDegree[i]==0){
            q.push(i);
        }
    }
    for(int i = 1;i<=N;i++){
//        if(q.empty()){
//              return;
//        }
        int x = q.front();
        q.pop();
        result[i] = x;
        for(int i=0;i<students[x].size();i++){
            int y = students[x][i];
            inDegree[y]--;
            if(inDegree[y]==0){
                q.push(y);
            }
        }
    }
    for(int i=1;i<=N;i++){
        cout << result[i] << " ";
    }
}

int main(){
    cin >> N >> M;
    
    int x,y;
    for(int i=1;i<=M;i++){
        cin >> x >> y;
        students[x].push_back(y);
        inDegree[y]++;//진입차수 ++
    }
    topologySort();
    
    return 0;
}
