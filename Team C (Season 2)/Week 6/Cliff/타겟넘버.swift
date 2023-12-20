import Foundation

/*
 문제 설명
 n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

 -1+1+1+1+1 = 3
 +1-1+1+1+1 = 3
 +1+1-1+1+1 = 3
 +1+1+1-1+1 = 3
 +1+1+1+1-1 = 3
 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

 제한사항
 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
 각 숫자는 1 이상 50 이하인 자연수입니다.
 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
 입출력 예
 numbers    target    return
 [1, 1, 1, 1, 1]    3    5
 [4, 1, 2, 1]    4    2
 입출력 예 설명
 입출력 예 #1

 문제 예시와 같습니다.

 입출력 예 #2

 +4+1-2+1 = 4
 +4-1+2-1 = 4
 총 2가지 방법이 있으므로, 2를 return 합니다.
 
 [리뷰]
 - DFS를 사용해서 풀어야 한다고 유추했음
 - 외부에서 반례 찾지 않고 풀었음
 - 자력으로 풀었으나 (A)의 이유로 시간이 많이 걸림
 */

/// https://school.programmers.co.kr/learn/courses/30/lessons/43165
func targetNumber(_ numbers: [Int], _ target: Int) -> Int {
    var numbers = numbers
    let maxDepth = numbers.count
    var resultCount = 0

    func dfs(baseValue: Int, addValue: Int, depth: Int = 0) {
        // A: Terminator가 dfs 재귀하기 이전에 있어야 함 (뒤에 있으면 결과 제대로 안나옴)
        if depth == maxDepth {
            resultCount += baseValue == target ? 1 : 0
            return
        }
        
        dfs(baseValue: baseValue + numbers[depth], addValue: numbers[depth], depth: depth + 1)
        dfs(baseValue: baseValue - numbers[depth], addValue: numbers[depth], depth: depth + 1)
        // print(baseValue, addValue, numbers[depth], depth)
    }
    
    dfs(baseValue: 0, addValue: numbers[0])
    
    return resultCount
}

targetNumber([1, 1, 1, 1, 1], 3)
targetNumber([4, 1, 2, 1], 4)

targetNumber([1, 1, 5], 5)
