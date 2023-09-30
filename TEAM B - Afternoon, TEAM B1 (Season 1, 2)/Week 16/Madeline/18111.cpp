//
//  main.cpp
//  18111
//  마인크래프트
//  Created by 신정연 on 2023/09/06.
//

#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    
    int n,m,b;
    int max_height = -1, min_time = 1e9;//출력할거
    int ground[501][501];
    
    cin >> n >> m >> b;
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            cin >> ground[i][j];
        }
    }
    
    for(int h=0;h<=256;h++) {//높이를 하나씩 낮춰가면서 구해보아요
        int inven = 0;//인벤토리에서 꺼낼거 개수 구하기 (+1초)
        int remove = 0;//제거하는거 (+2초)
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                int tmp_height = ground[i][j] - h;//바꿔가면서 구할 현재 높이
                if(tmp_height < 0) { //현재 높이가 음수면(== 목표 높이보다 낮으면) 인벤토리에서 하나 꺼내서 채워
                    inven -= tmp_height;
                }
                else {//양수면 땅에서 하나 빼
                    remove += tmp_height;
                }
            }
        }
        //시간 구하기
        if(remove + b >= inven) {// 인벤 개수 <= 제거해야되는 블록수일때
            int tmp_time = 2 * remove + inven;//현재 높이에서 걸리는 시간
            if(min_time >= tmp_time) {
                min_time = tmp_time;
                max_height = h;
            }
        }
    }
    
    cout << min_time << " " << max_height;
    
    return 0;
}
