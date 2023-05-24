//
//  9461.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/05/21.
//

import Foundation

func solution9461() {
    guard let T: Int = Int(readLine() ?? "0") else {return}
    var answer: [Int] = [1,1,1,2,2]
    
    for i in 4...100{
        answer.append(answer[i-4]+answer[i])
    }
    for _ in 0..<T {
        guard let n: Int = Int(readLine() ?? "0") else {return}
        print(answer[n-1])
    }
}

