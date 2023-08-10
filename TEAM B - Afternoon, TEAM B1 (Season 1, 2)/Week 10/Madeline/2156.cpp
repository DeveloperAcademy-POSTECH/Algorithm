//
//  main.cpp
//  2156
//
//  Created by 신정연 on 2023/07/12.
//  다이나믹 프로그래밍 DP
/*
 포도잔 6개 일렬로 -> 다마셔야하고, 연속으로 3잔 x
 최대한 많이 마시고 싶어함ㅋ
 */


#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> dp;//최대 마시는 양 저장
vector<int> wine;

int main(){
    int N;
    cin >> N;
    
    for(int i=0;i<3;i++){
        dp.push_back(0);
        wine.push_back(0);
    }
    
    int quantity;
    for(int i=0;i<N;i++){
        cin >> quantity;
        wine.push_back(quantity);
    }
    for(int i=3;i<wine.size();i++){
        //winep[i] 먹을 때 -> 그전꺼 먹은거랑 안먹은거 중 더 큰거
        int maxWine = max(dp[i-3]+ wine[i-1] + wine[i], dp[i-2]+wine[i]);
        //wine[i]를 먹을때, 안먹을때 중에 더 큰거
        dp.push_back(max(maxWine, dp[i-1]));
    }
    cout << dp[wine.size()-1];
    
    return 0;
}
