//
//  main.cpp
//  12852 1로 만들기2
//
//  Created by 신정연 on 2023/08/31.
//
/*
 10 -> 1,2,3번 방법으로 해서 나온 수 -> *3 -> ...
       4
     x 2 3
      x11 1x2 => 1이 나온 최솟값
 그래프 돌면서 1이 나온 순간에 높이랑 그 부모노드 연결된 윗줄 쭉 출력?
        10
    x    5    9
       x x 4  3 x 8
             1  => 1이 나온 최솟값
 -> 반복문을 많이 돌려야될듯

 2부터 쭉 해보니까
 dp 이전거 다 출력하면 됨
 dp[1] = 0
 d[2] = 1
 dp[3] = 1
 dp[4] = 3
 */

#include <iostream>
#include <algorithm>

using namespace std;

int N;
int dp[1000001];

int main(){

    cin >> N;

    for(int i=1;i<=N;i++){
        dp[i] = i;
    }

    // 아래에서 최소를 구해주나?? 없어도 되낭??????
    for(int i=2;i<=N;i++){
        if(i%2==0){
            dp[i] = min(dp[i], dp[i/2]);
        }
        if(i%3==0){
            dp[i] = min(dp[i], dp[i/3]);
        }
        dp[i] = min(dp[i], dp[i-1]) + 1;
    }
    
    cout << dp[N] - 1 << "\n";
    
    while(N!=0){
        cout << N << " ";
        if(dp[N] == dp[N-1] + 1){
            N = N-1;
        }
        else if(N%2 == 0 && dp[N] == dp[N/2] + 1) {
            N /= 2;
        }
        else if(N%3 == 0 && dp[N] == dp[N/3] + 1) {
            N /= 3;
        }
    }
    
    
    return 0;
}
