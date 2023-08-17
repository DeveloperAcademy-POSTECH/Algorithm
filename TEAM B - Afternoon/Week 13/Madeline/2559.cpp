//
//  main.cpp
//  2559
//
//  Created by 신정연 on 2023/08/14.
//

#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    
    //segment tree가 모야?
    
    int N,K, inp, tmp=0, max=0;
    cin >> N >> K;
    int temp[100001] = {0,};
    for(int i=0;i<N;i++){
        cin >> inp;
        temp[i] = inp;
    }
    for(int i=0;i<K;i++){
        //0~4
        tmp += temp[i];
    }
    max = tmp;
    for(int i=0;i<N-K;i++){
        tmp-=temp[i];//-0
        tmp+=temp[i+K];//+5
        if(tmp > max){
            max = tmp;
        }
    }
    cout << max;
    return 0;
}
