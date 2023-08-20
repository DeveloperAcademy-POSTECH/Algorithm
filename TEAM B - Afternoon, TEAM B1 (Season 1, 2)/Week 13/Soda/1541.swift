//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/08/14.
//

// 백준 1541 잃어버린 괄호 https://www.acmicpc.net/problem/1541

/*
✅
1. 최소를 만드려면 빼기를 최대한 이용해야겠다고 생각
-를 만날 때마다 잘라 새로운 배열을 만들어줌.
calculate 함수를 만들어 해당 배열의 요소들을 더한 값들의 배열을 return
ex. [55-50+40] -> ["55", "50+40"] -> [50, 90]
각 요소들을 전부 뺀 값을 출력
*/

//func calculate(_ expression: [String]) -> [Int] {
//    var result = [Int]()
//
//    for i in expression {
//        let tmp = i.split(separator: "+").map { Int($0)! }.reduce(0, +)
//        result.append(tmp)
//    }
//
//    return result
//}
//
//let expression = readLine()!.split(separator: "-").map { String($0) }
//let result = calculate(expression)
//print(result.dropFirst().reduce(result[0], -))


/*
✅
expression을 -를 기준으로 잘라준다
각 배열의 요소들의 합을 result 배열에서 빼준다.
주의할 점은 첫 번째 요소는 빼기가 아니라 그 값 그대로, 나머지는 빼주기
result가 그대로 결과가 된다
*/

let expression = readLine()!.split(separator: "-").map { String($0) }
var result = 0

for i in 0..<expression.count {
    let tmp = expression[i].split(separator: "+").map { Int($0)! }.reduce(0, +)

    if i == 0 {
        result = tmp
        continue
    }

    result -= tmp
}

print(result)
