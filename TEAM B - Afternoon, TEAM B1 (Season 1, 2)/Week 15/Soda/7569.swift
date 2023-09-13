//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/09/03.
//

// 백준 7569 토마토 https://www.acmicpc.net/problem/7569

// 시간 초과

//let line = readLine()!.split(separator: " ").map { Int($0)! }
//let (M, N, H) = (line[0], line[1], line[2])
//var matrix = Array(repeating: Array(repeating: Array(repeating: 0, count: M), count: N), count: H)
//var queue = [[Int]]()
//
//let dx = [0, 1, 0, 0, 0, -1]
//let dy = [1, 0, 0, -1, 0, 0]
//let dz = [0, 0, 1, 0, -1, 0]
//
//func bfs() {
//    while !queue.isEmpty {
//        let first = queue[0]
//        let x = first[2]
//        let y = first[1]
//        let z = first[0]
//
//        queue.removeFirst()
//
//        for i in 0..<6 {
//            let nx = x + dx[i]
//            let ny = y + dy[i]
//            let nz = z + dz[i]
//
//            if nx >= 0 && ny >= 0 && nz >= 0 && nx < M && ny < N && nz < H && matrix[nz][ny][nx] == 0 {
//                queue.append([nz, ny, nx])
//                matrix[nz][ny][nx] = matrix[z][y][x] + 1
//            }
//        }
//    }
//}
//
//for h in 0..<H {
//    for n in 0..<N {
//        let line = readLine()!.split(separator: " ").map { Int($0)! }
//        matrix[h][n] = line
//    }
//}
//
//for h in 0..<H {
//    for n in 0..<N {
//        for m in 0..<M {
//            if matrix[h][n][m] == 1 {
//                queue.append([h, n, m])
//            }
//        }
//    }
//}
//
//bfs()
//
//let flatMatrix = matrix.flatMap { $0 }.flatMap { $0 }
//print(flatMatrix.contains(0) ? -1 : flatMatrix.max()! - 1) // 토마토가 모두 익지 못하는 상황일 때 -> matrix는 0을 포함한다


/*
 1. 풀이
 인접한 토마토를 익히는 것에서 bfs일 것이라고 생각했다.
 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향을 탐색해 주어야 하므로, dx, dy, dz 배열을 만들어 준다.
 익은 토마토의 위치를 한꺼번에 받는다. 1인 토마토들이 동시에 다른 토마토들을 익히기 때문이다.
 2. 시간 초과를 해결한 코드
 removeFirst()의 시간 복잡도가 O(N)이기 때문에 시간 초과가 발생함.
 따라서 index라는 변수를 새로 만들어 처리함
 */

let line = readLine()!.split(separator: " ").map { Int($0)! }
let (M, N, H) = (line[0], line[1], line[2])
var matrix = Array(repeating: Array(repeating: Array(repeating: 0, count: M), count: N), count: H)
var queue = [[Int]]()

let dx = [0, 1, 0, 0, 0, -1]
let dy = [1, 0, 0, -1, 0, 0]
let dz = [0, 0, 1, 0, -1, 0]

var index = 0

func bfs() { // bfs 함수
    while index < queue.count {
        let first = queue[index]
        let x = first[2]
        let y = first[1]
        let z = first[0]
        index += 1

        for i in 0..<6 { // 범위 내에 있는 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 인접한 토마토를 ㅔㅊ크한다
            let nx = x + dx[i]
            let ny = y + dy[i]
            let nz = z + dz[i]

            if 0..<M ~= nx && 0..<N ~= ny && 0..<H ~= nz && matrix[nz][ny][nx] == 0 {
                queue.append([nz, ny, nx])
                matrix[nz][ny][nx] = matrix[z][y][x] + 1
            }
        }
    }
}

// 입력받기
for h in 0..<H {
    for n in 0..<N {
        let line = readLine()!.split(separator: " ").map { Int($0)! }
        matrix[h][n] = line
    }
}

for h in 0..<H {
    for n in 0..<N {
        for m in 0..<M {
            if matrix[h][n][m] == 1 {
                // 실수했던 부분. 토마토가 익은 1의 위치를 한꺼번에 큐에 담아주고 시작해야 한다. 처음에는 for문으로 차례로 받았다
                queue.append([h, n, m])
            }
        }
    }
}

bfs()

let flatMatrix = matrix.flatMap { $0 }.flatMap { $0 }
print(flatMatrix.contains(0) ? -1 : flatMatrix.max()! - 1) // 토마토가 모두 익지 못하는 상황일 때 -> matrix는 0을 포함한다
