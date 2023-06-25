//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/06/24.
//
// 백준 1463 1로 만들기 https://www.acmicpc.net/problem/1463

// 1. dp
//let N = Int(readLine()!)!
//var dp = Array(repeating: 0, count: 1000001)
//
//for i in 2..<N+1 {
//    dp[i] = dp[i-1] + 1
//
//    if (i%2 == 0) { dp[i] = min(dp[i], dp[i/2]+1) }
//    if (i%3 == 0) { dp[i] = min(dp[i], dp[i/3]+1) }
//}
//
//print(dp[N])

// 2. 엄청난 풀이 ,,,
let N = Int(readLine()!)!

func recur(_ n : Int, _ cnt: Int) -> Int {
    if n < 2 { return cnt } // 정답이 0인 경우
    return min(recur(n/2, cnt+1 + (n%2)), recur(n/3, cnt+1+(n%3)))

}

print(recur(N, 0))
