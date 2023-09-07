//
//  main.cpp
//  7569
//  🍅
//  Created by 신정연 on 2023/09/04.
//

#include <iostream>
#include <algorithm>
#include <queue>
#include <tuple>

using namespace std;

//오왼 위아래 앞뒤
int dx[6] = { 1, -1, 0, 0, 0, 0 };
int dy[6] = { 0, 0, 1, -1, 0, 0 };
int dz[6] = { 0, 0, 0, 0, 1, -1 };

int tomato[101][101][101];
bool visited[101][101][101]; // -> 익은걸로
int M,N,H;
int cnt = 0, days = 0;
//얘네를 3개짜리 튜플에 넣어놓을것인가 아니먄 pair 2개짜리로 넣어놓을것인가
//queue<pair<pair<int, int>, int>> Q; -> 3개 입력받기 위한 ((x,y),z)
//튜플 안써봤으니까 써보자
queue<tuple<int, int, int>> Q;//x,y,z

int main(){
    
    cin >> M >> N >> H;
    
    //요 순서가 헷갈리는구만
    for(int i=0;i<H;i++){
        for(int j=0;j<N;j++){
            for(int k=0;k<M;k++){
                cin >> tomato[i][j][k];
                
                if(tomato[i][j][k] == 0){
                    cnt++; // 안익은거 개수 세기
                }
                if(tomato[i][j][k] == 1){
                    Q.push({i,j,k});
                    visited[i][j][k] = true; // 익어따
                }
            }
        }
    }
   
    if(cnt==0) { // 안익은거 하나도 없으면
        cout << cnt;
        return 0;
    }
    
    while(!Q.empty()) {
        
        int size = Q.size();
        
        for(int i=0;i<size;i++) {
            //tuple을 요렇게 불러와요
            int x = get<0>(Q.front());
            int y = get<1>(Q.front());
            int z = get<2>(Q.front());
            
            //하여튼 익은 토마토 x,y,z 위치 저장했으니까
            Q.pop(); // 빼고
            
            for(int i=0;i<6;i++) {
                //인접한 토마토를 조사해보아요
                int nx = x + dx[i];
                int ny = y + dy[i];
                int nz = z + dz[i];
                //범위 안에 있는지 확인 && 방문은 안했는디 && 토마토 == 0 안익어따
                if(nx >= 0 && ny >= 0 && nz >= 0 && H > nx && N > ny && M > nz && !visited[nx][ny][nz] && tomato[nx][ny][nz] == 0){
                    Q.push({nx,ny,nz}); // 익는다
                    visited[nx][ny][nz] = true;
                    cnt--;//안익은거 개수 빼
                }
            }
//            cout << "q = " << size << "\n";
        }
        days++;
        
    }
    //다 돌았는데도 안익은게 잇음 -> 동떨어진애 잇다
    if(cnt > 0) {
        cout << -1;
    }
    else{
        cout << days - 1;
    }
    
    return 0;
}
