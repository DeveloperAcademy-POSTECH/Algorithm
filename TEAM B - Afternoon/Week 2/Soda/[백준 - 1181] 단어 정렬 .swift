//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/05/10.
//
// 백준 1181 단어 정렬 https://www.acmicpc.net/problem/1181

// 1. 중복 제거를 위해 set으로 선언한 뒤 배여롤 변경

//let N: Int = Int(readLine()!)!
//var set: Set = Set<String>()
//
//for _ in 0..<N {
//    set.insert(readLine()!)
//}
//
//var arr = Array(set)
//
//arr = arr.sorted {
//    if $0.count == $1.count {
//        return $0 < $1
//    } else {
//        return $0.count < $1.count
//    }
//}
//
//print(arr.joined(separator: "\n"))

// 2. 딕셔너리 [단어:단어의 길이]로 정렬

let N: Int = Int(readLine()!)!
var dic: Dictionary = [String:Int]()

for _ in 0..<N {
    let word = readLine()!
    dic[word] = word.count
}

var answer = dic.sorted {
    if $0.value == $1.value {
        return $0.key < $1.key
    } else {
        return $0.value < $1.value
    }
}

for i in answer {
    print(i.key)
}
