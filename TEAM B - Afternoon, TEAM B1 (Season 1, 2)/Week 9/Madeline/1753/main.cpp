//
//  main.cpp
//  1753
//
//  Created by 신정연 on 2023/07/05.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#define INF 1000000
#define MAX_VERTEX 20001 // 최대 vertex 개수
#define MAX_EDGE 300001 // 최대 edge 개수

using namespace std;

int Cost[MAX_VERTEX];//비용 저장
int V,E,start;
vector <pair<int,int>> Vertex[MAX_EDGE];//v,w

void Dijkstra(){
    priority_queue<pair<int,int>> PQ;//v,w
    //값이 클수록 더 높은 우선순위를 가짐
    //{2,3,5}일 때, 위 같이 선언하면 5를 가장 먼저 뽑아서 사용
    PQ.push(make_pair(start, 0));
    Cost[start] = 0;//시작점 자신은 0으로 출력
    
    while(!PQ.empty()){
        int cost = -PQ.top().second;//현재 - 비용
        int current = PQ.top().first;//현재 - 도착노드
        PQ.pop();//제거
        
//        if(Cost[current] < cost){
//            continue;
//        }
        
        for(int i=0;i<Vertex[current].size();i++){
            int next = Vertex[current][i].first;//다음 노드
            int ncost = Vertex[current][i].second;//다음 노드까지의 비용
//            cout << "DIJ" << next << ncost << endl;
            if(Cost[next] > cost + ncost){
                Cost[next] = cost + ncost;
                PQ.push(make_pair(next,-Cost[next]));
            }
        }
    }
    for(int i=1;i<=V;i++){
        if(Cost[i] == INF){
            cout << "INF" << endl;
        }
        else{
            cout << Cost[i] << endl;
        }
    }
    
}
int main(){
    
    //인풋 아웃풋 시간 줄여주는 -> 이 차이로 시간초과가 나네,,
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    //입력 받아요
    cin >> V >> E;
    cin >> start;
    
    //비용 INF로 초기화
    for(int i=1;i<=V;i++){
        Cost[i] = INF;
    }
    //노드, 정점 저장
    for(int i=0;i<E;i++){
        int u,w,v;
        cin >> u >> v >> w;
        Vertex[u].push_back(make_pair(v, w));//도착노드, 비용
//        cout << "i=" << i << endl;
    }
    Dijkstra();
    return 0;
}
