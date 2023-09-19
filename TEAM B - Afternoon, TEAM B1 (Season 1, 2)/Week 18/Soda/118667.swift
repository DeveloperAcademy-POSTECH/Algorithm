//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/09/20.
//
// 프로그래머스 두 큐 합 같게 만들기 https://school.programmers.co.kr/learn/courses/30/lessons/118667

import Foundation

// 투포인터를 pop, insert한 특정한 값을 구하기 -> 투포인터를 사용해 볼까
func solution(_ queue1:[Int], _ queue2:[Int]) -> Int {
    var sum1 = queue1.reduce(0, +)
    var sum2 = queue2.reduce(0, +)
    var totalSum = sum1 + sum2
    var goal = totalSum / 2
    var array = queue1 + queue2 // 큐 2개를 하나의 배열로 합치기
    var answer = 0

    if totalSum % 2 != 0 { // 큐들의 총합이 짝수가 되지 않으면 -1 리턴
        return -1
    }

    var left = 0 // pop할 인덱스
    var right = queue1.count // right 포인터는 queue2의 첫 번째 요소부터 시작, insert할 인덱스

    while (left <= right && right < array.count) { // 범위 지정
        if sum1 < goal {
            sum1 += array[right] // right 포인터에 있는 요소를 합치기
            right += 1 // right 포인터 이동
        } else if sum1 > goal {
            sum1 -= array[left] // left 포인터에 있는 요소 삭제하기
            left += 1 // left 포인터 이동
        } else { // sum1의 합이 goal과 같아졌을 때 - 합을 완성했으므로 탈출
            break
        }
        answer += 1
    }

    // 범위를 넘었을 때, while문의 범위를 넘어서 어떤 방법을 쓰더라도 각 큐의 원소 합을 같게 만들 수 없을 때
    if sum1 != goal {
        return -1
    }

    return answer
}
