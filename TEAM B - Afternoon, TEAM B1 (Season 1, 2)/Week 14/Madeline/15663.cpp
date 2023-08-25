//
//  main.cpp
//  15663
//
//  Created by 신정연 on 2023/08/23.
//

#include <iostream>
#include <algorithm>

using namespace std;

int N,M;
int arr[9]; // 선택한 숫자 인덱스
int num[9]; // 입력받은 자연수 저장
bool isVisited[9]; // 사용했나 체크

void func(int i){ // 지금까지 선택한 숫자 개수
    if(i==M){ // M개 숫자 모두 선택해씀
        for(int j=0;j<M;j++){
            cout << num[arr[j]] << " ";
        }
        cout << "\n";
        return;
    }
    //아직 다 선택 안했음
    int tmp = 0;// 중복 체크
    for(int j=0;j<N;j++){
        if(!isVisited[j] && tmp != num[j]){
            arr[i] = j;
            tmp = num[j];
            isVisited[j] = true;
            func(i+1);
            isVisited[j] = false;
        }
    }
}

int main(){
    
    cin >> N >> M;//4,2
    
    for(int i=0;i<N;i++){
        cin >> num[i];// 9 7 9 1
    }
    sort(num, num+N);//1 7 9 9
    func(0);
    
    return 0;
}

// 백트래킹 활용하는건지는 찾지 못했음 백트래킹 더 공부할것
/*
 N개 중 M개 고른 수열 모두 출력
 */
