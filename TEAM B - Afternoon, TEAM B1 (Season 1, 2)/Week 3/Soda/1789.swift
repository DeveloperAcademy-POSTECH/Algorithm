//
//  1789.swift
//  Algorithm
//
//  Created by 김민 on 2023/05/21.
//
// 백준 1789 https://www.acmicpc.net/problem/1789

/*
 1. 처음 풀이
 1부터 차례로 더해서 S 완성 시키기, S보다 합이 커진다면, -1 하기
 */
 
//let S: Int = Int(readLine()!)!
//var count = 0, sum = 0
//
//while true {
//    sum += count
//
//    if sum == S {
//        print(count)
//        break
//    } else if sum > S {
//        print(count - 1)
//        break
//    }
//
//    count += 1
//}

/*
2. 1부터 차례로 더하는 과정을 이진 탐색으로 표현해 보자.
정렬된 자연수들을 사용하기 때문에 이진 탐색 기법 사용 가능!
 */

let S: Int = Int(readLine()!)!
var start = 0
var end = S
var ans = 0

while start <= end {
    let mid = (start + end) / 2
    let sum = (mid * (mid+1))/2
    
    // 1 - mid까지의 합이 S보다 크면 end를 줄인다
    if sum > S {
        end = mid - 1
    } else { // 1 - mid까지 합이 S보다 작거나 같으면 start를 높인다. mid는 따로 저장!
        start = mid + 1
        ans = mid
    }
}

print(ans)
