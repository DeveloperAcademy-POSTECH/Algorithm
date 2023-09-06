//
//  main.cpp
//  1654
//
//  Created by 신정연 on 2023/08/14.
//

#include <iostream>
#include <algorithm>

using namespace std;

// 시간초과가 나씀니다
//int main(){
//
//    int k,n;
//    cin >> k >> n;
//    int line[10001];
//    int tmp, min, cnt=0;
//    for(int i=0;i<k;i++){
//        min = line[0];
//        cin >> tmp;
//        line[i] = tmp;
//        if(min > line[i]){
//            min = line[i];
//        }
//    }
//    for(int i=min;i>1;i--){
//        cnt = 0;
//        for(int j=0;j<k;j++){
//            cnt+=(line[j]/i);
//        }
//        if(cnt==n){
//            cout << i;
//            break;
//        }
//    }
//    return 0;
//}

int main(){
    
    int k,n;
    cin >> k >> n;
    
    int line[10001];
    int tmp, max = 0, cnt, ans = 0;
    for(int i=0;i<k;i++){
        cin >> tmp;
        line[i] = tmp;
        if(max < line[i]){
            max = line[i];
        }
    }
    long left = 1, right = max, mid;
    //int 자료형의 범위를 넘을 수 있음
    while(left <= right){
        cnt=0;
        mid = (left + right) / 2;
        for(int i=0;i<k;i++){
            cnt+=(line[i]/mid);
        }
        if(cnt>=n){
            left = mid + 1;
            if (ans < mid){
                ans = mid;
            }
        }
        else{
            right = mid - 1;
        }
    }
    cout << ans;
    return 0;
}
