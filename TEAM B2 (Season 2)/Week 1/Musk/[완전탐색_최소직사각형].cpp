#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int high_width = 0;
    int high_height = 0;
    
    for(int i=0;i<sizes.size();i++) {
        if(sizes[i][0] < sizes[i][1]) {
            if (high_width < sizes[i][0]) { high_width = sizes[i][0]; }
            if (high_height < sizes[i][1]) {high_height = sizes[i][1]; }
        } else {
            if (high_width < sizes[i][1]) { high_width = sizes[i][1]; }
            if (high_height < sizes[i][0]) {high_height = sizes[i][0]; }
        }
    }
    
    int answer = high_width * high_height;
    return answer;
}
