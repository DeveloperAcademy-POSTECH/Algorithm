//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/10/01.
//
// 백준 14501 퇴사 https://www.acmicpc.net/problem/14501

/*
DP 문제
마지막날 -> 첫째날로 생각하기
퇴사일의 범위를 넘어갔을 때는 다음날의 최대 이익을 가져오기(해당일에는 일을 할 수 없으므로)
넘어가지 않을 때는 해당 일에 일을 했을 때의 최대 이익과 일을 하지 않았을 때를 비교하여 최대 이익 갱신
*/

let N = Int(readLine()!)!
var matrix = [[0, 0]]
var dp = Array(repeating: 0, count: 20)

for _ in 0..<N {
    matrix.append(readLine()!.split(separator: " ").map { Int($0)! })
}

for i in (1...N).reversed() {
    let (t, p) = (matrix[i][0], matrix[i][1])
    let finishDay = i + t // 일을 끝낸 날

    if finishDay > N + 1 { // 퇴사일의 범위를 넘어가면
        dp[i] = dp[i+1] // 다음날의 최대 이익을 그대로 가져오기
    } else {
        // 당일에 일을 하지 않고 다음 날 최대 이익, 당일에 일을 했을 때 최대 이익 비교
        dp[i] = max(dp[i+1], dp[finishDay] + p)
    }
}

print(dp[1])
