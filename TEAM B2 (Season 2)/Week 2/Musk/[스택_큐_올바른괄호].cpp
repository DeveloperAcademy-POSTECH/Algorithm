#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s) {
    stack<int> stack;
    
    for(int i=0;i<s.size();i++) {
        if(s[i] == '(') { stack.push(1); }
        else if(stack.empty() && (s[i] == ')')) { return false; }
        else { stack.pop(); }
    }
    
    return stack.empty();
}