//
//  17298.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/04/25.
//

import Foundation

func solution17298() {
    let n : Int = Int(readLine()!)!
    let prob : [Int] = readLine()!.split(separator: " ").map({
        Int(String($0))!
    })
    let list = prob.reversed()
    var stack : [Int] = []
    var answer : [Int] = []
    for i in list {
        while true {
            if stack.isEmpty {
                answer.append(-1)
                stack.append(i)
                break
            }else if stack[stack.count-1] > i {
                answer.append(stack[stack.count-1])
                stack.append(i)
                break
            }else {
                stack.removeLast()
            }
        }
                
    }
    print(answer.reversed().map{String($0)}.joined(separator: " "))
    
}
