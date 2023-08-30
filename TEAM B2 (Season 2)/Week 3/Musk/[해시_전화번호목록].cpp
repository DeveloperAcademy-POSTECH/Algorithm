#include <string>
#include <vector>
#include <unordered_set>
using namespace std;


bool solution(vector<string> phone_book) {
    bool answer = true;
    unordered_set<string> set;
    
    for(auto item : phone_book) { set.insert(item); }
    
    for(auto item : set) {
        if (set.find(item) == 0) {
            
        }
    }

    return answer;
}