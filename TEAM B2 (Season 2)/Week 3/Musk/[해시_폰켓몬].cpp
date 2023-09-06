#include <vector>
#include <unordered_set>
using namespace std;

// https://velog.io/@yuiop1029/프로그래머스-폰켓몬

int solution(vector<int> nums) {
    
    unordered_set<int> set;
    
    for(auto item : nums ) {
        if(!(set.find(item) != set.end())) { set.insert(item); }
    }
    
    int answer = set.size() > nums.size()/2 ? nums.size()/2 : set.size();
    return answer;
}