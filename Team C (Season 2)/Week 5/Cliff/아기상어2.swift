//
//  17086.swift
//  AlgorithmTest-ReadLine
//
//  Created by 윤범태 on 2023/09/23.
//

import Foundation

/*
 참고: 1012번 문제
 */

func Q_17086() {
    let input: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    let N = input[0] // m은 열
    let M = input[1] // n은 행,
    
    var oceans = [[Int]](repeating: [Int](repeating: 0, count: M), count: N)
    for n in 0..<N {
        oceans[n] = readLine()!.split(separator: " ").map { Int(String($0))! }
    }
    
    print(oceans)
    
    // 팔방향 탐색 (시계방향) => 해당 방향으로 나아감
    let dirX = [0, 1, 1, 1, 0, -1, -1, -1]
    let dirY = [-1, -1, 0, 1, 1, 1, 0, -1]
    
    var queue: [(x: Int, y: Int)] = []
    
    func bfs() {
        while !queue.isEmpty {
            let coord = queue.removeFirst()
            
            for i in 0..<dirX.count {
                let nextX = coord.x + dirX[i]
                let nextY = coord.y + dirY[i]
                
                if nextX < 0  || nextX >= M || nextY < 0 || nextY >= N {
                    continue
                }
                
                if oceans[nextY][nextX] == 0 {
                    // (nextX, nextY)에 현재거리에서 1을 더한다
                    oceans[nextY][nextX] = oceans[coord.y][coord.x] + 1
                    queue.append((nextX, nextY))
                }
            }
        }
    }
    
    for n in 0..<N {
        for m in 0..<M {
            if oceans[n][m] == 1 {
                queue.append((m, n))
            }
        }
    }
    
    bfs()
    // print(oceans)
    let result = oceans.flatMap { $0 }.max()! - 1
    print(result)
}

/*
 문제
 N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 아기 상어가 최대 1마리 존재한다.

 어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.

 안전 거리가 가장 큰 칸을 구해보자.

 입력
 첫째 줄에 공간의 크기 N과 M(2 ≤ N, M ≤ 50)이 주어진다. 둘째 줄부터 N개의 줄에 공간의 상태가 주어지며, 0은 빈 칸, 1은 아기 상어가 있는 칸이다. 빈 칸과 상어의 수가 각각 한 개 이상인 입력만 주어진다.

 출력
 첫째 줄에 안전 거리의 최댓값을 출력한다.

 예제 입력 1
 5 4
 0 0 1 0
 0 0 0 0
 1 0 0 0
 0 0 0 0
 0 0 0 1
 예제 출력 1
 2
 예제 입력 2
 7 4
 0 0 0 1
 0 1 0 0
 0 0 0 0
 0 0 0 1
 0 0 0 0
 0 1 0 0
 0 0 0 1
 예제 출력 2
 2
 */

