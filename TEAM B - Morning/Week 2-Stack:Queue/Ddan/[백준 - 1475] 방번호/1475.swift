//
//  1475.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/05/16.
//

import Foundation

func solution1475() {
    var input: [Int] = Array(readLine()!).map{ Int(String($0))!}
    var answer: Int = 0
    
    while input.count > 0{
        answer += 1
        for index in 0...9{
            if index == 6 || index == 9{
                if input.contains(6){
                    input.remove(at: input.firstIndex(of: 6)!)
                }else if input.contains(9) {
                    input.remove(at: input.firstIndex(of: 9)!)
                }
            } else {
                if input.contains(index){
                    input.remove(at: input.firstIndex(of: index)!)
                }
            }
        }
    }
    print(answer)
}
