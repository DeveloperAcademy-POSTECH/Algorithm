//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/08/19.
//
// 백준 2512 예산 https://www.acmicpc.net/problem/2512

/*
이분 탐색 문제
M이 크고, 가능한 한 최대한 ~ 의 키워드로부터 이분 탐색 문제일 것이라고 생각했다.
*/

// 필요한 입력을 받는다
let N = Int(readLine()!)!
let requests = readLine()!.split(separator: " ").map { Int($0)! }
let M = Int(readLine()!)!

// start는 0으로, end는 요청의 최댓값으로 지정한다.
var start = 0
var end = requests.max()!

// 이분 탐색을 이용한다.
while start <= end {
    // mid값을 특정 상한액으로 사용한다.
    let mid = (start + end) / 2
    var sum = 0

    // 요청을 순회하며 요청 >= 특정 상한액일 경우 특정 상한액을 더해 주고, 요청이 작을 경우, 요청을 더해준다.
    for request in requests {
        if request >= mid {
            sum += mid
        } else {
            sum += request
        }
    }

    // 합이 M보다 큰 경우 -> 특정 상한액(mid)를 줄여야 한다. -> end를 mid - 1로 변경
    // 합이 M보다 작은 경우 -> 특정 상한액(mid)를 늘릴 수 있다. -> start를 mid + 1로 변경
    if sum > M {
        end = mid - 1
    } else {
        start = mid + 1
    }
}

print(start-1)
