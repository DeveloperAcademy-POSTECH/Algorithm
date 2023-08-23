//
//  main.cpp
//  1541
//
//  Created by 신정연 on 2023/08/15.
//

#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;

int main(){
    
    char str[51];
    bool flag = false; // - 가 나오면 true
    int sum = 0, tmp=0, len;
    cin >> str;
    len = strlen(str);
    
    for(int i=0;i<=len;i++){
        
        if(str[i] == '-' || str[i] == '+' || i==len){
            
            if(flag == false){
                sum += tmp;
                tmp = 0;
                if(str[i] == '-'){
                    flag = true;
                }
            }
            else{
                sum -= tmp;
                tmp = 0;
            }
        }
        else{
            tmp *= 10;
            tmp += str[i] - '0'; // char -> int
        }
//        cout << tmp << " " << str[i] << "\n";
    }
    
    cout << sum;
    
    return 0;
}
