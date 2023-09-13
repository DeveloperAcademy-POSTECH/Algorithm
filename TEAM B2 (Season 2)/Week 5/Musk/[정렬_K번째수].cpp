#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for(auto item: commands) {
        vector<int> temp(array.begin() + item[0]-1, array.begin() + item[1]);
        sort(temp.begin(), temp.end());
        answer.push_back(temp[item[2]-1]);
    }
    
    return answer;
}