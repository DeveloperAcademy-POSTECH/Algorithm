//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/05/22.
//
// 백준 2805 나무 자르기 https://www.acmicpc.net/problem/2805

/*
1. 처음 생각했던 풀이
나무를 정렬한 후에 중간 값으로 전체 배열을 빼보고, 합과 비교하는 이진 탐색을 실시해 보자.
-> 배열에 있는 나무 높이가 아닐 때를 고려하기 성가심
 
2. 따라서 이진 탐색을 실시하되, 중간값을 지정된 나무의 높이만이 아닌 모든 수로 하자!라고 함
-> 성공... 했지만 이게 이진 탐색 문제인지 몰랐다면 풀지 못할 것 같다.
*/

let line: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
let M = line[1]
let trees = readLine()!.split(separator: " ").map { Int($0)! }
var end = trees.max()!
var start = 0

while start <= end {
    let mid = (start + end) / 2
    var sum = 0
    
    for tree in trees {
        if tree > mid { sum += (tree-mid) }
    }
    
    if sum >= M {
        start = mid + 1
    } else { end = mid - 1 }
}

print(start-1)
