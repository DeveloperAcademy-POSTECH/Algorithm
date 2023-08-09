//
//  2805.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/06/23.
//

import Foundation

//func solution2805() {
//    let NM: [Int] = readLine()!.components(separatedBy: " ").compactMap{Int(String($0))!}
//    let trees: [Int] = readLine()!.components(separatedBy: " ").compactMap{Int(String($0))!}
//
//    var start: Int = 0
//    var end: Int = trees.max()!
//    var middle = 0
//    var result = 0
//    while start <= end {
//        middle = (start + end) / 2
//        result = 0
//        result = trees.map { $0 > middle ? $0 - middle : 0 }.reduce(0, +)
//        if result >= NM[1] {
//            start = middle + 1
//        } else {
//            end = middle - 1
//        }
//    }
//    print(start-1)
//}


func solution2805() {
    let input = readLine()!.split(separator: " ").compactMap{ Int(String($0))}
    let m = input[1]
    let trees = readLine()!.split(separator: " ").compactMap{ Int(String($0)) }

    var min = 0
    var max = trees.max()!
    var mid = 0
    var result = 0
    var temp = 0

    while min < max {
      mid = (min + max) / 2
      temp = trees.map { $0 > mid ? $0 - mid : 0 }.reduce(0, +)
      
      if(temp < m) {
        max = mid
      } else {
        result = mid
        min = mid + 1
      }
    }

    print(result)
}

