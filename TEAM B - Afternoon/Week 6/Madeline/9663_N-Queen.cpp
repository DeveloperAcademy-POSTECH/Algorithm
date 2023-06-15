//
//  9663.cpp
//  Backtracking
//  BOJ 9663 N-Queen 문제
//  Created by 신정연 on 2023/06/14.
//

#include <iostream>
#include <vector>

using namespace std;

int N;//크기가 NxN인 체스판
int answer = 0;//퀸을 놓는 경우의 수
int loc[15];// (1 ≤ N < 15)

bool isPromising(int row){//조건을 만족하는지
    for(int i=0;i<row;i++){
        //같은 행,열인지 or 대각선인지 검사
        if((loc[i] == loc[row]) || (row-i)==(abs(loc[row]-loc[i]))){
            return 0;
        }
    }
    return 1;
}

void NQueen(int row){
    if(row == N){//N번째 행까지 다 돌았음
        answer += 1;
        return;
    }
    else{
        for(int i=0;i<N;i++){
            loc[row] = i;// row[0] = 2 -> 0행 2열에 퀸 존재
            
            if (isPromising(row)){
                NQueen(row+1);// 다음 행
            }
        }
    }
}

int main() {
    cin>> N;
    NQueen(0);//0번째 행부터 시작
    cout<< answer;
    
    return 0;
}
