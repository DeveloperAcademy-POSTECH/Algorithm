//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/08/25.
//

// 백준 12852 1로 만들기2 https://www.acmicpc.net/problem/12852

/*
dp 문제
1로 만들기 문제에서 경로까지 출력하는 문제
dp[i] = i까지 연산을 하는 횟수의 최솟값
dp[i] = 1. dp[i-1] + 1
        2. dp[i/3] + 1
        3. dp[i/2] + 1의 최솟값
      = min(dp[i-1] + 1, dp[i/3] + 1, dp[i/2] + 1)
점화식을 따라 dp 테이블을 만든다.
path라는 배열에 해당 경우의 경로를 저장한다.

마지막에 paths 배열을 사용하여 경로 출력하기
경로가 저장되어 있기 때문에, 해당 인덱스로 찾아가서 출력해 주기만 하면 된다.
*/

let N = Int(readLine()!)!
var dp = Array(repeating: 0, count: N+1)
var paths = Array(repeating: 0, count: N+1)
var answer = [Int]()

for n in 2..<N+1 {
    dp[n] = dp[n-1] + 1
    var path = n - 1 // 1을 빼는 경우

    if (n % 3 == 0) && (dp[n/3] + 1 < dp[n]) { // 3으로 나눈 경우 + 1
        dp[n] = dp[n/3]+1
        path = n / 3
    }
    if (n % 2 == 0) && (dp[n/2] + 1 < dp[n]){
        dp[n] = dp[n/2]+1
        path = n / 2
    }

    paths[n] = path
}

var x = N
while(x != 0) {
    answer.append(x)
    x = paths[x]
}

print(dp[N])
print(answer.map { String($0) }.joined(separator: " "))
