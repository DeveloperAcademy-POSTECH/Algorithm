//
//  main.cpp
//  1012
//
//  Created by 신정연 on 2023/08/23.
//

#include <iostream>
#include <algorithm>

using namespace std;

int test, M, N, cnt;

int Cabbage[51][51] = {0,};//배추 위치 저장
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

void dfs(int i, int j){
    Cabbage[i][j] = 0;
    for(int k=0;k<4;k++){
        int xx = i + dx[k];
        int yy = j + dy[k];
        //현재 위치가 배추밭 범위를 벗어나면 넘어가
        if(xx<0 || yy<0 || xx>= M || yy>=N){
            continue;
        }
        //범위안에 있는데, 배추가 있따? 다시 재귀함수
        if(Cabbage[xx][yy] == 1){
            dfs(xx,yy);
        }
    }
}

int main(){
    
    cin >> test;
    for(int i=0;i<test;i++){
        cin >> M >> N >> cnt;
        
        int m,n;//M,N 위치
        int total = 0;
        for(int i=0;i<cnt;i++){
            cin >> m >> n;
            Cabbage[m][n] = 1;
        }
        
        for(int i=0;i<M;i++){
            for(int j=0;j<N;j++){
                if(Cabbage[i][j] == 1){
                    dfs(i,j);//근처 배추 없애기
                    total++;
                }
            }
        }
        cout << total << "\n";
    }
    
    return 0;
}
