//
//  main.cpp
//  11000
//
//  Created by 신정연 on 2023/06/21.
//  BOJ 11000 강의실 배정

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    int N;
    cin >> N;
    
    vector<pair<int, int>> classroom;
    int s,t;
    for(int i=0;i<N;i++){
        cin >> t >> s;
        classroom.push_back(make_pair(s,t));
    }
    sort(classroom.begin(), classroom.end());
    
    //첫번째 수업 끝나는 시간 = current time
    int time = classroom[0].first;
    int cnt = 1;
    
    for(int i=1;i<=N;i++){
        if(time >= classroom[i].second){
            cnt++;
            time = classroom[i].first;
        }
    }
    cout << cnt;
    
    return 0;
}
