//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/08/14.
//

// 백준 11049 https://www.acmicpc.net/problem/11049
// dp 문제


let N = Int(readLine()!)!
var matrix = [[Int]]()
var dp = Array(repeating: Array(repeating: 0, count: N), count: N) 

for _ in 0..<N {
    matrix.append(readLine()!.split(separator: " ").map { Int($0)! })
}

for gap in 0..<N {
    for i in 0..<N-gap-1 {
        let j = i+gap+1
        dp[i][j] = Int.max
        for k in i..<j {
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
        }
    }
}

print(dp[0].last!)
