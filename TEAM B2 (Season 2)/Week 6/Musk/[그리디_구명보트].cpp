#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// https://velog.io/@yuiop1029/프로그래머스-구명보트

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(),people.end());
    int save = 0;
    int save_front = 0;
    int save_last = people.size()-1;
    while(people.size() - save > 1) {
        if(people[save_last] + people[save_front] <= limit) {
            save_front++;
            save_last--;
            save += 2;
        } else {
            save_last--;
            save++;
        }
        answer++;
    }
    if (people.size() - save == 1) { answer++; }
    
    return answer;
}