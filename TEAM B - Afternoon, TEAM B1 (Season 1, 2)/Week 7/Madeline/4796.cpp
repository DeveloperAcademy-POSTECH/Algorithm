//
//  main.cpp
//  4796
//
//  Created by 신정연 on 2023/06/20.
//  BOJ 4796 캠핑

#include <iostream>
#include <algorithm>

using namespace std;

int 4796() {
    int L,P,V;
    int i = 1;
    while(1){
        cin >> L >> P >> V;
        if(L==0 && P==0 && V==0){
            break;
        }
        //V/P = x..n -> L *x + n
        cout << "Case " << i << ": "<< (V/P)*L + min(V%P, L) << endl;
        i++;
    }
    return 0;
}
