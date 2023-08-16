//
//  1463.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/05/28.
//

import Foundation

func solution1463() {
    guard let N: Int = Int(readLine() ?? "0") else { return }
    
    var answer: [Int] = [0,0,1,1]
    guard N != 1 else {
        print(0)
        return
    }
    guard N != 2 else {
        print(1)
        return
    }
    guard N != 3 else {
        print(1)
        return
    }
    for i in 4...N {
        answer.append(answer[i-1] + 1)
        if i%3 == 0 {
            answer[i] = min(answer[i],answer[i/3]+1)
        }
        if i%2 == 0 {
            answer[i] = min(answer[i],answer[i/2]+1)
        }
        
    }
    print(answer[N])
}
