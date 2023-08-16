#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

unordered_map<string, int> inTime;
unordered_map<string, int> stayTime;

vector<string> split(string input, string delimeter){
    vector<string> ret;
    long long pos = 0;
    string token = "";
    while((pos = input.find(delimeter)) != string::npos){
        token = input.substr(0, pos);
        ret.push_back(token);
        input.erase(0, pos + delimeter.length());
    }
    ret.push_back(input);
    return ret;
}


int t2m(vector<string> t){
    string h = t[0];
    string m = t[1];
    int hour; int min;
    
    hour = stoi(h);
    min = stoi(m);
    
    return hour*60 + min;
}



vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    vector<pair<string, int>> v;
    
    for(auto record: records){
        auto info = split(record, " ");
        auto id = info[1];
        auto timestamp = split(info[0], ":");
        
        auto min = t2m(timestamp);
        
        if(info[2] == "IN"){
            inTime[id] = min;
        }
        else {
            stayTime[id] += min - inTime[id];
            inTime.erase(id);
        }
    }
    
    for(auto ele: inTime){
        auto id = ele.first;
        int lastTime = 23*60 + 59;
        stayTime[id] += lastTime - ele.second;
    }
    
    for(auto ele: stayTime){
        auto id = ele.first;
        auto min = ele.second;
        if(min <= fees[0]){ v.push_back({id, fees[1]}); continue; }
        
        long long fee = fees[1];
        
        min -= fees[0];
            
        float minute =  ceil((float)min / (float)fees[2]);
        
        
        fee += minute * fees[3];
        v.push_back({id, fee});
    }
    sort(v.begin(),v.end());
    for(auto ele: v){
        answer.push_back(ele.second);
    }
    
    return answer;
}