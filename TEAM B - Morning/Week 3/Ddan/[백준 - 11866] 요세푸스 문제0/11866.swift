//
//  11866.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/05/15.
//

import Foundation

func solution11866() {
    var prob : [Int] = readLine()!.components(separatedBy: " ").map{ Int(String($0))!}
    var answer : [Int] = []
    var arr : [Int] = []
    var index = prob[1] - 1
    for i in 1...prob[0] {
        arr.append(i)
    }
    while true {
        answer.append(arr[index])
        arr[index] = 0
        if arr.max() == 0 {
            break
        }
        for _ in 0..<prob[1]{
            index += 1
            if index > prob[0]-1 {
                index = 0
            }
            while arr[index] == 0 {
                index += 1
                if index > prob[0]-1 {
                    index = 0
                }
            }
        }
    }
    print("<",terminator: "")
    for i in 0..<answer.count-1{
        print(answer[i],terminator: ", ")
    }
    print(answer.last!,terminator: ">")
}
