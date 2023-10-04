//
//  main.cpp
//  21608
//  상어 초
//  Created by 신정연 on 2023/09/04.
//
// 와 진짜 어렵다


#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N;
int x,y;
bool flag = false;// 조건끝났다 플래그
int seat[21][21]; // 결론적으로 학생들 배정할 자리
int likes[401][4]; // 좋아하는 학생 번호 저장해
int adj[21][21]; // 인접한 칸 수
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};
int score[5] = {0,1,10,100,1000};

void condition(int num){
    //** 1번 조건 : 비어있으면서 && 인접 && 좋아하는 사람 -> 최대인거 고르기
    int max = -1;
    // 근처에 있는 좋아하느 사람을 세보자
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            int cnt = 0;// 주변에 있는 좋아하는 사람 개수 셀거야
            int adj_cnt = 0;//인접한 칸 수
            if(seat[i][j] == 0){ // 빈자리면!
                
                for(int k=0;k<4;k++) {
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    
                    if(nx < 0 || nx >= N || ny < 0 || ny >= N){ // 범위 밖에 있으면,
                        continue;//넘어가
                    }
                    if(seat[nx][ny]==0){ // 범위 안에 있으면서 빈칸인거 -> 2번조건에서 씀
                        adj_cnt++;
                    }
                    if(seat[nx][ny] == likes[num][0] || seat[nx][ny] == likes[num][1] || seat[nx][ny] == likes[num][2] || seat[nx][ny] == likes[num][3]){
                        //인접한 자리에 좋아하는 사람이 있으면,
                        cnt++;
                    }
                }
            }
            if(max < cnt){
                max = cnt;
                x=i;
                y=j;
            }
            //** 2번 조건: 여러개면, 그 중에 인접 && 빈칸이 max인거 찾기
            else if(max == cnt){
                adj[i][j] = adj_cnt;//이게 인접&&빈칸인 개수
                if(adj[i][j] > adj[x][y]){//두개 비교해서 자리 업데이트
                    x = i;
                    y = j;
                }
                //** 3번 (1) 조건: 이것도 여러개야, 그러면 그 중에서 i가 작은거로 해
                else if(adj[i][j] == adj[x][y]){
                    if(i<x){
                        x = i;
                        y = j;
                    }
                    // ** 3번 (2) 조건: j가 작은걸로 해
                    else if(i==x) {
                        if(j<y) {
                            x = i;
                            y = j;
                        }
                    }
                }
            }
        }
    }
    
    seat[x][y] = num;
//    cout << num << "\n";
}

int main(){
    
    int num, tmp;
    cin >> N;
    
    for(int i=1;i<=N*N;i++){
        cin >> num; // 학생 번호
        for(int j=0;j<4;j++){
            cin >> tmp;
            likes[num][j] = tmp;// 좋아하는 사람 번호 저장
        }
        condition(num);
    }
    
    int student, cnt = 0, result = 0;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            student = seat[i][j]; //학생 누구야
            cnt=0;
            for(int k=0;k<4;k++){ // 인접 칸 좋아하는 사람 수 세기
                int nx = i + dx[k];
                int ny = j + dy[k];
                
                if(nx < 0 || nx >= N || ny < 0 || ny >= N){ // 범위 밖에 있으면,
                    continue;//넘어가
                }
                
                if(seat[nx][ny] == likes[student][0] || seat[nx][ny] == likes[student][1] || seat[nx][ny] == likes[student][2] || seat[nx][ny] == likes[student][3]){
                    //인접한 자리에 좋아하는 사람이 있으면,
                    cnt++;
                }
            }
            result += score[cnt];
        }
    }
    
    cout << result;
    return 0;
}
