//
//  1912.swift
//  AlgorithmTest-ReadLine
//
//  Created by 윤범태 on 2023/11/01.
//

import Foundation

func Q_1912실패() {
    let array = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
    var a2: [Int] = []
    var a3: [Int] = []
    var a4: [Int] = []
    var a5: [Int] = []
    var a6: [Int] = []
    var a7: [Int] = []
    var a8: [Int] = []
    var a9: [Int] = []
    var a10: [Int] = []
    
    for i in 0..<array.count - 1 {
        a2.append(array[i] + array[i + 1])
    }
    
    for i in 0..<array.count - 2 {
        a3.append(array[i] + array[i + 1] + array[i + 2])
    }
    
    for i in 0..<array.count - 3 {
        a4.append(array[i] + array[i + 1] + array[i + 2] + array[i + 3])
    }
    
    for i in 0..<array.count - 4 {
        a5.append(array[i] + array[i + 1] + array[i + 2] + array[i + 3] + array[i + 4])
    }
    
    for i in 0..<array.count - 5 {
        a6.append(array[i] + array[i + 1] + array[i + 2] + array[i + 3] + array[i + 4] + array[i + 5])
    }
    
    for i in 0..<array.count - 6 {
        a7.append(array[i] + array[i + 1] + array[i + 2] + array[i + 3] + array[i + 4] + array[i + 5] + array[i + 6])
    }
    
    for i in 0..<array.count - 7 {
        a8.append(array[i] + array[i + 1] + array[i + 2] + array[i + 3] + array[i + 4] + array[i + 5] + array[i + 6] + array[i + 7])
    }
    
    for i in 0..<array.count - 8 {
        a9.append(array[i] + array[i + 1] + array[i + 2] + array[i + 3] + array[i + 4] + array[i + 5] + array[i + 6] + array[i + 7] + array[i + 8])
    }
    
    for i in 0..<array.count - 9 {
        a10.append(array[i] + array[i + 1] + array[i + 2] + array[i + 3] + array[i + 4] + array[i + 5] + array[i + 6] + array[i + 7] + array[i + 8] + array[i + 9])
    }
    
    print(array)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
    print(a6)
    print(a7)
    print(a8)
    print(a9)
    print(a10)
}

/*
 연속합
 
 n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.

 예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

 입력
 첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

 출력
 첫째 줄에 답을 출력한다.

 예제 입력 1
 10
 10 -4 3 1 5 6 -35 12 21 -1
 
 예제 출력 1
 33
 
 예제 입력 2
 10
 2 1 -4 3 4 -4 6 5 -5 1
 
 예제 출력 2
 14
 
 예제 입력 3
 5
 -1 -2 -3 -4 -5
 
 예제 출력 3
 -1
 
 [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
 [6, -1, 4, 6, 11, -29, -23, 33, 20]
 [9, 0, 9, 12, -24, -17, -2, 32]
 [10, 5, 15, -23, -12, 4, -3]
 [15, 11, -20, -11, 9, 3]
 [21, -24, -8, 10, 8]
 [-14, -12, 13, 9]
 [-2, 9, 12]
 [19, 8]
 [18]
 
 https://black-hair.tistory.com/107
 총합이 음수로 되는 경우에는 처음부터 새로 시작하는 것이
 더 큰 숫자를 만들 수 있기 때문에 총 합을 0으로 초기화하고 새로 시작하면 된다.

 이렇게 구현하는 경우에는 단순합 연산만 이용하여 구할수 있게 된다.
 
 */

func Q_1912() {
    let n = Int(readLine()!)!
    let array: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    
    var result: Int = array[0]
    var total: Int = 0
    
    for i in 0..<n {
        result = max(result, total + array[i])
        total += array[i]
        total = max(0, total)
    }
    
    print(result)
}
