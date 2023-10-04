#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// https://velog.io/@yuiop1029/프로그래머스-단속카메라

int solution(vector<vector<int>> routes) {
    int answer = 0;
    sort(routes.begin(), routes.end());
    
    int temp = routes[0][1];
    for (auto item: routes) {
        if (temp < item[0]) {
            temp = item[1];
            answer++;
        }
        else if (temp >= item[1]) { temp = item[1]; }
    }
    return ++answer;
}