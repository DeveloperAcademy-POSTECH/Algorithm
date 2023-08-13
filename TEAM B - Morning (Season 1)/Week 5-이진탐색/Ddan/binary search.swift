//
//  binary search.swift
//  AlgorithmStudy
//
//  Created by 박승찬 on 2023/06/20.
//

import Foundation

func binarySearchRecursive(_ array: [Int], num: Int) -> Bool {
    guard array.count != 1 else {
        return array[0] == num ? true : false
    }
    let mid = array.count / 2
    guard array.count != 2 || array[1] > num else {
        return false
    }
    if array[mid] == num { return true }
    let range = array[mid] > num ? (0..<mid) : ((mid+1)..<array.count)
    return binarySearchRecursive(Array(array[range]), num: num)
}
 
func binarySearchIteration(_ array: [Int], num: Int) -> Bool {
    var start = 0
    var end = (array.count - 1)
    
    while start <= end {
        let mid = (start + end) / 2
        
        if array[mid] == num { return true }
        if array[mid] > num {
            end = mid - 1
        } else {
            start = mid + 1
        }
    }
    return false
}
