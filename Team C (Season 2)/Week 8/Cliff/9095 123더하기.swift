//
//  9095.swift
//  AlgorithmTest-ReadLine
//
//  Created by 윤범태 on 2023/11/01.
//

import Foundation

/*
 1, 2, 3 더하기
 
 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

 1+1+1+1
 1+1+2
 1+2+1
 2+1+1
 2+2
 1+3
 3+1
 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

 출력
 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

 예제 입력 1
 3
 4
 7
 10
 
 예제 출력 1
 7
 44
 274
 */
func Q_9095런타임에러() {
    let T = Int(readLine()!)!
    var Ns: [Int] = []
    
    for _ in 0..<T {
        Ns.append(Int(readLine()!)!)
    }
    
    var sums = [0, 1, 2, 4, 7, 13, 24, 44, 81]
    var results: [Int] = []
    
    for n in Ns {
        if n <= sums.count {
            results.append(sums[n])
        } else {
            for i in sums.count...n {
                sums.append(sums[i - 1] + sums[i - 2] + sums[i - 3])
            }
            
            results.append(sums[n])
        }
    }
    
    // 결과 출력
    for result in results {
        print(result)
    }
}

func Q_9095() {
    var memo: Dictionary<Int, Int> = [:]
    func dp(_ n: Int) -> Int {
        switch n {
        case 0...2:
            return n
        case 3:
            return 4
        default:
            if let memoValue = memo[n] {
                return memoValue
            }
            
            memo[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)
            return memo[n]!
        }
    }
    
    let T = Int(readLine()!)!
    
    (0..<T).map { _ in
        Int(readLine()!)!
    }.forEach {
        print(dp($0))
    }
}
