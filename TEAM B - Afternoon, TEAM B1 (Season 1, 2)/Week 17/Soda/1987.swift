//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/09/11.
//

// 백준 1987 알파벳 https://www.acmicpc.net/problem/1987
// 인접한 곳을 탐색하긴 하지만, 결국 깊이 우선 탐색을 사용해서 풀이한다

let nums = readLine()!.split(separator: " ").map { Int($0)! }
let (R, C) = (nums[0], nums[1])// R: 세로, C: 가로
var board = [[Int]](repeating: Array(repeating: 0, count: 0), count: R)
var alphabetVisited = Array(repeating: false, count: 26)
// 기존 visited 배열을 만들지 않아도, 26개의 알파벳을 방문했는지 여부만 체크해도 조건들을 만족할 수 있음

for i in 0..<R {
    let line = readLine()!.map { Int($0.asciiValue!) - 65} // 입력을 받을 때 대문자의 아스키값 - 65를 통해 alphabetVisited 배열에 알파벳 순서대로 쉽게 접근할 수 있게 한다
    board[i] = line
}

// 상하좌우를 탐색할 dx, dy 배열
let dx = [-1, 0, 1, 0]
let dy = [0, 1, 0, -1]
var result = 0

func dfs(_ x: Int, _ y: Int, _ count: Int) { // 인덱스와 count를 파라미터로 받는다
    alphabetVisited[board[x][y]] = true // 알파벳을 방문했다고 처리
    result = max(result, count) // 말이 지날 수 있는 최대 칸 수를 구해야 하므로, max로 구해줌

    for i in 0..<4 { // 상하좌우 탐색
        let nx = x + dx[i]
        let ny = y + dy[i]

        if 0..<R ~= nx && 0..<C ~= ny { // 보드의 범위 안에 있다면
            if !alphabetVisited[board[nx][ny]] { // 방문하지 않은 알파벳이라면
                dfs(nx, ny, count+1) // 거기서 한번 더 dfs 탐색 실시, count를 1 늘림으로써 말이 지나간 칸 수를 구해 준다
                alphabetVisited[board[nx][ny]] = false // 탐색이 끝나면 해당 알파벳을 방문하지 않음 처리를 하여 후에 다시 탐색할 수 있게 함
            }
        }
    }
}

dfs(0, 0, 1)
print(result)

/*
 Swift에서 시간 초과를 없애기 위해서는 비트 마스킹을 써야 한다. -> 일단 다른 문제들부터 풀고, 투비 컨티뉴 ... 🥲
 */

//let nums = readLine()!.split(separator: " ").map { Int($0)! }
//let (R, C) = (nums[0], nums[1])// R: 세로, C: 가로
//var board = [[Int]](repeating: Array(repeating: 0, count: 0), count: R)
//var visited = Array(repeating: false, count: 26)
//
//for i in 0..<R {
//    let line = readLine()!.map { Int($0.asciiValue!) - 65}
//    board[i] = line
//}
//
//let dx = [-1, 0, 1, 0]
//let dy = [0, 1, 0, -1]
//var result = 0
//
//func dfs(_ x: Int, _ y: Int, _ count: Int) {
//    visited[board[x][y]] = true
//    result = max(result, count)
//
//    for i in 0..<4 {
//        let nx = x + dx[i]
//        let ny = y + dy[i]
//
//        if 0..<R ~= nx && 0..<C ~= ny {
//            if !visited[board[nx][ny]] {
//                dfs(nx, ny, count+1)
//                visited[board[nx][ny]] = false
//            }
//        }
//    }
//}
//
//dfs(0, 0, 1)
//print(result)
