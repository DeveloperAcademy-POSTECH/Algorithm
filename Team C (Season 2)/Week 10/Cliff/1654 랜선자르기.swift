//
//  1654.swift
//  AlgorithmTest-ReadLine
//
//  Created by 윤범태 on 2023/11/23.
//

import Foundation

func Q_1654시간초과() {
    let KN: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    var sumOfCables = 0
    var cables: [Int] = []
    for _ in (0..<KN[0]) {
        let input = Int(readLine()!)!
        cables.append(input)
        sumOfCables += input
    }
    
    var start = 0
    var end = sumOfCables / KN[1]
    
    while start <= end {
        let mid = (start + end) / 2
        
        let cuttedCableCount = cables.reduce(0) { $0 + ($1 / mid) }
        
        if cuttedCableCount > KN[1] {
            start = mid
        } else if cuttedCableCount == KN[1] {
            print(mid)
        } else {
            end -= 1
        }
    }
}

// 출처: https://st-lab.tistory.com/269
func Q_1654() {
    let KN: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    
    var sumOfCables = 0
    var cables: [Int] = []
    var maxCable = 0
    
    for _ in (0..<KN[0]) {
        let input = Int(readLine()!)!
        cables.append(input)
        sumOfCables += input
        maxCable = max(maxCable, input) // 입력과 동시에 해당 랜선의 길이가 최댓값인지를 확인하고 max를 갱신
    }
    
    // 반드시 max에서 +1 값이어야 한다.
    maxCable += 1
    
    var min = 0
    var mid = 0
    
    while min < maxCable {
        mid = (min + maxCable) / 2
        let cuttedCableCount = cables.reduce(0) { $0 + ($1 / mid) }
        
        /*
         *  [upper bound 형식]
         *
         *  mid길이로 잘랐을 때의 개수가 만들고자 하는 랜선의 개수보다 작다면
         *  자르고자 하는 길이를 줄이기 위해 최대 길이를 줄인다.
         *  그 외에는 자르고자 하는 길이를 늘려야 하므로 최소 길이를 늘린다.
         */
        if cuttedCableCount < KN[1] {
            maxCable = mid
        } else {
            min = mid + 1
        }
    }
    
    // UpperBound로 얻어진 값(min)에 -1이 최대 길이가 된다.
    print(min - 1)
}

/*
 랜선 자르기
 https://www.acmicpc.net/problem/1654
 
 문제
 집에서 시간을 보내던 오영식은 박성원의 부름을 받고 급히 달려왔다. 박성원이 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.
 
 이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다. 박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)
 
 편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.
 
 입력
 첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다. K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다. 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다. 랜선의 길이는 231-1보다 작거나 같은 자연수이다.
 
 출력
 첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.
 
 예제 입력 1
4 11
802
743
457
539

 예제 출력 1
 200
 
 힌트
 802cm 랜선에서 4개, 743cm 랜선에서 3개, 457cm 랜선에서 2개, 539cm 랜선에서 2개를 잘라내 모두 11개를 만들 수 있다.
 */
