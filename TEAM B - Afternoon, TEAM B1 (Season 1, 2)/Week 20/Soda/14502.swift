//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/10/01.
//
// 백준 14502 연구소 https://www.acmicpc.net/problem/14502

/*
벽 3개를 세우는 모든 경우를 구해도 시간 초과가 나지 않는다.
bfs로 인접한 상하좌우를 탐색하여 바이러스를 퍼뜨린다.
*/

// 입력받기
let nums = readLine()!.split(separator: " ").map { Int($0)! }
let (N, M) = (nums[0], nums[1]) // 세로 N, 가로 M
var matrix = Array(repeating: [Int](), count: N)
var answer = 0

for i in 0..<N {
    matrix[i].append(contentsOf: readLine()!.split(separator: " ").map { Int($0)! })
}

// 벽 3개를 만들 수 있는 모든 경우를 구하고
func createWall(_ count: Int) {
    if count == 3 { // 벽 3개가 모두 세워지면 바이러스 퍼뜨리는 함수 실행
        bfs()
        return
    }

    for i in 0..<N {
        for j in 0..<M {
            if matrix[i][j] == 0 { // 빈칸이면 벽을 만들 수 있음
                matrix[i][j] = 1
                createWall(count+1)
                matrix[i][j] = 0 // 밖으로 나왔을 때는 다시 0으로 만들어 주기
            }
        }
    }
}

// 상하좌우 탐색을 위한 dx, dy 배열
let dx = [-1, 0, 1, 0]
let dy = [0, 1, 0, -1]

// bfs로 인접한 곳을 탐색하며 세균을 퍼뜨리고, 만들 수 있는 최대 안전 영역 체크
func bfs() {
    var queue = [[Int]]()
    var tmpMatrix = matrix

    for i in 0..<N {
        for j in 0..<M {
            if tmpMatrix[i][j] == 2 { // 바이러스의 좌표 저장
                queue.append([i, j])
            }
        }
    }

    while !queue.isEmpty {
        let x = queue[0][0]
        let y = queue[0][1]

        queue.removeFirst()

        for i in 0..<4 {
            let nx = x + dx[i]
            let ny = y + dy[i]

            // 범위에 맞다면 바이러스 퍼뜨리기
            if 0..<N ~= nx && 0..<M ~= ny && tmpMatrix[nx][ny] == 0 {
                tmpMatrix[nx][ny] = 2
                queue.append([nx, ny])
            }
        }
    }

    // 안전 영역의 개수를 카운트해 주고, 항상 최대로 갱신
//    let zeroCount = tmpMatrix.flatMap { $0 }.filter { $0 == 0}.count
    var count = 0
    for i in 0..<N {
        for j in 0..<M {
            if tmpMatrix[i][j] == 0 {
                count += 1
            }
        }
    }
    answer = max(answer, count)
}

createWall(0)
print(answer)
