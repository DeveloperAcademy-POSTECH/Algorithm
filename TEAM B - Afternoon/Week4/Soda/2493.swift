//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/05/29.
//
// 백준 2493 탑 https://www.acmicpc.net/problem/2493

/*
1. 내 풀이 - 시간 초과
i번째 탑을 검사학 위해 i-1, i-2, ... 해당되는 탑을 만날 때까지 모두 검사
*/

//let N: Int = Int(readLine()!)!
//var stack: [Int] = readLine()!.split(separator: " ").map { Int($0)! }.reversed()
//var index = 0
//var result = ""
//
//while index < stack.count {
//    let top = stack[index]
//    var isExist = false
//
//    for i in index+1..<stack.count {
//        if stack[i] >= top {
//            result += "\(stack.count - i)"
//            isExist = true
//            break
//        }
//    }
//
//    if !isExist { result += "0"}
//    index += 1
//}
//
//for num in result.reversed() {
//    print(num, terminator: " ")
//}

/*
2. 참고 풀이
더 높은 탑을 만나지 못한 탑은 stack에 집어넣기
towers 배열의 탑들을 왼쪽 방향으로 stack에 들어 있는 탑과 비교 (stack은 탑의 번호나 높이가 아닌 index를 저장하는 배열)
더 높은 탑을 마주쳤을 때는 stack의 탑을 pop해 주기
*/

let N: Int = Int(readLine()!)!
var towers: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
var stack: [Int] = []
var result: [Int] = Array(repeating: 0, count: N)

for i in stride(from: N-1, to: -1, by: -1) {
    while !stack.isEmpty && towers[i] > towers[stack.last!] {
        let index = stack.removeLast()
        result[index] = i+1
    }
    stack.append(i)
}

print(result.map { String($0) }.joined(separator: " "))
