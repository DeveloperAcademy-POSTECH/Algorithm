//
//  10799.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/04/23.
//

import Foundation

func solution10799(){
    let prob = Array(readLine()!)
    var stack : [Any] = []
    var answer = 0
    for i in 0...prob.count-1{
        if prob[i] == "(" {
            stack.append(prob[i])
        } else {
            if prob[i-1] == "(" {
                stack.removeLast()
                answer += stack.count
            }else {
                stack.removeLast()
                answer += 1
            }
        }
    }
    print(answer)
}

extension String {
    subscript(_ index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}
