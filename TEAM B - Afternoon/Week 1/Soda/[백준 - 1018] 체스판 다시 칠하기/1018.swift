//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/05/01.
//
// 백준 브루트포스 1018 체스판 다시 칠하기

// 1번 풀이 - 나의 풀이...
// 8x8이 되는 경우의 수로 다 잘라본다.
// 주어진 체스판과 다른 것들의 개수를 찾는다. 얘네를 비교한당.

//let size: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
//let N = size[0], M = size[1]
//var chessBoard: [[String]] = []
//var result: [Int] = []
//
//let white =
//[["W","B","W","B","W","B","W","B"],
// ["B","W","B","W","B","W","B","W"],
// ["W","B","W","B","W","B","W","B"],
// ["B","W","B","W","B","W","B","W"],
// ["W","B","W","B","W","B","W","B"],
// ["B","W","B","W","B","W","B","W"],
// ["W","B","W","B","W","B","W","B"],
// ["B","W","B","W","B","W","B","W"]]
//
//let black =
//[["B","W","B","W","B","W","B","W"],
// ["W","B","W","B","W","B","W","B"],
// ["B","W","B","W","B","W","B","W"],
// ["W","B","W","B","W","B","W","B"],
// ["B","W","B","W","B","W","B","W"],
// ["W","B","W","B","W","B","W","B"],
// ["B","W","B","W","B","W","B","W"],
// ["W","B","W","B","W","B","W","B"]]
//
//// 입력받기
//for _ in 0..<N {
//    chessBoard.append(readLine()!.map { String($0) })
//}
//
//// 체스판의 시작점
//for i in 0..<N-7 {
//    for j in 0..<M-7 {
//        var wCount = 0 // white와 다른 수 체크
//        var bCount = 0 // black과 다른 수 체크
//
//        // 각 시작점으로부터 8x8의 체스판 만들기
//        for a in i..<i+8 {
//            for b in j..<j+8 {
//                if white[a-i][b-j] != chessBoard[a][b] { // white와 체스판의 다른 수 체크
//                    wCount += 1
//                } else if black[a-i][b-j] != chessBoard[a][b] { // black과 체스판의 다른 수 체크
//                    bCount += 1
//                }
//            }
//        }
//
//        result.append(wCount)
//        result.append(bCount)
//    }
//}
//
//print(result.min()!)

// 2. 참고 풀이
// white 체스판, black 체스판을 타이핑하지 않고 성질을 이용하기

let size: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
let N = size[0], M = size[1]
var chessBoard: [[String]] = []
var result: [Int] = []

// 입력받기
for _ in 0..<N {
    chessBoard.append(readLine()!.map { String($0) })
}

for i in 0..<N-7 {
    for j in 0..<M-7 {
        var wCount = 0
        var bCount = 0
        
        for a in i..<i+8 {
            for b in j..<j+8 {
                if (a+b) % 2 == 0 {
                    if chessBoard[a][b] != "B" { // 틀린 개수 체크
                        bCount += 1
                    }
                    if chessBoard[a][b] != "W" {
                        wCount += 1
                    }
                } else {
                    if chessBoard[a][b] != "W" {
                        bCount += 1
                    }
                    if chessBoard[a][b] != "B" {
                        wCount += 1
                    }
                }
            }
        }
        result.append(bCount)
        result.append(wCount)
    }
}

print(result.min()!)
