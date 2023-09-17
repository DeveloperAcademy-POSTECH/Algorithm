//
//  main.cpp
//  1107
//  리모컨
//  Created by 신정연 on 2023/09/13.
//

#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int N;//이동해야 하는 채널
int cnt;
int broken;

bool button[10];//고장나면 false로 바꾸자

//bool isNormal(int number) {
//    if(number == 0) {
//        return button[0];//고장났는지 안났는지 반환
//    }
//    while(number > 0) {
//        //고장난 버튼이 있다, 포함되어있따
//        if(button[number%10] == false) {
//            return false;
//        }
//        number /= 10;
//    }
//    return true;
//}

int countPress(int number) {
    if(number == 0) {
        return button[0] ? 1 : 0;
    }
    
    int count = 0;
    while(number > 0) {
        if(button[number % 10]) {
            count ++;
        } else {
            return 0;
        }
        number /= 10;
    }
    
    return count;
}

int main(){
    
    cin >> N;
    
    cin >> cnt;
    
    fill(button, button+10, true);
    
    for(int i=0;i<cnt;i++) {
        cin >> broken;
        button[broken] = false;
    }
    //지금 보고 있는게 100번
    int answer = abs(N - 100);//100번에서 시작해서 다다다ㅏ 누르기 = 초기값으로
    
    for(int i=0;i<=1000000;i++) {
        //이번호가 고장난 번호냐
//        if(isNormal(i)) {// 안났다면
//            //몇자리수냐(몇번 눌러야되냐) 구현하라면 걍 string으로 바꿔서 length
//            len = to_string(i).length();
//            len += abs(i-N);//+,- 횟수
//            answer = min(answer, len);
//        }
        int count = countPress(i);
        if(count > 0) {
            int total = count + abs(i - N);
            answer = min(answer, total);
        }
        
    }
    
    cout << answer;
    
    return 0;
}
