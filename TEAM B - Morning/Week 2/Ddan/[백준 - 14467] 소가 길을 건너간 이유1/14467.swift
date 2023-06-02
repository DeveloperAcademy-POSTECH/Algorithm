//
//  14467.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/05/08.
//

import Foundation

func solution14467() {
    let n : Int = Int(readLine()!)!
    var prob : [String] = ["","","","","","","","","","",""]
    var answer : [Int] = [0,0,0,0,0,0,0,0,0,0,0]
    
    for _ in 0..<n {
        let arr = readLine()!.components(separatedBy: " ")
        if prob[Int(arr[0])!] == "" {
            prob[Int(arr[0])!] = arr[1]
        }else if prob[Int(arr[0])!] != arr[1]{
            answer[Int(arr[0])!] += 1
            prob[Int(arr[0])!] = arr[1]
        }
    }
    
    print(answer.reduce(0, +))
    
}
