//
//  main.cpp
//  주차요금계산
//
//  Created by 신정연 on 2023/09/17.
//

#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>

/*
stoi : string -> int
substr: 문자열의 일부를 리턴 substr(시작위치, 위치+개수 = len)
*/


using namespace std;

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    map<int, int> carIn;//들어온 자동차의 시간![num, time]
    map<int, int> carOut;//나간 시간
    for(int i=0;i<records.size();i++) {
        int time = stoi(records[i].substr(0,3)) * 60 + stoi(records[i].substr(3,5));
        int number = stoi(records[i].substr(6,10));
        string info = records[i].substr(11,13);
        
        if(info == "IN") {
            carIn[number] = time;
        } else if(info == "OUT") {
            carOut[number] += time - carIn[number];//애초에 분으로 입력
            carIn.erase(number);
        }
    }
    
    for(auto i = carIn.begin(); i != carIn.end(); i++) {
        carOut[i->first] += 1439 - i->second;
    }
    
    for(auto i = carOut.begin(); i != carOut.end(); i++) {
        if(i->second <= fees[0]) {
            answer.push_back(fees[1]);
        } else {
            answer.push_back(fees[1] + ceil((double)(i->second - fees[0]) / fees[2]) * fees[3]);
        }
    }
    
    
    return answer;
}
