#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;

    for(int i=0; i<arr.size();i++) {
        if(i == 0 || (answer.back() != arr[i])) {
            answer.push_back(arr[i]);
        }
    }
    
    return answer;
}

// 이렇게 풀기도 하길래 가져와봄
// arr.erase(unique(arr.begin(), arr.end()), arr.end()); 

// 스택 / 큐 문제라 해서 강제로 풀어봄. 맘에는 안든다
// #include <queue>
// vector<int> solution(vector<int> arr) {
//     vector<int> answer;
//     queue<int> q;
    
//     for(int i=0;i<arr.size();i++) {
//         if(q.front() != arr[i]) {
//             if(i != 0) { q.pop(); }
//             q.push(arr[i]);
//             answer.push_back(arr[i]);
//         }
//     }
    
//     return answer;
// }
