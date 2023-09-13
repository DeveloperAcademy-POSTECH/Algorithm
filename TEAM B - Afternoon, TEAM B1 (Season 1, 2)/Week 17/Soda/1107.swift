//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/09/06.
//

// 백준 1107 리모컨 https://www.acmicpc.net/problem/1107

/*
버튼의 개수 10개? -> 그냥 다 해봐도 되려나?
case 0) 고장난 개수가 0개라면 그냥 N의 자릿수만큼이 답이 됨
case 1) 고장난 버튼이 N에 포함되지 않는다면, N의 자릿수 혹은 100에서 +, -로 만졌을 때의 최소 중 하나
case 2) 고장난 버튼이 N에 포함된다면, 고장난 애들이 없지만 N에 최대한 가까운 수를 찾아(+1, -1을 해주며) 해결 or 100에서 +, -로 만졌을 때 최소 중 하나

런타임 에러가 났던 이유
고장난 버튼이 0개이면 아예 입력이 불가능하도록 처리했어야 했다
*/


let N = Int(readLine()!)!
let count = Int(readLine()!)!
let NCount = String(N).count
let originResult = N > 100 ? N - 100 : 100 - N
var buttons = [Int]()
if count != 0 {
    buttons = readLine()!.split(separator: " ").map { Int(String($0))! }
}

if count == 0 { // 고장난 버튼이 없을 때
    print(min(NCount, originResult))
} else if N == 100 {
    print(0)
} else if !(String(N).map({ Int(String($0))! }).contains(where: { buttons.contains($0) })) {
    print(min(NCount, originResult))
} else {
    var tmpA = N
    var tmpB = N
    var resultA = Int.max
    var resultB = Int.max

    while (tmpA > 0) { // 채널은 음수가 존재하지 않음
        tmpA -= 1
        let a = String(tmpA).map { Int(String($0))! }.contains { buttons.contains($0) }

        if !a {
            resultA = N - tmpA + String(tmpA).count
            break
        }
    }

    while (tmpB < 999901) { // 0 <= N <= 500,000 이므로 최악의 경우는 100번에서 499900번 + 버튼을 눌러 500000 채널로 이동하는 것
        tmpB += 1
        let b = String(tmpB).map { Int(String($0))! }.contains { buttons.contains($0) }

        if !b {
            resultB = tmpB - N + String(tmpB).count
            break
        }
    }
    print(min(resultA, resultB, originResult))
}
