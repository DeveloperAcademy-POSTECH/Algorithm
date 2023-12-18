//
//  2512.swift
//  AlgorithmTest-ReadLine
//
//  Created by 윤범태 on 2023/11/22.
//

import Foundation

/*
 https://www.acmicpc.net/problem/2512
 예산
 
 문제
 국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것이다. 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다. 그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.

 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.
 예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다.

 여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.

 입력
 첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다. 다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다. 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다.

 출력
 첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다.

예제 입력 1
4
120 110 140 150
485

예제 출력 1
127

예제 입력 2
5
70 80 30 40 100
450

예제 출력 2
100
 
 == 반례 ==
 
5
100 100 100 100 100
10
 
 answer: 2
 
4
111 111 143 153
323
 
 answer: 80
 
10
1 1 1 1 11 11 11 11 11 100
100
 
 answer: 41
 output: 아예안됨
 */

func Q_2512실패() {
    let N = Int(readLine()!)!
    let reqBudgets: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    let M = Int(readLine()!)!
    
    let avrOfReqBudgets = Double(reqBudgets.reduce(0, { $0 + $1 })) / Double(N)
    let averageOfM = Double(M) / Double(N)
    
    guard avrOfReqBudgets > averageOfM else {
        print(reqBudgets.max()!)
        return
    }
    
    let budgetsLowThanAvrOfM = reqBudgets
        .filter { $0 <= Int(averageOfM) }
    let sumsOfLower = budgetsLowThanAvrOfM.reduce(0) { $0 + $1 }
    
    for maxValue in Int(averageOfM)...Int(avrOfReqBudgets) + 1 {
        let sum = maxValue * (reqBudgets.count - budgetsLowThanAvrOfM.count) + sumsOfLower
        if sum >= M {
            print(maxValue - 1)
            return
        }
    }
}


// 출처: https://computer-science-student.tistory.com/662
func Q_2512() {
    let _ = Int(readLine()!)!
    let reqBudgets: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    let M = Int(readLine()!)!
    
    var start = 0
    var end = reqBudgets.max()!
    
    while start <= end {
        // 상한액 설정
        let mid = (start + end) / 2
        // 지급할 예산 총액
        var sum = 0
        
        for budget in reqBudgets {
            // 요청한 금액이 상한액 이상/미만이라면
            if budget >= mid {
                sum += mid // 상한액 더하기
            } else {
                sum += budget // 요청액 더하기
            }
        }
        
        // 지급할 예산 총액이 구비된 총 예산 이하/초과라면
        if sum <= M {
            start = mid + 1
        } else {
            end = mid - 1
        }
    }
    
    print(end)
}
