//
//  5597.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/05/09.
//

import Foundation

func solution5597() {
    var student : [Bool] = [true]
    for _ in 0..<30{
        student.append(true)
    }
    for _ in 0..<28{
        student[Int(readLine()!)!] = false
    }
    for i in 1..<student.count{
        if student[i] {
            print(i)
        }
    }
}
