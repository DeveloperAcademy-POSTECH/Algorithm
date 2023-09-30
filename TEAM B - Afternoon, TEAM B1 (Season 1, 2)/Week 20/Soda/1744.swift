//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/09/30.
//
// 백준 1744 수 묶기 https://www.acmicpc.net/problem/1744


/*
입력받을 때 양수 배열, 음수 배열(0 포함)로 나누어 받는다.
[양수 배열]
1. 배열의 개수가 짝수 개일 때는 큰 순서대로 차례차례 묶어 준다.
2. 배열의 개수가 홀수 개일 때도 큰 순서대로 차례차례 묶어 주고, 마지막은 그냥 더하기만 함.
3. 묶을 때 두 수를 더했을 때가 곱했을 때보다 큰 경우도 있음을 주의. (1+1 > 1*1)

[음수 배열]
1. 0이 포함되어 있지 않고 개수가 짝수인 경우 - 묶어서 양수로 만들기
2. 0이 포함되어 있지 않고 개수가 홀수인 경우 - 제일 큰 수(절댓값이 가장 작은 수)만 남겨두고 나머지는 묶기
3. 0이 포함되어 있는데 짝수 개수인 경우 - 제일 큰 수(절댓값이 가장 작은 수) * 0
4. 0이 포함되어 있는데 홀수 개수인 경우 - 제일 작은 수(절댓값이 가장 큰 수) * 0
*/

let N = Int(readLine()!)!
var minus = [Int]()
var plus = [Int]()

// 음수 배열, 양수 배열로 나누기
for _ in 0..<N {
    let num = Int(readLine()!)!
    if num <= 0 {
        minus.append(num)
    } else {
        plus.append(num)
    }
}

var answer = 0

// 양수 배열 - 큰수부터 순회하면서 짝지어서 곱하기
plus.sort(by: >)
var last = plus.count % 2 == 0 ? 0 : plus.removeLast()

for i in stride(from: 0, to: plus.count, by: 2) {
    answer += max(plus[i] * plus[i+1], plus[i] + plus[i+1])
}
answer += last


minus.sort(by: <)
if minus.contains(0) { // 0이 포함되어 있는 경우
    if minus.count == 1 {
        answer += 0
    } else {
        minus.removeLast() // 0 제거
        let _ = minus.count % 2 == 0 ? minus.removeFirst() : minus.removeLast()
        let tmp = minus.count % 2 == 0 ? 0 : minus.removeLast()

        for i in stride(from: 0, to: minus.count, by: 2) {
            answer += (minus[i] * minus[i+1])
        }
        answer += tmp
    }
} else { // 0이 포함되어 있지 않은 경우
    let max = minus.count % 2 == 0 ? 0 : minus.removeLast()
    for i in stride(from: 0, to: minus.count, by: 2) {
        answer += (minus[i] * minus[i+1])
    }
    answer += max
}
print(answer)
