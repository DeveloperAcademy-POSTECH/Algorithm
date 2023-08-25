//
//  main.cpp
//  2467
//
//  Created by 신정연 on 2023/08/23.
//

#include <iostream>
#include <algorithm>

using namespace std;

int N;
long long int liq[100001];
long long int resL, resR;

int main(){
    
    cin >> N;
    
    for(int i=0;i<N;i++){
        cin >> liq[i];
    }
    
    int left = 0;
    int right = N-1;
    
    
    //처음값
    int result = abs(liq[left] + liq[right]);
    resL = liq[left];
    resR = liq[right];
    
    while(left < right){
        int tmp = (liq[left] + liq[right]);
        if(abs(tmp) < result){
            result = abs(tmp);
            resL = liq[left];
            resR = liq[right];
        }
        if(tmp < 0){
            left++;
        }
        else{
            right--;
        }
    }
    
    cout << resL << " " << resR;
    
    return 0;
}
