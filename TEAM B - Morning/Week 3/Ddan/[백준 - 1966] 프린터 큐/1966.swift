//
//  1966.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/05/15.
//

import Foundation

func solution1966() {
    let n : Int = Int(readLine()!)!
    
    for _ in 0..<n {
        var prob : [Int] = readLine()!.components(separatedBy: " ").map{
            Int(String($0))!
        }
        var arr : [Int] = readLine()!.components(separatedBy: " ").map{
            Int(String($0))!
        }
        
        var index = 0
        var answer = 0
        while true {
            if arr[index] == arr.max(){
                arr.remove(at: index)
                answer += 1
                prob[0] -= 1
                if index < prob[1]{
                    prob[1] -= 1
                }else if index == prob[1]{
                    print(answer)
                    break
                }
                if index > prob[0]-1 {
                    index = 0
                }
            }else {
                if index >= prob[0]-1{
                    index = 0
                }else {
                    index += 1
                }
            }
        }
    }
    
}

