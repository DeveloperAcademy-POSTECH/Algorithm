//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/06/16.
//
// 백준 11047 동전 https://www.acmicpc.net/problem/11047

/*
K원을 만드는 데 동전 개수가 최소가 되려면 가치가 큰 돈을 최대한 많이 써야 함
-> 가치를 저장한 배열을 반대로 반복문을 돌아 사용한 동전 개수를 저장
K는 이때의 나머지가 됨
*/

let nums = readLine()!.split(separator: " ").map { Int($0)! }
let N = nums[0]
var K = nums[1]
var values = [Int]()
var answer = 0

for _ in 0..<N {
    values.append(Int(readLine()!)!)
}

for value in values.reversed() {
    answer += K / value
    K = K % value
}

print(answer)
