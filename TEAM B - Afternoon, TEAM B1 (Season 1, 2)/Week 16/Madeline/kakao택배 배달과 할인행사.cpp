//
//  main.cpp
//  택배배달수거하기
//
//  Created by 신정연 on 2023/09/06.
//

#include <string>
#include <vector>

using namespace std;

long long solution(int cap, int n, vector<int> deliveries, vector<int> pickups) {
    long long answer = 0;
    int d = 0, p = 0;//현재 배달, 수거 상태
    int cnt = 0;//트럭 이동 횟수(거리)
    
    // 멀리있는데부터 가야되니까 역순으로
    for(int i=n-1;i>=0;i--) {
        d -= deliveries[i];// 배달택배 상자수 빼서 업데이트
        p -= pickups[i];// 수거하는거 상자수-
        
        //택배랑 빈 택배가 0이면 종료
        while(1) {
            if(d >= 0 && p >= 0){//배달할거 수거할거 0이상일때 종료(처리할게 없음)
                break;
            }
            d += cap;//용량만큼 증가 -> 처리할 수 있는 개수
            p += cap;// 만약에 얘네가 용량 초과하면 다음 이동으로 넘어가
            cnt++;
        }
        answer += (i+1)*2*cnt;//현재 집 위치 * 현재까지 이동한 거리cnt
        cnt = 0;
    }
    return answer;
}
