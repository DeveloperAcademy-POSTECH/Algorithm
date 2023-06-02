//
//  2493.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/04/23.
//

import Foundation

func solution2493() {
    let n : Int = Int(readLine()!)!
    let prob : [Int] = readLine()!.split(separator: " ").map({
        Int(String($0))!
    })
    var stack1 : [Int] = [] // 탑의 높이
    var stack2 : [Int] = [] // 탑의 인덱스
    var answer : [Int] = [] // 정답
    
    for i in 0...n-1 {
        while true {
            if stack1.isEmpty {
                stack1.append(prob[i])
                stack2.append(i+1)
                answer.append(0)
                break
            } else {
                if stack1[stack1.count-1] > prob[i] {
                    answer.append(stack2[stack2.count-1])
                    stack1.append(prob[i])
                    stack2.append(i+1)
                    break
                } else {
                    stack1.removeLast()
                    stack2.removeLast()
                }
            }
        }
    }
    for i in answer {
        print(i, terminator: " ")
            
    }
}
