//
//  11399.swift
//  AlgorithmTest-ReadLine
//
//  Created by 윤범태 on 2023/10/26.
//

import Foundation

/*
 ATM
 https://www.acmicpc.net/problem/11399
 */

func Q_11399() {
    _ = Int(readLine()!)!
    let elapsedTimes: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }.sorted()
    
    var accTime = 0
    var waitingTimes: [Int] = []
    
    for elapsedTime in elapsedTimes {
        accTime += elapsedTime
        waitingTimes.append(accTime)
    }
    
    let totalElapsedTime = waitingTimes.reduce(0) {
        $0 + $1
    }
    
    print(totalElapsedTime)
}

