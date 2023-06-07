//
//  10026.cpp
//  DFS&BFS
//
//  Created by 신정연 on 2023/06/07.
//

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

int N;

string board[101];
bool visited[101][101];

int dx[] = {1,-1,0,0};
int dy[] = {0,0,1,-1};

void dfs(int x, int y){
    for(int i=0;i<4;i++){
        int nx = x+dx[i];
        int ny = y+dy[i];
        //범위에 들어있는지 확인
        if(nx<0||nx>=N||ny<0||ny>=N)
            continue;
        //방문했는지
        if(visited[nx][ny] == 0 && board[nx][ny]==board[x][y]){
            visited[nx][ny] = 1;
            dfs(nx,ny);
        }
    }
}

int main(){
    
    //c++ cin, cout 속도 향상
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> board[i];
    }
    //색약 아닌 사람입장에서 개수
    int normal = 0;
    for(int i = 0;i<N;i++){
        for(int j = 0;j<N;j++){
            if(visited[i][j] == 0){
                normal++;
                visited[i][j] = 1;
                dfs(i,j);
            }
        }
    }
    //색약인 사람 입장 개수
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(board[i][j] == 'G')
                board[i][j] = 'R';
            visited[i][j] = 0;
        }
    }
    int color_blind = 0;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(visited[i][j] == 0){
                color_blind++;
                visited[i][j] = 1;
                dfs(i,j);
            }
        }
    }
    cout << normal <<" "<<color_blind;
    
    return 0;
    
}
