#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string, int> counts;

    //clothes[1] -> headgear같은 key, ++는 value를 하나씩 더한다.
    for (auto cloth : clothes) {
        counts[cloth[1]]++;
    }
    
    for (auto count : counts) {
       answer *= (count.second + 1);
    }

    answer--;
    return answer;
}

    // for (int i=0;i<q.size();i++) {
    //     cout << q[i].second << endl;
    // }