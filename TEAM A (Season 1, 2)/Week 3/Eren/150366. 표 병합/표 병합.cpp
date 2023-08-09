#include <bits/stdc++.h>
#include <string.h>
using namespace std;
#define ii pair<int, int>

string board[54][54];

ii par[55][55];

ii Find(ii a){
    if(par[a.first][a.second] == a) return a;
    else return par[a.first][a.second] = Find(par[a.first][a.second]);
}


bool Union(ii a, ii b){
    a = Find({a.first, a.second});
    b = Find({b.first, b.second});
    
    if(a == b) return false;
    
    par[b.first][b.second] = a;
    return true;
}

vector<string> split(string input, string delimeter) {
    vector<string> ret;
    long long pos = 0;
    string token = "";
    while((pos = input.find(delimeter)) != string::npos) {
        token = input.substr(0, pos);
        ret.push_back(token);
        input.erase(0, pos + delimeter.length());
    }
    ret.push_back(input);
    return ret;
}

void reset(int x, int y){
    vector<ii> v;
    for(int i=1; i<=50; i++){
        for(int j=1; j<=50; j++){
            auto [a, b] = Find({i,j});
            if(x == a and y == b)
                v.push_back({i, j});
        }
    }
    for(auto [i, j]: v){
        par[i][j] = {i, j};
        board[i][j] = "";
    }
}


vector<string> solution(vector<string> commands) {
    vector<string> answer;
    
    for(int i=1; i<=50; i++)
        for(int j=1; j<=50; j++)
            par[i][j] = {i,j};
    
    for(auto command : commands) {
        vector<string> c = split(command, " ");
        int r1, c1, r2, c2;
        if(c[0] == "UPDATE" and c.size() == 4){
            r1 = stoi(c[1]); c1 = stoi(c[2]);
            
            auto [r3, c3] = Find({r1,c1});
            
            board[r3][c3] = c[3];
        }
        
        else if(c[0] == "UPDATE" and c.size() == 3){
            for(int i=1; i<=50; i++)
                for(int j=1; j<=50; j++)
                    if(board[i][j] == c[1])
                        board[i][j] = c[2];
        }
        
        else if(c[0] == "MERGE") {
            r1 = stoi(c[1]); c1 = stoi(c[2]);
            r2 = stoi(c[3]); c2 = stoi(c[4]);
            
            auto [r3, c3] = Find({r1, c1});
            auto [r4, c4] = Find({r2, c2});
            
            if(r3 == r4 and c3 == c4) continue;
            
            if(board[r3][c3] == "" && board[r4][c4] != ""){
                par[r3][c3] = {r4, c4};
            }
            else {
                par[r4][c4] = {r3, c3};
                board[r4][c4] = "";
            }
        }
        else if(c[0] == "UNMERGE"){
            r1 = stoi(c[1]); c1 = stoi(c[2]);
            
            auto [r3, c3] = Find({r1, c1});
            string tmp = board[r3][c3];
            
            reset(r3, c3);
            
            board[r1][c1] = tmp;
            
        }
        else if(c[0] == "PRINT"){
            r1 = stoi(c[1]); c1 = stoi(c[2]);
            
            auto [r3, c3] = Find({r1, c1});
            
            if(board[r3][c3] == "") answer.push_back("EMPTY");
            else answer.push_back(board[r3][c3]);
        }
        
    }
            
    return answer;
}