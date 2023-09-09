//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/08/22.
//

// 백준 11053 가장 긴 증가하는 부분 수열 https://www.acmicpc.net/problem/11053

/*
처음에는 부분 수열이라길래 백트래킹인 줄 알았는데, 너무 안 풀려서 알고리즘 분류를 보니까 DP였따.
테이블 정의: D[i] = A[i]를 마지막 값으로 가지는 가장 긴 증가 부분 수열 길이
초기값: D[0] = 1이다. (길이는 무조건 1이기 때문)
점화식: 자기보다 작은 수들 중 D[i]가 최대인 값 + 1
*/

let N = Int(readLine()!)!
let nums = readLine()!.split(separator: " ").map { Int($0)! }
var dp = Array(repeating: 0, count: N)

dp[0] = 1

// 전체 수열을 순회하는 반복문
for i in 0..<N {
    var tmp = 0

    for j in 0..<i { // 인덱스 0부터 i번째 요소 전까지 순회
        if nums[i] > nums[j] { // nums[i]보다 작은 수들 중 D[i]가 최대인 값을 찾음
            tmp = max(tmp, dp[j])
        }
    }

    // 최대값 + 1이 된다. 자기보다 작은 수가 없는 경우에는 tmp = 0 이 됨. (ex. [10, 20, 10])
    dp[i] = tmp + 1
}

print(dp.max()!) // dp 테이블 중 최댓값을 출력한다
