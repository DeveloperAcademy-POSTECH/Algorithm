//
//  main.cpp
//  11049
//
//  Created by 신정연 on 2023/08/14.
//

#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int main(){
    
    int n, r, c;
    int row[503], col[503];
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> r >> c;
        row[i] = r;
        col[i] = c;
    }
    
    int DP[501][501];; // <- 행렬 곱 경우ㅜ의 수 저장
    
    for(int len=1; len<n; len++){
        for(int i=0; i<n; i++){
            int j= i+len;
            if(j >= n) break;
            int res = INT_MAX;
            for(int k=i; k<j; k++){
                res = min(res, DP[i][k]+DP[k+1][j]+row[i]*col[k]*col[j]);
            }
            DP[i][j] = res;
        }
    }
    cout << DP[0][n-1] ;
    return 0;
}
