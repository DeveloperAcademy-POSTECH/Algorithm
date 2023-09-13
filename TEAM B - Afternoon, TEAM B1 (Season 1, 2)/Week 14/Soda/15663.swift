//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/08/21.
//

// 백준 15663 N과 M(9) https://www.acmicpc.net/problem/15663
/*
❎
부분 수열 -> 백트래킹일까? 했는데 맞았음
중복을 걸러야 하기 때문에 이전과 동일한 수가 나오면 넘어가는 로직이 필요함
*/

// 입력
let line = readLine()!.split(separator: " ").map { Int($0)! }
let (N, M) = (line[0], line[1])
let nums = readLine()!.split(separator: " ").map { Int($0)! }.sorted() // 오름차순으로 정렬한다 💡
var visited = Array(repeating: false, count: N+1) // 방문 체크
var stack = [Int]() // 출력될 수열

// dfs 함수
func dfs(_ num: Int, _ count: Int) {
    var before = 0

    if count == M { // stack이 M개가 되면 수열이 완성되었으므로 출력함
        print(stack.map { String($0) }.joined(separator: " "))
        return // dfs() 함수 종료
    }

    for i in 0..<N {
        /*
         방문하지 않고, 이전 수와 다르면 조건문 실행한다.
         해당 인덱스의 visitied를 true로 바꾸고, stack에 집어넣는다.
         이전 수를 저장하기 위해 before에 해당 수(num[i])를 저장한다.
         */
        if !visited[i] && nums[i] != before {
            visited[i] = true
            stack.append(nums[i])
            before = nums[i]
            dfs(i, count+1)
            visited[i] = false
            stack.removeLast()
        }
    }
}

dfs(nums[0], 0)
