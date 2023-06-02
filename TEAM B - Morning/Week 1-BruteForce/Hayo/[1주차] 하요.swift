//
//  main.swift
//  test
//
//  Created by DongHyeok Kim on 2023/05/03.
//

import Foundation


let input = readLine()!.split(separator: " ").map{ Int($0)! }
let n = input[0]
let k = input[1]

let kthDivisor = findKthDivisor(n, k)
print(kthDivisor)



func findDivisors(_ n: Int) -> [Int] {
    var divisors = [Int]()
    for i in 1...n {
        if n % i == 0 {
            divisors.append(i)
        }
    }
    return divisors
}


func findKthDivisor(_ n: Int, _ k: Int) -> Int {
    let divisors = findDivisors(n)
    if k > divisors.count { // K번째 약수가 존재하지 않는 경우
        return 0
    } else {
        return divisors[k-1]
    }
}



