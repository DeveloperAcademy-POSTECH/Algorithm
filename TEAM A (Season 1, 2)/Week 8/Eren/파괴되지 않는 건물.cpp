#include <vector>
#include <vector>
using namespace std;

int attack[1004][1004];

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;
    
    for(vector<int> s: skill){
        int r1 = s[1]; int c1 = s[2];
        int r2 = s[3]; int c2 = s[4];
        int degree = s[5];
        
        if(s[0] == 1){
            attack[r1][c1] += -degree;   attack[r1][c2+1] += degree;
            attack[r2+1][c1] += degree;  attack[r2+1][c2+1] += -degree;
        }
        else {
            attack[r1][c1] += degree;    attack[r1][c2+1] += -degree;
            attack[r2+1][c1] += -degree; attack[r2+1][c2+1] += degree;
        }

    }
    
    for(int i=0; i<board.size(); i++){
        for(int j=0; j<board[0].size(); j++){
            attack[i][j+1] += attack[i][j];
        }
    }
    for(int j=0; j<board[0].size(); j++){
        for(int i=0; i<board.size(); i++){
            attack[i+1][j] += attack[i][j];
        }
    }
    
    for(int i=0; i<board.size(); i++){
        for(int j=0; j<board[0].size(); j++){
            board[i][j] += attack[i][j];
            if(board[i][j] > 0) answer++;
        }
    }
    
    return answer;
}