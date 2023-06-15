//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/06/06.
//
// 백준 10026 적록색약 https://www.acmicpc.net/problem/10026

// 1. 2가지 케이스 모두 구현
//let N = Int(readLine()!)!
//var matrix: [[Character]] = Array(repeating: Array(repeating: "A", count: N), count: N)
//var visited = Array(repeating: Array(repeating: false, count: N), count: N)
//var rgVisited = Array(repeating: Array(repeating: false, count: N), count: N)
//
//var queue = [[Int]]()
//let dx = [0, -1, 0, 1]
//let dy = [-1, 0, 1, 0]
//var count = 0
//var rgCount = 0
//
//// matrix에 입력받기
//for i in 0..<N {
//    let colors = readLine()!
//    matrix[i] = [Character](colors)
//}
//
//for i in 0..<N {
//    for j in 0..<N {
//        if !visited[i][j] {
//            queue.append([i, j])
//            visited[i][j] = true
//
//            while !queue.isEmpty {
//                let x = queue[0][0]
//                let y = queue[0][1]
//                let color = matrix[x][y]
//
//                queue.removeFirst()
//
//                for i in 0..<4 {
//                    let nx = x + dx[i]
//                    let ny = y + dy[i]
//
//                    if nx >= 0 && ny >= 0 && nx < N && ny < N && !visited[nx][ny] {
//                        if color == matrix[nx][ny] {
//                            queue.append([nx, ny])
//                            visited[nx][ny] = true
//                        }
//                    }
//                }
//            }
//            count += 1
//        }
//    }
//}
//
//for i in 0..<N {
//    for j in 0..<N {
//        if !rgVisited[i][j] {
//            queue.append([i, j])
//            rgVisited[i][j] = true
//
//            while !queue.isEmpty {
//                let x = queue[0][0]
//                let y = queue[0][1]
//                let color = matrix[x][y]
//
//                queue.removeFirst()
//
//                for i in 0..<4 {
//                    let nx = x + dx[i]
//                    let ny = y + dy[i]
//
//                    if nx >= 0 && ny >= 0 && nx < N && ny < N && !rgVisited[nx][ny] {
//                        if color == matrix[nx][ny] || (color == "R" && matrix[nx][ny] == "G") || (color == "G" && matrix[nx][ny] == "R")  {
//                            queue.append([nx, ny])
//                            rgVisited[nx][ny] = true
//                        }
//                    }
//                }
//            }
//            rgCount += 1
//        }
//    }
//}
//
//print(count, rgCount)


/*
 2. 적록색약을 쉽게 계산하기 위해 입력받은 컬러들에서 빨강을 초록으로 변경
 적록색약인 사람과 적록색약이 아닌 사람이 동일한 로직을 사용하게 됨
 */

let N = Int(readLine()!)!
var matrix: [[Character]] = Array(repeating: Array(repeating: "A", count: N), count: N)
var rgMatrix: [[Character]] = Array(repeating: Array(repeating: "A", count: N), count: N)
var visited = Array(repeating: Array(repeating: false, count: N), count: N)
var rgVisited = Array(repeating: Array(repeating: false, count: N), count: N)

var queue = [[Int]]()
let dx = [0, -1, 0, 1]
let dy = [-1, 0, 1, 0]

// matrix에 입력받기
for i in 0..<N {
    let colors = readLine()!
    matrix[i] = [Character](colors)
    rgMatrix[i] = [Character](colors).compactMap { $0 == "G" ? "R" : $0 }
}

func bfs(matrix: [[Character]], visited: inout [[Bool]]) -> Int {
    var count = 0

    for i in 0..<N {
        for j in 0..<N {
            if !visited[i][j] {
                queue.append([i, j])
                visited[i][j] = true

                while !queue.isEmpty {
                    let x = queue[0][0]
                    let y = queue[0][1]
                    let color = matrix[x][y]

                    queue.removeFirst()

                    for i in 0..<4 {
                        let nx = x + dx[i]
                        let ny = y + dy[i]

                        if nx >= 0 && ny >= 0 && nx < N && ny < N && !visited[nx][ny] {
                            if color == matrix[nx][ny] {
                                queue.append([nx, ny])
                                visited[nx][ny] = true
                            }
                        }
                    }
                }
                count  += 1
            }
        }
    }
    return count
}

print(bfs(matrix: matrix, visited: &visited), bfs(matrix: rgMatrix, visited: &rgVisited))
