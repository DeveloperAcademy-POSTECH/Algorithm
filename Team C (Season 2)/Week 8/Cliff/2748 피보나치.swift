//
//  2748.swift
//  AlgorithmTest-ReadLine
//
//  Created by 윤범태 on 2023/10/31.
//

import Foundation

/*
 https://www.acmicpc.net/problem/2748
 
 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

 n=17일때 까지 피보나치 수를 써보면 다음과 같다.

 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

 n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 n이 주어진다. n은 90보다 작거나 같은 자연수이다.

 출력
 첫째 줄에 n번째 피보나치 수를 출력한다.

 예제 입력 1
 10
 
 예제 출력 1
 55
 */
func Q_2748() {
    let n = Int(readLine()!)!
    // 문제에 나와있었으니까
    var fibonacci: [Int] = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
    
    if n < fibonacci.count {
        // n = 17까지는
        print(fibonacci[n])
    } else {
        // n = 18 이상부터는 n을 포함하는 범위까지의 피보나치 배열 생성
        for i in fibonacci.count...n {
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        }
        
        print(fibonacci[n])
    }
}
