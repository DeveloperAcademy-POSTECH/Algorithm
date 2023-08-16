#include <bits/stdc++.h>
#include <string>
using namespace std;

vector<string> split(string input, string delimeter) {
    vector<string> ret;
    long long pos = 0;
    string token = "";
    
    while((pos = input.find(delimeter)) != string::npos){
        token = input.substr(0,pos);
        ret.push_back(token);
        input.erase(0,pos + delimeter.length());
    }
    ret.push_back(input);
    return ret;
}

int atomDate(int y, int m, int d){
    return y * 28 * 12 + m * 28 + d;
}

int _term[30];

vector<int> solution(string today, vector<string> terms, vector<string> privacies) {
    vector<int> answer;
    
    auto todaySplit = split(today, ".");
    int yy = stoi(todaySplit[0]);
    int mm = stoi(todaySplit[1]);
    int dd = stoi(todaySplit[2]);
    
    int todayAtom = atomDate(yy, mm, dd);
    
    for(string term: terms){
        auto t = split(term, " ");
        char name = char(t[0][0]);
        _term[name - 'A'] = stoi(t[1]);
    }
    
    int i= 1;
    for(string privacy : privacies){
        vector<string> p = split(privacy, " ");
        vector<string> date = split(p[0], ".");
        int y = stoi(date[0]);
        int m = stoi(date[1]);
        int d = stoi(date[2]);
        
        int dateAtom = atomDate(y, m, d);
        
        int term = char(p[1][0]) - 'A';
        
        if(todayAtom - dateAtom >= _term[term] * 28) 
            answer.push_back(i);
        
        // cout << _term[term] << ' ' << todayAtom - dateAtom<< endl;
        
        i++;
    }
    return answer;
}