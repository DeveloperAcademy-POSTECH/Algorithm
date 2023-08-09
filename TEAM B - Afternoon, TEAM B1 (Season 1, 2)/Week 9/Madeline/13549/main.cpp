//
//  main.cpp
//  13549
//
//  Created by 신정연 on 2023/07/05.
//
// x -> x-1 or x+1 (1sec) or 2*x (0sec) 로 이동
// 움직임의 경우의 수 = 3

#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int N,K;
int Time[100001];//각 노드로 가는 최소시간 저장

void Dijkstra(){
    priority_queue<pair<int,int>> PQ;//앞에거 기준으로 정렬
    //시작 지점 = N
    PQ.push(make_pair(N, 0));
    Time[N] = 0;
    
    while(!PQ.empty()){
        int cost = -PQ.top().second;//현재 수빈쓰 - 비용
        int current = PQ.top().first;//현재 수빈쓰 - 도착노드 동생
        PQ.pop();//제거
        
        //움직임 3개 중 비용이 가장 적은 걸 구하자
        vector<int> nextX = { cost + 1, cost - 1, cost * 2 };
        
        for(int i=0;i<3;i++){
            int next = nextX[i]; //다음 노드
            if (0 <= next && next <= 100000) {
                int time = current; // 다음 노드까지의 비용
                
                if(i!=2){
                    time++;
                }
                if (Time[next] > time) {
                    Time[next] = time;
                    PQ.push({ next, time });
                }
            }
        }
    }
    cout << Time[K] << endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N >> K;
    
    for(int i=0;i<100001;i++){
        Time[i] = 100000;
    }
    
    
    Dijkstra();
    
    return 0;
}
