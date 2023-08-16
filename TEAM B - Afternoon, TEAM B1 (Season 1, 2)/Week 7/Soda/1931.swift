//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/06/21.
//
// 백준 회의실 배정 https://www.acmicpc.net/problem/1931

/*
회의들의 종료 시간을 고려하여 최대한 많은 회의를 진행하기
회의 종료 시간이 빠른순으로 정렬, 종료 시간이 같다면 시작 시간이 빠른 순으로 정렬(시작 시간과 종료 시간이 같을 수도 있기 때문)
ex. 5-10, 10-10
5-10 -> 10-10은 가능하지만, 10-10 -> 5-10은 불가능함
*/

let N = Int(readLine()!)!
var meetings = [[Int]]()
var answer = 0
var now = -1

// 회의 입력받기
for _ in 0..<N {
    meetings.append(readLine()!.split(separator: " ").map { Int($0)! })
}

// 회의 종료 시간이 빠른순으로 정렬, 종료 시간이 같다면 시작 시간이 빠른 순으로 정렬
//meetings = meetings.sorted {
//    if $0[1] == $1[1] {
//        return $0[0] < $1[0]
//    } else {
//        return $0[1] < $1[1]
//    }
//}

meetings.sort {
    if $0[1] == $1[1] {
        return $0[0] < $1[0]
    } else {
        return $0[1] < $1[1]
    }
}

for i in 0..<meetings.count {
    // 다음 회의의 시작 시간이 현재 회의의 종료 시간 보다 크거나 같을
    if meetings[i][0] >= now {
        now = meetings[i][1]
        answer += 1
    }
}

print(answer)

