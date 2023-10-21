//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/10/09.
//
// 백준 2565 전깃줄 https://www.acmicpc.net/problem/2565

/*
전깃줄 위치 input을 오름차순으로 정렬했을 때, 전깃줄이 겹치지 않으려면 오른쪽 값이 전보다 커야 함
-> 증가하는 가장 긴 부분 수열 찾기 문제와 동일함
-> dp
*/

let N = Int(readLine()!)!
var numbers = [[Int]]()
var dp = Array(repeating: 0, count: N) // dp 배열 - numbers[i]를 마지막 값으로 가지는 가장 긴 증가 부분 수열 길이

// 입력 받기
for _ in 0..<N {
    numbers.append(readLine()!.split(separator: " ").map { Int($0)! })
}

numbers.sort { $0[0] < $1[0] }

// numbers[0]의 가장 긴 부분 수열은 1이므로 dp[0] 초깃값은 1임
dp[0] = 1

for i in 0..<N {
    var tmp = 0

    // i번째보다 앞쪽에 있는 수들을 순회함
    for j in 0..<i {
        if (numbers[j][1] < numbers[i][1]) { // 증가하는 부분 수열이므로 작은 수 찾기
            tmp = max(tmp, dp[j]) // 최댓값 갱신
        }
    }

    dp[i] = tmp + 1 // 자신을 포함하므로 +1
}

print(N - dp.max()!)
