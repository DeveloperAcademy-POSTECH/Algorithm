//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/09/17.
//
// 백준 18606 부분합 https://www.acmicpc.net/problem/1806

let line = readLine()!.split(separator: " ").map { Int($0)! }
let (N, S) = (line[0], line[1])
var nums = readLine()!.split(separator: " ").map { Int($0)! }

// start, end 두 포인터를 이동시키며 그 사이의 합을 구한다
// 투포인터 중 두 변수가 같은 방향에서 시작하는 유형
// 투포인터는 주로 수열에서 특정한 합을 가지는 부분 연속 수열을 찾을 때 쓰인다고 함
var start = 0
var end = 0
var sum = nums[0]
var answer = N + 1 // min 값을 구하기 위해 최대 길이로 설정

while (true) {
    if sum < S {
        /*
         합이 S보다 작으면, 포인터 사이의 거리를 늘려야 한다
         end 포인터를 오른쪽으로 이동
         */
        end += 1
        if end == N  { break } // 범위를 넘어서면 탈출
        sum += nums[end]
    } else { // 합이 S보다 크거나 같다면 최소를 알맞게 갱신해 줘야 한다
        answer = min(answer, end - start + 1) // end - start + 1 -> 현재 구간의 길이
        sum -= nums[start]
        start += 1 // 다음 탐색을 위해 start 포인터를 오른쪽으로 이동한다
    }
}

// answer이 N - 1이면 합을 만드는 것이 불가능하다는 뜻 -> 0 출력
print(answer == N + 1 ? 0 : answer)
