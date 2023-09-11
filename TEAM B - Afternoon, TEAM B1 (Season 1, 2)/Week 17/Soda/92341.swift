//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/09/12.
//

// 프로그래머스 주차 요금 정산 https://school.programmers.co.kr/learn/courses/30/lessons/92341

import Foundation

/*
 시간 간격을 계산하는 함수
05:39 형식의 String 타입의 시간을 : 를 이용하여 시, 분으로 구분
 출차 시간과 입차 시간의 간격을 구해서 return
 */
func calculateTimeInterval(_ inTime: String, _ outTime: String) -> Int {
    let inLine = inTime.split(separator: ":").map { Int($0)! }
    let outLine = outTime.split(separator: ":").map { Int($0)! }
    let interval = (outLine[0] * 60 + outLine[1]) - (inLine[0] * 60 + inLine[1])

    return interval
}

func solution(_ fees:[Int], _ records:[String]) -> [Int] {
    var recordsArray = [[String]]()

    // "05:34 5961 IN" -> ["05:34", "5961", "IN"] 으로 분리
    for i in 0..<records.count {
        recordsArray.append(records[i].split(separator: " ").map { String($0) })
    }

    // 번호판 순서대로 정렬하기
    recordsArray.sort { $0[1] < $1[1] }

    // 차 번호판 배열
    var carNumbers = [String]()
    for i in 0..<recordsArray.count {
        if !carNumbers.contains(recordsArray[i][1]) {
            carNumbers.append(recordsArray[i][1])
        }
    }

    // 차 번호판 순서에 따른 시간만 분리한 배열 -> 5971의 ["05:34", "07:59"]
    var carTimes = Array(repeating: Array(repeating: "", count: 0), count: carNumbers.count)

    for i in 0..<carNumbers.count {
    var lines = [String]()
    for j in 0..<recordsArray.count {
        if recordsArray[j][1] == carNumbers[i] {
            lines.append(recordsArray[j][0])
        }
    }
        carTimes[i] = lines
    }

    // 시각 모음 배열의 요소 짝수가 아닐 경우 -> 출차된 내역이 없음 -> 23:59분을 추가해 준다
    for i in 0..<carTimes.count {
        if carTimes[i].count % 2 != 0 {
            carTimes[i].append("23:59")
        }
    }

    // 각 요소들을 돌며 누적 주차 시간 계산, result에 저장
    var result = Array(repeating: 0, count: carNumbers.count)
    for i in 0..<carTimes.count {
        for j in stride(from: 0, to: carTimes[i].count, by: 2) {
            let interval = calculateTimeInterval(carTimes[i][j], carTimes[i][j+1])
            result[i] += interval
        }
    }

    // 최종 주차 요금 계산
    for i in 0..<result.count {
        var total = 0

        if result[i] <= fees[0] { // 기본 시간 이하인 경우는 기본 요금
            total = fees[1]
        } else {
            total = fees[1] + Int(ceil(Double(result[i] - fees[0]) / Double(fees[2]))) * fees[3]
        }
        result[i] = total
    }

    return result
}
