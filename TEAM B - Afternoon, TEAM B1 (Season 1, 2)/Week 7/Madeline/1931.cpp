//
//  main.cpp
//  GreedySearch
//
//  Created by 신정연 on 2023/06/18.
//  BOJ 1931 회의실 배정

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    
    //인풋 아웃풋 시간 줄여주는
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    //N과 회의시간 입력받기
    int N;
    cin >> N;
    int a,b;
    
    vector<pair<int, int>> meetings;
    
    for(int i=0;i<N;i++){
        cin >> b >> a;
        meetings.push_back(make_pair(a,b));
    }
    //meetings vector에 시작시간, 끝 시간 삽입 -> 정렬
    sort(meetings.begin(), meetings.end());
    
    int current = meetings[0].first;
    int count = 1;
    
    for(int i = 1; i <= N ;i++){
        
        if(current <= meetings[i].second){
            count++;
            current = meetings[i].first;
        }
    }
    
    cout << count;
    
    return 0;
}
