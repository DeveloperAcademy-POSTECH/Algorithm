//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/09/30.
//
// 백준 9375 패션왕 신해빈 https://www.acmicpc.net/problem/9375

// 테스트 케이스 개수 입력받기
let t = Int(readLine()!)!

for _ in 0..<t {
    let n = Int(readLine()!)!
    var clothes = [[String]]()

    for _ in 0..<n { // 공백으로 분리하여 의상 이름과 종류를 [의상, 종류] 형식으로 저장
        clothes.append(readLine()!.split(separator: " ").map { String($0) })
    }

    var dic = [String: Int]() // 딕셔너리 생성
    clothes.forEach { cloth in
        dic[cloth[1], default: 0] += 1 // 각 종류마다 몇 개가 있는지를 체크해 줌 -> 의상 이름은 따로 저장할 필요가 없다
    }

    var nums = [Int]()
    dic.forEach { (_, value) in // 딕셔너리 value들만 가져옴
        nums.append(value)
    }

    // 조합의 개수를 구하려면 (종류a의 개수+1) * (종류b의 개수+1) ... - 1을 하면 됨.
    // 계산을 위해서 map으로 각 요소들에 1을 더해 줌
    nums = nums.map { $0 + 1 }
    print(nums.reduce(1, *) - 1)
}
