//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/05/04.
//
// 백준 14467 소가 길을 건너간 이유 1 https://www.acmicpc.net/problem/14467

/*
1. 소가 10마리 있다고 했으니 행이 10개인 2차원 배열을 만들어준다. (소 번호에 따라 각 행에 소의 위치 정보를 저장하는 목적)
2. 소의 번호에 따라 만들어둔 배열에서 해당하는 행에 소의 위치 정보를 저장
3. 각 행을 순회하며 빈 배열이 아닐 때는 기존의 위치 정보와 현재 위치 정보를 비교히여 달라졌을 때 결과값 +1
4. 결과값 출력
 
틀렸던 이유?
문제를 제대로 이해하지 못한 듯하다. 위치가 1,0 혹은 0,1 조합만 포함되면 길을 건넌다고 생각했는데 1,0,0,0,1,1은 결과가 2번인
것처럼 이전 위치와 달라졌을 때만 해당됨.
*/

//let N: Int = Int(readLine()!)!
//var arr: [[Int]] = Array(repeating: Array(repeating: 0, count: 0), count: 10)
//var result = 0
//var location = 0
//
//for _ in 0..<N {
//    let line: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
//    arr[line[0]-1].append(line[1])
//}
//
//for i in 0..<10 {
//    if !arr[i].isEmpty { location = arr[i][0] }
//    for j in 0..<arr[i].count {
//        if arr[i][j] != location {
//            location = arr[i][j]
//            result += 1
//        }
//    }
//}
//
//print(result)

/*
행이 10개인 배열을 직접 만들지 않고? 딕셔너리로 넣어볼까여
*/

let N: Int = Int(readLine()!)!
var cows = [Int:Int]()
var result = 0

for _ in 0..<N {
    let line: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
    let num = line[0]
    let location = line[1]
     
    if cows[num] == nil {
        cows[num] = location
    } else {
        if cows[num] != location {
            result += 1
            cows[num] = location
        }
    }
}

print(result)
