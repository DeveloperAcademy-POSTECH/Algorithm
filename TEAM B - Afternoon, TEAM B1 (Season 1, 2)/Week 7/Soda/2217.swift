//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/06/16.
//
// 백준 2217 로프 https://www.acmicpc.net/problem/2217

/*
이 로프들을 이요하여 들어올릴 수 있는 물체의 최대 중량을 구하기 -> 그리디
ex. 10개, 15개이면 각 로프에는 중량이 w/2만큼 가
근데 w/2 <= 10, w/2 <= 15여야 하는 고지 따라서 w는 20이 되나바
그러면 그냥 최소 중량으로만 하면 답 나오는 거 아냐?
예외) 10, 100, 110 이면
10을 버티는 로프를 사용하지 않고, 100, 110 로프만 사용하는 게 효과적임
최대 중량이 제일 큰 로프순으로 꺼내면서 순서대로 병렬로 연결한다 ... 오 이거 괜찮은 듯.
*/

let N = Int(readLine()!)!
var ropes = [Int]()

// 로프 중량 입력받기
for _ in 0..<N {
    ropes.append(Int(readLine()!)!)
}

// 로프 정렬
ropes = ropes.sorted(by: >)
var maxW = 0

/*
case 1) 로프를 병렬로 연결했을 때 -> 최소 중량(반복문에서 현재의 가능 중량) * (index + 1)
case 2) 필요없는 로프는 사용하지 않는 경우
*/

for i in 0..<N {
    maxW = max(maxW, ropes[i] * (i+1))
}

print(maxW)
