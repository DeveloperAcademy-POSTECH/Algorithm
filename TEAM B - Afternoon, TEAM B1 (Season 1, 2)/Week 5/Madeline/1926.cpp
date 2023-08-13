//
//  1926.cpp
//  DFS&BFS
//
//  Created by 신정연 on 2023/06/07.
//
// BFS
//
// [백준] 1926 그림

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

//pair를 쉽게 쓰기 위해서 선언, first second -> t.X, t.Y
#define X first
#define Y second


int main(){
    
    //c++ cin, cout 속도 향상
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
                // ====== BFS 기본 작업 =======
    // 판(도화지)
    int board[501][501];
    //방문 여부 저장하는 변수
    bool visited[501][501];

    //행, 열 개수
    int n,m;

    //상하좌우 사용
    int dx[4] = {1,0,-1,0};
    int dy[4] = {0,1,0,-1};
    
    // 큐 Q -> pair 로 생성
    queue<pair<int,int>> Q;
                // ====== BFS 기본 작업 =======
    
    //행, 열 입력받아
    cin >> n >> m;
    
    // 그림 입력받아
    for(int i = 0;i<n;i++){
        for(int j=0;j<m;j++){
            cin >> board[i][j];
        }
    }
    
    //그림의 넓이
    int area = 0;
    int max = 0;
    //그림의 개수
    int num = 0;
    
    // starting point = 0,0 방문해씀
//    visited[0][0] = 1;
//    Q.push({0,0});
    
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            //이미 방문했는지
            if(visited[i][j] || board[i][j]==0)
                continue;
            visited[i][j] = 1;
            Q.push({i,j});
            area = 0;
            num++;
            
            while(!Q.empty()){
                //큐의 front -> cur 에 저장 후 pop()
                pair<int, int> cur = Q.front();
                
                Q.pop();
                
                area++;
                
                //상하좌우
                //       x-1,y
                //x, y-1  x,y  x,y+1
                //       x+1,y
                //nx, ny 값 아래, 오른쪽, 위, 왼쪽
                //dx[dir], dy[dir] = (1,0), (0,1), (-1,0), (0,-1)
                for(int dir = 0; dir < 4; dir++){
                    int nx = cur.X + dx[dir];
                    int ny = cur.Y + dy[dir];
                    
                    //범위에 들어오는지 확인
                    if(nx < 0 || nx >= n || ny < 0 || ny >= m)
                        continue;
                    //이미 방문한건지 확인
                    if(visited[nx][ny] || board[nx][ny] != 1)
                        continue;
                    //위 두개 순서 고대로 해야 함
                    visited[nx][ny] = 1;
                    Q.push({nx,ny});
                }
                if(max < area){
                    max=area;
                }
            }
        }
    }
    cout << num << "\n" << max;
    return 0;
    
}
