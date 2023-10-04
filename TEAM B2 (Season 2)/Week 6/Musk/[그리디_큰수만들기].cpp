#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

// https://velog.io/@yuiop1029/프로그래머스-큰-수-만들기
// 앞에서부터 작은 숫자들을 전부 지우면 되지 않을까?

string solution(string number, int k) {
    
    int locate = 0;
    // 맨처음 찾기, 삭제시키면 변수가 있어서 locate를 0으로 초기화 해서 다시 찾아봄.
    while(k) {
        if (number.size() ==  locate) { break; }
        if(number[locate] < number[locate+1]) {
            number.erase(number.begin()+locate);
            locate = 0;
            k--;
        } else { 
            locate++;
        }
    }
        
    // 위에서 앞자리 일수록 큰 숫자로 되었으니 k가 남으면 뒤에서 삭제시킴.
    if(k != 0) { 
        for(int i=0;i<k;i++) {
            number.erase(number.end()-1);
        }
    }
        
    
    
    return number;
}


//  vector<char> remain;
//     for (auto item: number) { remain.push_back(item); }
//     sort(remain.begin(), remain.end());
    
//     for(int i=0;i<k;i++) {
//         for (auto item: remain) { 
//             if(number[i] == item) { number.erase(number.begin()+i); }
//             }
//     }
    