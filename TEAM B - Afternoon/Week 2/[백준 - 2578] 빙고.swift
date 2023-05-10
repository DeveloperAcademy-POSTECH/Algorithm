//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/05/08.
//
// 백준 2578 빙고 https://www.acmicpc.net/problem/2578

var bingoBoard = [
    [11, 12, 2, 24, 10],
    [16, 1, 13, 3, 25],
    [6, 20, 5, 21, 17],
    [19, 4, 8, 14, 9],
    [22, 15, 7, 23, 18]
]

let a = bingoBoard[0].firstIndex(of: 2)
var result = 0

for _ in 0..<5 {
    let nums = readLine()!.split(separator: " ").map { Int($0)! }
    
    for i in 0..<5 {
        for j in 0..<5 {
            if let index = bingoBoard[j].firstIndex(of: nums[i]) {
                bingoBoard[j][index] = 0
            }
            
            
        }
    }
}

func bingo() -> Bool {
    var result = 0
    
    // 행 체크
    for i in 0..<5 {
        var sum = 0
        for j in 0..<5 {
            sum += bingoBoard[i][j]
        }
        if sum == 0 {
//            print("행")
            result += 1
        }
    }
    
    // 열 체크
    for i in 0..<5 {
        var sum = 0
        for j in 0..<5 {
            sum += bingoBoard[j][i]
        }
        if sum == 0 {
            result += 1
//            print("열")
        }
    }
    
    // 대각선 체크1
    // ex. 00 11 22 33 44
    var sum1 = 0
    for i in 0..<5 {
        sum1 += bingoBoard[i][i]
    }
    if sum1 == 0 {
        result += 1
//        print("대각선")
    }
    
    // 대각선 체크2
    // ex. 05 13 22 31 40
    var sum2 = 0
    for i in 0..<5 {
        for j in (0..<5).reversed() {
            sum2 += bingoBoard[i][j]
        }
    }
    if sum2 == 0 {
        result += 1
//        print("대각선")
    }
    
    return result >= 3
}
