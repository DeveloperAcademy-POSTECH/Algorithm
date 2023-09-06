//
//  main.cpp
//  11053
//
//  Created by 신정연 on 2023/08/23.
//

#include <iostream>
#include <algorithm>

using namespace std;

int N;
int A[1001];
int tmp[1001] = {0,};

int main(){
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> A[i];
    }
    
    for(int i=0;i<N;i++){
        for(int j=0;j<i;j++){
            if(A[i] > A[j]){
//                tmp[i]++; -> X, 이건 그냥 작은거 개수 세는거
                tmp[i] = max(tmp[i], tmp[j]+1);
            }
//            cout << A[i] << " " << tmp[i] << "\n";
        }
    }
    sort(tmp, tmp+N);
    cout << tmp[N-1]+1 << "\n";
    
    return 0;
}
