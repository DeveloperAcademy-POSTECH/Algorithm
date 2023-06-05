//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/05/27.
//
// 프로그래머스 기능개발 https://school.programmers.co.kr/learn/courses/30/lessons/42586


import Foundation

/*
 1. 큐를 이용한 풀이
 남은 일수를 계산하여 queue 배열에 append
 인덱스를 사용하여 배포일 계산 -> index 변수를 따로 만들어 뒤에 있는 기능이 앞에 있는 기능과 함께 배포되도록 함
 */

//
//func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
//    var queue: [Int] = []
//
//    // 남은 일수 계산
//    for i in 0..<progresses.count {
//        queue.append(Int(ceil(Double(100 - progresses[i]) / Double(speeds[i]))))
//    }
//
//    // 배포
//    var index = 0
//    var result: [Int] = []
//
//    for i in 1..<progresses.count {
//        if queue[i] > queue[index] {
//            result.append(i - index)
//            index = i
//        }
//    }
//    result.append(progresses.count - index)
//
//    return result
//}

// ---------------------------------------------------------------------------------------

/*
 2. 작업의 개수가 100개 이하이니까 배포일도 무조건 100이하 일 것 -> 크기 100 days 배열 생성
    작업이 진도율이 100%가 될 때를 체크한다. 100이 될 때까지 배포일을 1씩 더해 줌.
    진도율이 100이 되면 해당 배포일에 +1 (days의 인덱스를 활용)
    filter을 사용하여 0을 제외한 나머지 수들만 출력
 */

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var days: [Int] = Array(repeating: 0, count: 100)
    var day = -1
    
    for i in 0..<progresses.count {
        while (progresses[i] + day * speeds[i]) < 100 { day += 1 }
        days[day] += 1
    }
    
    return days.filter { $0 != 0}
}
