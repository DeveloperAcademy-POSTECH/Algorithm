//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/06/25.
//
// 백준 9095 1,2,3 더하기 https://www.acmicpc.net/problem/9095

/*
dp[k] = k를 1,2,3의 합으로 나타내는 방법의 수
1. dp[k-1] 에서 1을 더했을 때산 연산
2. dp[k-2] 에서 2를 더했을 때의 연산 (dp[k-2]가 존재할 경우)
3. dp[k-3] 에서 3을 더했을 때의 연산 (dp[k-3]이 존재할 경우)
점화식 dp[k] = dp[k-1] + dp[k-2] + dp[k-3]
ex. dp[4] = dp[3] + dp[2] + d[1] 
초기값 dp[1] = 1, dp[2] = 2, dp[3] = 4
 */


let t = Int(readLine()!)!
var dp = Array(repeating: 0, count: 12)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in 0..<t {
    let n = Int(readLine()!)!
    if n > 3 { // 4 이상일 때만 계산, 그외에는 그냥 해당 값 출력
        for i in 4...n {
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        }
    }
    print(dp[n])
}
