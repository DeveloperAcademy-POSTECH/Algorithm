//
//  1935.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/03/09.
//

import Foundation

func solution1935(){
    var numArray : [Double] = [] //각 숫자값
    var num : [Double] = [] //피연산자 스택
    var answer : Double = 0
    
    let N = Int(readLine()!)!
    let prob = Array(readLine()!)
    for _ in 1...N{
        numArray.append(Double(readLine()!)!)
    }
    for i in prob{
        switch i {
        case "+" :
            answer = num[num.count-2] + num[num.count-1]
            num.remove(at: num.count-1)
            num.remove(at: num.count-1)
            num.append((answer))
        case "-" :
            answer = num[num.count-2] - num[num.count-1]
            num.remove(at: num.count-1)
            num.remove(at: num.count-1)
            num.append((answer))
        case "*":
            answer = num[num.count-2] * num[num.count-1]
            num.remove(at: num.count-1)
            num.remove(at: num.count-1)
            num.append((answer))
        case "/":
            answer = num[num.count-2] / num[num.count-1]
            num.remove(at: num.count-1)
            num.remove(at: num.count-1)
            num.append((answer))
        default:
            num.append(numArray[Int(i.asciiValue!)-65])
            
        }
    }
    print(String(format: "%.2f",num[0]))
    
}
