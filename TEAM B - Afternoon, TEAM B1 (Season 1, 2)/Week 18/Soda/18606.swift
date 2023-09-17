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
var start = 0
var end = 0
var sum = nums[0]
var answer = N + 1

while (true) {
    if sum < S { // 합이 S보다 작으면, 포인터 사이의 거리를 늘려야 한다
        end += 1
        if end == N  { break }
        sum += nums[end]
    } else { // 합이 S보다 크다면 최소를 알맞게 갱신해 줘야 한다
        answer = min(answer, end - start + 1)
        sum -= nums[start]
        start += 1
    }
}

print(answer == N + 1 ? 0 : answer)
