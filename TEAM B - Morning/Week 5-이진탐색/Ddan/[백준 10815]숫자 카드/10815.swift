//
//  10815.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/06/20.
//

import Foundation

func solution10815() {
    guard let n: Int = Int(readLine() ?? "0") else {
        return
    }
    var probArray: [Int] = readLine()!.components(separatedBy: " ").map { Int(String($0))!}
    guard let m: Int = Int(readLine() ?? "0") else {
        return
    }
    var compArray: [Int] = readLine()!.components(separatedBy: " ").map{ Int(String($0))!}
    
    var answer: [String] = []
    probArray.sort()
    
    for index in compArray {
        var start: Int = 0
        var end: Int = probArray.count-1
        var flag = false
        while start <= end {
            let mid = (end + start)/2
            if probArray[mid] == index {
                flag = true
                break
            }else if probArray[mid] > index {
                end = mid - 1
            }else {
                start = mid + 1
            }
        }
        if flag {
            answer.append("1")
        } else {
            answer.append("0")
        }
    }
    print(answer.joined(separator: " "))
}

