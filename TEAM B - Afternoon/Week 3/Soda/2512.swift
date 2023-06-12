//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/05/23.
//
// 백준 2512 예산 https://www.acmicpc.net/problem/2512

/*
상한액, 가능한 한 최대의 ... -> 이진 탐색으로 예상
각 지방의 예산 중 최대를 end로 하고, 이진 탐색 실시
예산이 mid 값보다 클 때는 mid 값을 합하고, mid 값보다 작을 때는 예산을 합합으로써 예산 배정 실시
*/

let N: Int = Int(readLine()!)!
let nums: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
let M: Int = Int(readLine()!)!

var start = 0
var end = nums.max()!

while start <= end {
    let mid = (start + end) / 2
    var sum = 0
    
    for num in nums {
        if mid > num {
            sum += num
        } else {
            sum += mid
        }
    }
    
    if M >= sum {
        start = mid + 1
    } else {
        end = mid - 1
    }
}

print(start - 1)
