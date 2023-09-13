//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/08/27.
//

// 백준 2473 세 용액 https://www.acmicpc.net/problem/2473

/*
첫 번째 풀이 116ms
0부터 N까지를 순회하는 인덱스 i를 mid 값으로 잡음
순회할 때 start < end로 범위를 만들어서 이분 탐색을 진행했다.
합을 만들어주고, 합의 절댓값이 최소일 때를 찾는다.
합이 0보다 클 때는 end를 한칸 앞쪽으로, (합이 작아져야 한다는 뜻이므로)
합이 0보다 작을 때는 start를 한칸 뒤쪽으로, (합이 커져야 한다는 뜻이므로)
 */

//let N = Int(readLine()!)!
//var nums = readLine()!.split(separator: " ").map { Int($0)! }.sorted()
//var answer = [Int]()
//var max = Int.max
//var sum = Int.min
//
//for i in 0..<N {
//    var start = 0
//    var end = N-1
//
//    while (start < end) {
//        if (i != start) && (i != end) {
//            sum = nums[start] + nums[i] + nums[end]
//
//            if max > abs(sum) {
//                max = abs(sum)
//                answer = [nums[start], nums[i], nums[end]]
//            }
//        }
//
//        if sum > 0 {
//            end -= 1
//        } else if sum < 0 {
//            start += 1
//        } else {
//            break
//        }
//    }
//}
//
//print(answer.sorted().map { String($0) }.joined(separator: " "))

/*
참고 풀이
0부터 N까지 순회하고, start를 mid + 1, end를 N-1로 지정
*/

let N = Int(readLine()!)!
var nums = readLine()!.split(separator: " ").map { Int($0)! }.sorted()
var answer = [Int]()
var max = Int.max

for mid in 0..<N {
    var start = mid + 1
    var end = N - 1

    while start < end {
        let sum = nums[start] + nums[end] + nums[mid]

        if max > abs(sum) {
            max = abs(sum)
            answer = [nums[start], nums[end], nums[mid]]
        }

        if sum < 0 {
            start += 1
        } else {
            end -= 1
        }
    }
}

print(answer.sorted().map { String($0) }.joined(separator: " "))
