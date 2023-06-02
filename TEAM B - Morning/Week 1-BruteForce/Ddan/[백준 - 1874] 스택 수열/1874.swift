//
//  1874.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/03/15.
//

import Foundation

func solution1874(){
    let n : Int = Int(readLine()!)!
    var answer : [String] = []
    var stack : [Int] = []
    var num : Int = 1
    var flag : Bool = true
    for _ in 1...n{
        let prob : Int = Int(readLine()!)!
        while true{
            if prob >= num {
                stack.append(num)
                num += 1
                answer.append("+")
            }else if stack.count == 0 {
                stack.append(num)
                num += 1
                answer.append("+")
            }else if stack[stack.count-1] == prob{
                stack.removeLast()
                answer.append("-")
                break
            }else{
                flag = false
                break
            }
        }
    }
    if flag {
        for i in answer{
            print(i)
        }
    }else{
        print("NO")
    }
}
