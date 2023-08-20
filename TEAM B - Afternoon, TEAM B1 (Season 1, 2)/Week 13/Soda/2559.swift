//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/08/14.
//

// 백준 2559 수열 https://www.acmicpc.net/problem/2559

/*
 ❎
 1. 가장 먼저 떠올랐던 각 반복마다 인덱스를 잘라서 합을 계산하는 방법
 정답 비율이 낮기도 하고, 시간 제한이 1초라서 안 될 것 같긴 했는데 역시나 안 됐음. ㅎ 🥲
*/
//let input = readLine()!.split(separator: " ").map { Int($0)! }
//let (N, K) = (input[0], input[1])
//let temperatures = readLine()!.split(separator: " ").map { Int($0)! }
//var max = temperatures.min()!
//
//for i in 0...temperatures.count-K {
//    var sum = 0
//    for j in i..<i+K {
//        sum += temperatures[j]
//    }
//    if sum > max { max = sum }
//}
//
//print(max)

/*
 ❎
 2. 1번의 고차 함수 버전
 */

//let input = readLine()!.split(separator: " ").map { Int($0)! }
//let (N, K) = (input[0], input[1])
//var temperatures = readLine()!.split(separator: " ").map { Int($0)! }
//
//var result = temperatures[0..<K].reduce(0, +)
//
//for i in K...N {
//    let sum = temperatures[(i-K)..<i].reduce(0, +)
//    result = max(result, sum)
//}
//
//print(result)


/*
✅
3. 구간합 알고리즘 사용하기
입력받은 온도들을 누적 합 배열로 만들어 준다.
ex = 3 -2 -4 -9 0 3 7 13 8 -3 -> 3 1 -3 -12 -12 -9 -2 11 19 16
result의 첫 번째 요소는 인덱스를 고려해 직접 지정해 준다.
온도들을 뒤에서부터 돌면서 구간합 (sum[i] - sum[i-K])을 구해 준다.
구간합 배열에서 또 최대를 구해주기
*/

//let input = readLine()!.split(separator: " ").map { Int($0)! }
//let (N, K) = (input[0], input[1])
//var nums = readLine()!.split(separator: " ").map { Int($0)! }
//var sum = [Int]()
//var result = [Int]()
//
//// 누적 합 배열 만들어주기
//for i in 0..<N {
//    if i == 0 {
//        sum.append(nums[i])
//    } else {
//        sum.append(sum[i-1] + nums[i])
//    }
//}
//
//result.append(sum[K-1])
//
//for i in stride(from: sum.count-1, through: K, by: -1) {
//    result.append(sum[i] - sum[i-K])
//}
//
//print(result.max()!)

/*
✅
4. 더 간략한 풀이
sum의 첫 번째 요소를 0번째 인덱스~K-1번째 인덱스까지의 합으로 지정해 준다.
K부터 N 미만까지 반복문을 순회한다.

백준 예제를 예시로 풀이해 보면,
nums = [3, -2, -4, -9, 0, 3, 7, 13, 8, -3]
그리고 3+(-2)를 해 주면, 우선 sum = 1 이다.
나는 -4 + -2의 값을 구해야 하고, sum에는 3 + -2의 값이 저장되어 있다.
따라서 result에 -2 값을 제외한 -4-3(i = K, nums[i] - nums[i-K])의 값을 더해 준다.
-9 + -4의 값을 구해야 할 때, sum에는 -4 + -2의 값이 저장되어 있다.
result에 -4 값을 제외한 -9-(-2)를 더해 준다.
최댓값이 되면 갱신해 준다.
*/

let input = readLine()!.split(separator: " ").map { Int($0)! }
let (N, K) = (input[0], input[1])
let nums = readLine()!.split(separator: " ").map { Int($0)! }
var sum = nums[0..<K].reduce(0, +)
var result = sum

for i in K..<N {
    sum += nums[i] - nums[i-K]
    result = max(result, sum)
}

print(result)
