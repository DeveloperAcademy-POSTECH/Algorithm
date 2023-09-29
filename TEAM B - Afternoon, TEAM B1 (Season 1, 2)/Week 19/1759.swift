//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/09/29.
//
// 백준 1759 암호 만들기 https://www.acmicpc.net/problem/1759
/*
최소 1개의 모음 + 최소 2개의 자음으로 구성됨
암호를 이루는 알파벳은 증가하는 순서로 배열됐을 것
C개의 문자들이 주어졌을 때 조합하여 가능성 있는 암호들을 전부 구하기
그냥 구현 문제 아닐까?
*/

// 입력받기
let nums = readLine()!.split(separator: " ").map { Int($0)! }
let (L, C) = (nums[0], nums[1])
let words = readLine()!.split(separator: " ").map { String($0) }

// 입력받은 문자를 모음과 자음으로 구분하기
let vowels = ["a", "e", "i", "o", "u"]
var wordsVowels = [String]()
var wordsConsonants = [String]()

words.forEach { word in
    if vowels.contains(where: { $0 == word }) {
        wordsVowels.append(word)
    } else {
        wordsConsonants.append(word)
    }
}


// 조합 구하기
var result1 = [[String]]()
var result2 = [[String]]()

func consonantsDfs(_ index: Int, _ now: [String], _ depth: Int) {
    if now.count == depth {
        result1.append(now)
        return
    }

    for i in index..<wordsConsonants.count {
        consonantsDfs(i+1, now + [wordsConsonants[i]], depth)
    }
}

func vowelsDfs(_ index: Int, _ now: [String], _ depth: Int) {
    if now.count == depth {
        result2.append(now)
        return
    }

    for i in index..<wordsVowels.count {
        vowelsDfs(i+1, now + [wordsVowels[i]], depth)
    }
}


for i in 2..<L {
    // 자음 조합 구하기
    consonantsDfs(0, [], i)

    // 모음 추가하기
    let vowelsCount = L - i
    vowelsDfs(0, [], vowelsCount)
}

var finalResults = [String]()
result1.forEach { words in
    let vowelsToAdd = L - words.count
    result2.forEach { vowels in
        if vowels.count == vowelsToAdd {
            let key = words + vowels
            finalResults.append(key.sorted().joined(separator: ""))
        }
    }
}

finalResults.sorted().forEach { key in
    print(key)
}
