//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/09/15.
//
// 백준 구간 합 구하기4 https://www.acmicpc.net/problem/11659

/*
❎
for문을 돌고 직접 인덱스를 잘라서 처리 -> 시간초과 (1 ≤ M ≤ 100,000 이므로 최악 - 10만x10만)
*/

//let line = readLine()!.split(separator: " ").map { Int($0)! }
//let (N, M) = (line[0], line[1])
//
//var numbers = readLine()!.split(separator: " ").map { Int($0)! }
//numbers.insert(0, at: 0)
//
//var ranges = Array(repeating: Array(repeating: 0, count: 2), count: M)
//for i in 0..<M {
//    let range = readLine()!.split(separator: " ").map { Int($0)! }
//    ranges[i] = range
//}
//
//var result = [Int]()
//for range in ranges {
//    let (i, j) = (range[0], range[1])
//    let sum = numbers[i...j].reduce(0, +)
//    result.append(sum)
//}
//
//result.forEach {
//    print($0)
//}

/*
✅
시간 초과를 해결하기 위해 구간합을 사용한다 - 시간 복잡도 O(N)
배열을 순회하며 현재 인덱스까지의 모든 값의 합을 합 배열의 요소로 저장한다.
a번째 수부터 b번째 수까지의 합을 구하고 싶다면, 합 배열의 b번째 요소에서 a-1번째 요소를 빼주면 된다.
(1~b번째 요소) - (1~a번째 요소) = (a~b 구간의 합) 이기 때문이다.
*/

let line = readLine()!.split(separator: " ").map { Int($0)! }
let (N, M) = (line[0], line[1])

var numbers = readLine()!.split(separator: " ").map { Int($0)! }
numbers.insert(0, at: 0) // 앞에 0을 추가해서 인덱스

// 구간합 배열 만들기
for i in 1..<numbers.count {
    numbers[i] = numbers[i-1] + numbers[i]
}

// 입력받은 범위를 돌며 결과 출력
for _ in 0..<M {
    let range = readLine()!.split(separator: " ").map { Int($0)! }
    let (i, j) = (range[0], range[1])
    print(numbers[j]-numbers[i-1])
}
