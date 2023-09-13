#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
bool compare(string i, string j) {
        return j + i < i + j;
}

string solution(vector<int> numbers) {
    vector<string> strnums;
    for (auto item: numbers) { strnums.push_back(to_string(item)); }
    sort(strnums.begin(), strnums.end(), compare);
    
    string answer = "";
    for (auto item: strnums) { answer += item; }
    
    if(strnums.at(0) == "0") { return "0"; }
    return answer;
}