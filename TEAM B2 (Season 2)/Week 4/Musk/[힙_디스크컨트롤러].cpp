#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

struct ComparePair {
    bool operator()(const pair<int, int>& a, const pair<int, int>& b) const {
        // 두 번째 int 값을 기준으로 오름차순 정렬
        return a.second > b.second;
    }
};

int solution(vector<vector<int>> jobs) {
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, ComparePair> pq;
     sort(jobs.begin(), jobs.end()); 
    
    int answer = 0;
    int time = 0;
    int complete_inpq = 0;
    int task_time = 0;
    int temp;
    
    // int test = 100; test--

    while(complete_inpq < jobs.size() || !pq.empty()) {
        // 만약 시간이 맞다면 큐에서 빼고 우선순위 큐로 넣는다. 정확히 워킹함. ㄹㅇ
        if(complete_inpq < jobs.size()) {
            if (jobs[complete_inpq][0] <= time) {
            pq.push({ jobs[complete_inpq][0], jobs[complete_inpq][1]});
            complete_inpq++;
            continue; // 시간이 훌쩍 지나갈수도 있음. 일단 시간 적은걸 다 넣어야함.
                
            }
        }
        
         if (!pq.empty()) {
            time += pq.top().second; //소요시간
            answer += time - pq.top().first; //요청시점
            pq.pop();
        }
        else {
            // 다음 작업이 들어오는 시각으로 변경
            time = jobs[complete_inpq][0];
        }
        
        
    } 
    return answer / jobs.size();
}
        // 만약 작업이 완료되었다면, 우선순위큐에서 하나 pop해서 작업을 시작한다.
        // if(!pq.empty() && task_time <= 0) {
        //     temp = pq.top().first;
        //     task_time = pq.top().first;
        //     pq.pop();
        // } else {
        //     task_time--;
        // }
        // time++;