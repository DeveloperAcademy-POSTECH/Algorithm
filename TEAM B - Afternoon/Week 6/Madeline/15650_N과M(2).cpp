//
//  15650.cpp
//  Backtracking3
//  BOJ 15649 N과M(2) 문제
//  Created by 신정연 on 2023/06/14.
//
// 추가된 조건: 오름차순만 중복없이 출력

#include <iostream>
using namespace std;

int N,M;
int arr[9];// (1 ≤ M ≤ N ≤ 8)]
bool visited[9];
int col = 0;//행=dfs의 깊이

void dfs(int idx, int col){
    if(col == M){//M번째 행일때, 지금까지 저장한 arr 출력 후 종료
        for(int i=0;i<M;i++){
            cout << arr[i] << " ";
        }
        cout << "\n";
        return;
    }
    //(1~N,col)이 아니라, (idx,col)으로 방문
    for(int i=idx;i<=N;i++){
        if(!visited[i]){//아직 방문 안했음
            visited[i]=1;//방문했다고 체크
            arr[col] = i;//arr 업데이트
            dfs(i+1, col+1);
            visited[i]=0;//되돌아감
        }
    }
}

int main(){
    cin >> N >> M;
    dfs(1, 0);//0번째 행부터 시작
    return 0;
}

//N과M(1): 순열, N과M(2): 조합 이라고 한다
//조합은 순열과 달리 중복되면 안되므로 idx(시작점)이 필요하다.
//다음 col로 넘어갈 때 이전에 건든 작은 숫자를 건들지 않도록 하기 위해 idx가 있는 것이다.
