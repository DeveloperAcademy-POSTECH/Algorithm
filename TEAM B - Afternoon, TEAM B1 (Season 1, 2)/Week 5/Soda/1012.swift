//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/06/04.
//

// 백준 1012 유기농 배추 https://www.acmicpc.net/problem/1012
// 어떤 노드를 방문했는지 체크, 큐

let T: Int = Int(readLine()!)!
var answer = [Int]()

for _ in 0..<T {
    let nums: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
    let M = nums[0]
    let N = nums[1]
    var matrix = [[Int]](repeating: [Int](repeating: 0, count: N), count: M)
    var visited = [[Bool]](repeating: [Bool](repeating: false, count: N), count: M)

    for _ in 0..<nums[2] { // 배추의 위치를 받아 matrix에서 해당하는 인덱스를 1로 바꿔줌
        let location: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
        matrix[location[0]][location[1]] = 1
    }

    // 왼쪽부터 시계 방향
    let dx = [0, -1, 0, 1]
    let dy = [-1, 0, 1, 0]

    var queue = [[Int]]()
    var count = 0

    for i in 0..<M {
        for j in 0..<N {

            // 배추가 존재하고, 아직 방문하지 않았을 경우
            if matrix[i][j] == 1 && !visited[i][j] {
                queue.append([i, j])
                visited[i][j] = true

                while !queue.isEmpty {
                    // queue의 제일 앞 값을 뺀다
                    let x = queue[0][0]
                    let y = queue[0][1]

                    queue.removeFirst()

                    // 큐에서 꺼낸 값을 기준으로 좌, 상, 우, 하 탐색
                    for i in 0..<4 {
                        let nx = x + dx[i]
                        let ny = y + dy[i]

                        // 인접한 부분 탐색
                        // 인덱스가 x: 0~M-1, y: 0~N-1 사이에 위치하고, 배추가 존재하는데 방문하지 않았다면 큐에 넣기
                        if nx >= 0 && ny >= 0 && nx < M && ny < N && !visited[nx][ny] && matrix[nx][ny] == 1 {
                            queue.append([nx, ny])
                            visited[nx][ny] = true
                        }
                    }
                }
                count += 1
            }
        }
    }
    answer.append(count)
}

print(answer.map { String($0) }.joined(separator: "\n"))
