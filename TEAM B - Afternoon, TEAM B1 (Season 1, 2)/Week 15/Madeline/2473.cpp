//
//  main.cpp
//  2473
//  세 용액
//  Created by 신정연 on 2023/09/04.
//
// long long은 int형 범위 초과될때 씁니다~

#include <iostream>
#include <algorithm>

using namespace std;

int N;
long long liquid[5001];
//long long의 최댓값으로 두고 푼다!


int main(){
    
    long long min = 1e18; // 왜 전역변수로 두면 에러가 날까,,?
    long long result[4];
    
    cin >> N;
    
    for(int i=0;i<N;i++){
        cin >> liquid[i];
    }
    
    sort(liquid, liquid+N);//오름차순
    
    for(int i=0;i<N-1;i++){
        long long start = i+1;
        long long end = N-1;
        
        while(start<end){
            long long cnt = liquid[i] + liquid[start] + liquid[end];
            if(abs(cnt) < min){
                min = abs(cnt);
                result[1] = liquid[i];
                result[2] = liquid[start];
                result[3] = liquid[end];
            }
            
            if(cnt < 0){
                start++;
            }
            else{
                end--;
            }
        }
    }
    cout << result[1] << " " << result[2] << " " << result[3];
    
    return 0;
}
