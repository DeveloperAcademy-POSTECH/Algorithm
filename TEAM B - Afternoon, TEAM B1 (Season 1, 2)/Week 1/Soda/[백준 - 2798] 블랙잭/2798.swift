//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/05/02.
//
// 백준 2798 블랙잭

// 1. 배열에서 더하기
//let line = readLine()!.split(separator: " ").map { Int($0)! }
//let card = readLine()!.split(separator: " ").map { Int($0)! }
//let N = line[0]
//let M = line[1]
//var result: [Int] = []
//
//for i in 0...N-3 {
//    for j in i+1...N-2 {
//        for k in j+1...N-1 {
//            result.append(card[i]+card[j]+card[k])
//        }
//    }
//}
//
//print(result.filter { $0 <= M }.sorted().last!)

// 2. 조건식 추가
let line = readLine()!.split(separator: " ").map { Int($0)! }
let card = readLine()!.split(separator: " ").map { Int($0)! }
let N = line[0]
let M = line[1]
var sum = 0

for i in 0...N-3 {
    for j in i+1...N-2 {
        for k in j+1...N-1 {
            let check = card[i]+card[j]+card[k]
            if check <= M && sum <= check {
                sum = check
            }
        }
    }
}

print(sum)
