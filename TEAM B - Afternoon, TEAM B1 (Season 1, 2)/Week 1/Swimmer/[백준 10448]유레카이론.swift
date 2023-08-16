/*
접근
- 삼각수가 모여있는 집합을 만든다.
- 삼각수 집합을 이용하여 순서 없이 중복 허용된 요소 3개를 뽑아 더한다.
- 해당 자연수는 3개로 표현할 수 있는 자연수이다. 이를 result 배열에 1로 저장한다.
- 입력받은 정수를 x라 할 때, result[x]를 출력한다.
- result 배열에는 유레카 정수인 경우만 1로 저장된다.
- result 배열에는 유레카 정수인 경우만 1로 저장된다.
- 중복 허용으로 3개를 뽑는 경우는 44 * 43 * 42 / 3이므로, 26,000로 무식하게 풀 수 있다.
*/

import Foundation




let test = Int(readLine()!)!
var triangleNumbers = [1]
var result = [Int](repeating: 0, count: 1001)
var num = 1, count = 2
// 삼각수 구하기
while num <= 1000 {
    num += count
    triangleNumbers.append(num)
    count += 1
}
let length = triangleNumbers.count
// 중복 허용 3개의 요소 뽑기
for i in 0 ..< length {
    for j in i ..< length {
        for k in j ..< length {
            let number = triangleNumbers[i] + triangleNumbers[j] + triangleNumbers[k]
            guard number <= 1000 else { continue }
            result[number] = 1
        }
    }
}
// 결과 출력
for _ in 0 ..< test {
    print(result[Int(readLine()!)!])
}