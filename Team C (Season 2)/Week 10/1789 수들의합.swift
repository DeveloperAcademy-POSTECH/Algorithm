//
//  1789.swift
//  AlgorithmTest-ReadLine
//
//  Created by 윤범태 on 2023/11/22.
//

import Foundation

func Q_1789() {
    let N = Int(readLine()!)!
    
    guard N > 1 else {
        print(N)
        return
    }
    
    let root = Int(round(sqrt(Double(N))))

    for i in root...(4294967295) {
        let sum = (i * (i + 1)) / 2
        
        if sum == N {
            print(i)
            break
        } else if sum > N {
            print(i - 1)
            break
        }
    }
}

/*
 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

 입력
 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

 출력
 첫째 줄에 자연수 N의 최댓값을 출력한다.

 예제 입력 1
 200
 예제 출력 1
 19
 */
