//
//  main.cpp
//  1987
//  알파벳
//  Created by 신정연 on 2023/09/10.
//
/*
 세로 r, 가로 c
 (1,1) 말
 visited를 어떻게 설정할지 곰민이었는데 int로 해서 몇번째 알파벳으로 저장할바에 걍 bool로 해야겠다
 아니다 find 함수 써보고싶으니까 그냥 char로 담아야게따
 dfs로 조건넣어서 쭉쭉하면 되는줄알았는데 잘 안된당
 위에거도 그냥 다시 bool로..
 */

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int r,c;
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};
char board[21][21];
bool visited[26];//원래는 다 다를수있는데 알파벳은 26개밖에 없으니깐
int maxVisited = 0, cnt = 0;

void dfs(int i, int j, int cnt) {
    for(int k=0;k<4;k++) {
        int current = board[i][j] - 'A';//알파벳 Into num
        int nx = i + dx[k];
        int ny = j + dy[k];
        
        //범위 밖인지 검사
        if(nx < 0 || nx >= r || ny < 0 || ny >= c) {
            continue;
        }
        //이미 있는 애였는지 검사
        if(visited[current]) {
            continue;
        }
        
        if(cnt > maxVisited) {
            maxVisited = cnt;
        }
        
        visited[current] = true;
        dfs(nx, ny, cnt+1);
        visited[current] = false;
    }
}

int main(){
    
    cin >> r >> c;
    
    for(int i=0;i<r;i++) {
        for(int j=0;j<c;j++) {
            cin >> board[i][j];
        }
    }
    
    dfs(0,0,0);
    
    cout << maxVisited + 1;
    
    return 0;
}

//visited에 이미 있는 앤지 검사, 똑같은애 찾으면 거기서 중단하고 return
//        if(find(visited.begin(), visited.end(), board[i][j]) != visited.end()) {
//            cout << board[i][j] << " 이미 있어\n";
//            continue;
//        } else {
//            visited.push_back(board[i][j]);
//            cnt++;
//            cout << "cnt = " << cnt << "\n";
//        }
