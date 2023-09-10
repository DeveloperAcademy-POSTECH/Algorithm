#include <string>
#include <vector>
#include <unordered_set>

// https://velog.io/@yuiop1029/프로그래머스-완주하지-못한-선수

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    
    unordered_multiset<string> set;
    for(auto item : participant) { set.insert(item); }
    
    for(auto item : completion) { 
        unordered_multiset<string>::iterator itr = set.find(item);
        set.erase(itr);
    }
    
    string answer = *set.begin();
    
    return answer;
}