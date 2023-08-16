//
//  15649.cpp
//  Backtracking
//  BOJ 15649 N과M(1) 문제
//  Created by 신정연 on 2023/06/14.
//

#include <iostream>
using namespace std;

int N,M;
int arr[9];// (1 ≤ M ≤ N ≤ 8)]
bool visited[9];
int col = 0;//행=dfs의 깊이

void dfs(int col){
    if(col == M){//M번째 행일때, 지금까지 저장한 arr 출력 후 종료
        for(int i=0;i<M;i++){
            cout << arr[i] << " ";
        }
        cout << "\n";
        return;
    }
    for(int i=1;i<=N;i++){
        if(!visited[i]){//아직 방문 안했음
            visited[i]=1;//방문했다고 체크
            arr[col] = i;//arr 업데이트
            dfs(col+1);
            visited[i]=0;//되돌아감
        }
    }
}

int main(){
    cin >> N >> M;
    dfs(0);//0번째 행부터 시작
    return 0;
}
