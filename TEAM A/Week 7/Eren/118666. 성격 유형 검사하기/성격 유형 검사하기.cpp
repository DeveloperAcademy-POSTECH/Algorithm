#include <string>
#include <vector>

using namespace std;

int score[4];
string solution(vector<string> survey, vector<int> choices) {
    string answer = "";
    for (int i = 0; i < survey.size(); i++) {
        if (survey[i] == "RT") {
            int s = choices[i] - 4;
            score[0] += s;
        }
        else if (survey[i] == "TR") {
            int s = -(choices[i] - 4);
            score[0] += s;
        }
        else if (survey[i] == "CF") {
            int s = choices[i] - 4;
            score[1] += s;
        }
        else if (survey[i] == "FC") {
            int s = -(choices[i] - 4);
            score[1] += s;
        }
        else if (survey[i] == "JM") {
            int s = choices[i] - 4;
            score[2] += s;
        }
        else if (survey[i] == "MJ") {
            int s = -(choices[i] - 4);
            score[2] += s;
        }
        else if (survey[i] == "AN") {
            int s = choices[i] - 4;
            score[3] += s;
        }
        else if (survey[i] == "NA") {
            int s = -(choices[i] - 4);
            score[3] += s;
        }
    }
    if (score[0] > 0) { answer.push_back('T'); }
    else answer.push_back('R');
    if (score[1] > 0) { answer.push_back('F'); }
    else answer.push_back('C');
    if (score[2] > 0) { answer.push_back('M'); }
    else answer.push_back('J');
    if (score[3] > 0) { answer.push_back('N'); }
    else answer.push_back('A');
    return answer;
}