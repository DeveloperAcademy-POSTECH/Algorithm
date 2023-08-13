//
//  2606.cpp
//  DFS&BFS
//
//  Created by 신정연 on 2023/06/02.
//
// [백준 2606] 바이러스

#include <iostream>
#include <vector>

using namespace std;

vector<int> computers[101];
bool virus[101];
int total;

void dfs(int x){
    for(int i=0;i<computers[x].size();i++){
        int j = computers[x][i];
        if(!virus[j]){
            virus[j] = true;
            total++;
            dfs(j);
        }
    }
    return;
}

int main() {
    //컴퓨터 수
    int num;
    cin >> num;
    //네트워크에서 연결되어 있는 컴퓨터 쌍
    int connected;
    cin >> connected;
    //connected 만큼 연결되어 있는 번호 쌍
    
    //**위에 코드를 한 줄에**
    //cin>> num >> connected;
    
    for(int i = 0; i < connected; i++){
        //x,y 가 연결되어 있음
        int x,y;
        cin >> x >> y;
        computers[x].push_back(y);
        computers[y].push_back(x);
        // -> 서로 연결
    }
    
    dfs(1);
    
    cout << total;
    
    return 0;
}
