//
//  main.cpp
//  2512
//
//  Created by 신정연 on 2023/08/23.
//

#include <iostream>
#include <algorithm>

using namespace std;

int N, M;
int region[10001];
int maximum = 0, cnt = 0;

int main(){
    
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> region[i];
        if(maximum < region[i]){
            maximum = region[i];
        }
    }
    cin >> M;
    
    while(1){
        cnt = 0;
        for(int i=0;i<N;i++){
            if(maximum > region[i]){
                cnt += region[i];
            }
            else{
                cnt += maximum;
            }
//            cout << cnt << " " << region[i] << "\n";
        }
        if(cnt > M){
            maximum--;
        }
        else{
            break;
        }
    }
    
    cout << maximum;
    
    return 0;
}
