//
//  1003.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/05/20.
//

import Foundation

func solution1003(){
    let n: Int = Int(readLine()!)!
    
    for _ in 0..<n {
        let num: Int = Int(readLine()!)!
        let answer: [Int] = fibonacci(num)
        print(answer.map{String($0)}.joined(separator: " "))
    }
}

func fibonacci(_ n: Int) -> [Int] {
    var cache: [[Int]] = [[0,1],[1,1]]
    guard n != 0 else {
        return [1,0]
    }
    guard n != 1 else{
        return [0,1]
    }
    for i in 2..<n{
        cache.append([cache[i-1][0]+cache[i-2][0],cache[i-1][1]+cache[i-2][1]])
    }
    return cache[n-1]
}
