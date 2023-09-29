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

-> 개수가 적어서 직접 전부 다 해 봐도 될 것 같고, 암호의 조합을 구할 때는 dfs/백트래킹을 사용할 것 같다고 생각
*/

//// 입력받기
//let nums = readLine()!.split(separator: " ").map { Int($0)! }
//let (L, C) = (nums[0], nums[1])
//let words = readLine()!.split(separator: " ").map { String($0) }
//
//// 입력받은 문자를 모음과 자음으로 구분하기
//let vowels = ["a", "e", "i", "o", "u"]
//var wordsVowels = [String]()
//var wordsConsonants = [String]()
//
//words.forEach { word in
//    if vowels.contains(where: { $0 == word }) {
//        wordsVowels.append(word)
//    } else {
//        wordsConsonants.append(word)
//    }
//}
//
//
//// 조합 구하기
//var result1 = [[String]]()
//var result2 = [[String]]()
//
// 자음 조합 & 모음 조합을 구하는 dfs 함수
//func consonantsDfs(_ index: Int, _ now: [String], _ depth: Int) {
//    if now.count == depth {
//        result1.append(now)
//        return
//    }
//
//    for i in index..<wordsConsonants.count {
//        consonantsDfs(i+1, now + [wordsConsonants[i]], depth)
//    }
//}
//
//func vowelsDfs(_ index: Int, _ now: [String], _ depth: Int) {
//    if now.count == depth {
//        result2.append(now)
//        return
//    }
//
//    for i in index..<wordsVowels.count {
//        vowelsDfs(i+1, now + [wordsVowels[i]], depth)
//    }
//}
//
//
//for i in 2..<L {
//    // 자음 조합 구하기
//    consonantsDfs(0, [], i)
//
//    // 모음 조합 구하기
//    let vowelsCount = L - i
//    vowelsDfs(0, [], vowelsCount)
//}
//
// 만들어진 자음 조합에서 추가해야 하는 개수만큼을 구해 알맞은 모음 조합들을 추가해 주고 출력
//var finalResults = [String]()
//result1.forEach { words in
//    let vowelsToAdd = L - words.count
//    result2.forEach { vowels in
//        if vowels.count == vowelsToAdd {
//            let key = words + vowels
//            finalResults.append(key.sorted().joined(separator: ""))
//        }
//    }
//}
//
//finalResults.sorted().forEach { key in
//    print(key)
//}

/*
2.
*/

// 입력받기
let nums = readLine()!.split(separator: " ").map { Int($0)! }
let (L, C) = (nums[0], nums[1])
let words = readLine()!.split(separator: " ").map { String($0) }.sorted()

// 입력받은 문자를 모음과 자음으로 구분하기
let vowels = ["a", "e", "i", "o", "u"]
var result = [String]()

func dfs(start: Int, vowelsCount: Int, consonantsCount: Int) {
    // 암호 문자의 개수가 L개가 되었고, 모음 최소 개수가 1개, 자음 최소 개수가 2개 이상인 경우 출력
    if result.count == L && vowelsCount > 0 && consonantsCount > 1 {
        print(result.joined(separator: ""))
        return
    }

    // start ~ C까지 순회
    for i in start..<C {
        result.append(words[i])

        if vowels.contains(words[i]) { // 모음을 포함하는 경우
            dfs(start: i+1, vowelsCount: vowelsCount+1, consonantsCount: consonantsCount)
        } else {
            dfs(start: i+1, vowelsCount: vowelsCount, consonantsCount: consonantsCount+1)
        }

        result.removeLast()
    }
}

dfs(start: 0, vowelsCount: 0, consonantsCount: 0)

