//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/09/17.
//
// 백준 1520 내리막 길 https://www.acmicpc.net/problem/1520

//  ❎ 시간 초과 - dfs만 활용하였음
let line = readLine()!.split(separator: " ").map { Int($0)! }
let (M, N) = (line[0], line[1]) // 세로 M, 가로 N
var heights = Array(repeating: Array(repeating: 0, count: N), count: M)
var visited = Array(repeating: Array(repeating: false, count: N), count: M)
var result = 0

// 높이 입력받기
for i in 0..<M {
    let line = readLine()!.split(separator: " ").map { Int($0)! }
    heights[i] = line
}

let dx = [1, 0, -1, 0]
let dy = [0, 1, 0, -1]

func dfs(x: Int, y: Int) {
    if x == M - 1 && y == N - 1 {
        result += 1
        return
    }

    for i in 0..<4 {
        let nx = x + dx[i]
        let ny = y + dy[i]

        if 0..<M ~= nx && 0..<N ~= ny {

            if (heights[nx][ny] < heights[x][y]) {
                dfs(x: nx, y: ny)
            }
        }
    }
}

dfs(x: 0, y: 0)
print(result)

//let line = readLine()!.split(separator: " ").map { Int($0)! }
//let (M, N) = (line[0], line[1]) // 세로 M, 가로 N
//var heights = Array(repeating: Array(repeating: 0, count: N), count: M)
//var dp =  Array(repeating: Array(repeating: -1, count: N), count: M)
//
//// 높이 입력받기
//for i in 0..<M {
//    let line = readLine()!.split(separator: " ").map { Int($0)! }
//    heights[i] = line
//}
//
//let dx = [1, 0, -1, 0]
//let dy = [0, 1, 0, -1]
//
//func dfs(x: Int, y: Int) -> Int {
//    if x == M - 1 && y == N - 1 { // 마지막 좌표에 도달 시 종료
//        return 1
//    }
//
//    if dp[x][y] == -1 {
//        dp[x][y] = 0
//
//        for k in 0..<4 {
//            let nx = x + dx[k]
//            let ny = y + dy[k]
//
//            if 0..<M ~= nx && 0..<N ~= ny {
//                if heights[nx][ny] < heights[x][y] {
//                    dp[x][y] += dfs(x: nx, y: ny)
//                }
//            }
//        }
//    }
//
//    return dp[x][y]
//}
//
//print(dfs(x: 0, y: 0))
