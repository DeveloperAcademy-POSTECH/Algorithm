//
//  1277.swift
//  AlgorithmTest-ReadLine
//
//  Created by 윤범태 on 2023/12/18.
//

import Foundation

/*
 풀이: https://sphong0417.tistory.com/47
 - 좌표 저장
 - 연결 여부 저장
 - distances: 1번부터 각 정점(vertex)까지의 거리, 초기화 시 연결되었다면 0, 아니면 infinity
 
 다익스트라 알고리즘
 - 가중치 더하는 부분: 각 좌표간의 거리(=> 두 점 사이간의 거리)
 - 모든 발전소의 거리를 계속해서 갱신할 필요: 1 ~ N 까지 자기 자신을 제외하고 거리 갱신
 
 반례
 1 => (0,0)
 2 => (-1, -1)
 3 => (1,1)

 - 1~3이 최단거리 (1을 먼저 방문체크하고 다음 발전소부터 확인하게 되면 최단비용은 2-3을 잇는 선분의 길이가 되므로 부적합)
 - 1번 발전소에 대해 방문체크를 따로 하지 않음 (for j in 1..<N + 1 {...})
    => 1번부터 다른 발전소까지의 직접 잇는 거리가 고려될 수 있도록
 
 
 */

struct PlantPoint {
    var x, y: Int
}

func Q_1277() {
    let NW = readLine()!.split(separator: " ").map { Int(String($0))! }
    let (N, W) = (NW[0], NW[1])
    
    let _ = Double(readLine()!)!
    
    var plants: [PlantPoint] = []
    var connected: [[Bool]] = .init(repeating: .init(repeating: false, count: N + 1), count: N + 1)
    
    plants.append(.init(x: 0, y: 0))
    for _ in 1..<N + 1 {
        let xy = readLine()!.split(separator: " ").map { Int(String($0))! }
        let (x, y) = (xy[0], xy[1])
        
        plants.append(PlantPoint(x: x, y: y))
    }
    
    for _ in 0..<W {
        let ab = readLine()!.split(separator: " ").map { Int(String($0))! }
        let (a, b) = (ab[0], ab[1])
        
        connected[a][b] = true
        connected[b][a] = true
    }
    
    func getDistance(_ current: Int, _ next: Int) -> Double {
        if connected[current][next] {
            return 0.0
        }
        
        let src = plants[current]
        let dest = plants[next]
        // 유클리드 거리
        let dist = Double(truncating: (pow(Decimal(src.x - dest.x), 2) + pow(Decimal(src.y - dest.y), 2)) as NSNumber)
        
        return sqrt(dist)
    }
    
    func dijkstra() {
        var distances: [Double] = .init(repeating: .infinity, count: N + 1)
        distances[1] = 0
        
        for i in 2..<N + 1 {
            if connected[1][i] {
                distances[i] = 0
            }
        }
        
        var visited: Set<Int> = []
        for _ in 0..<N {
            var minDist: Double = .infinity
            var current = 0
            
            for j in 1..<N + 1 {
                if !visited.contains(j) && minDist >= distances[j] {
                    minDist = distances[j]
                    current = j
                }
            }
            
            if current == N {
                break
            }
            visited.insert(current)
            
            for j in 1..<N + 1 {
                if j == current {
                    continue
                }
                
                let next = j
                if distances[next] > distances[current] + getDistance(current, next) {
                    distances[next] = distances[current] + getDistance(current, next)
                }
            }
        }
     
        print(Int(distances[N] * 1000))
    }
    
    dijkstra()
}

/*
 발전소 설치
 https://www.acmicpc.net/problem/1277
 
 문제
 엄청난 벼락을 맞아 많은 전선들이 끊어져 현재 전력 공급이 중단된 상태이다. 가장 심각한 문제는 1번 발전소에서 N번 발전소로 가는 중간의 전선이 끊어진 것이기에 일단 이 두 발전소를 다시 연결하는게 현재 해결해야할 첫 번째 과제이다.

 발전소는 1번부터 N번까지 번호로 매겨져 2차원 격자 좌표 위에 있다. 그리고 몇몇 전선은 보존된 채 몇몇 발전소를 잇고 있다. 문제는 현재 전선과 발전소의 위치가 주어졌을 때 최소의 전선 길이를 추가로 사용하여 1번 발전소와 N번 발전소를 연결짓는 것이다. 물론 연결 짓는 중간에 다른 발전소를 거쳐갈 수 있다. 단, 안정성 문제로 어떠한 두 발전소 사이의 전선의 길이가 M을 초과할 수는 없다. 아래에 이에 대한 예를 그려놓았다.

          연결 전                          연결 후

 3  . . . 7 9 . . . . .          3  . . . 7 9 . . . . .
                                           /
 2  . . 5 6 . . . . . .          2  . . 5 6 . . . . . .
                                         /
 1  2-3-4 . 8 . . . . .          1  2-3-4 . 8 . . . . .
    |                               |
 0  1 . . . . . . . . .          0  1 . . . . . . . . .

    0 1 2 3 4 5 6 7 8 9             0 1 2 3 4 5 6 7 8 9
 
 입력
 첫 줄에는 발전소의 수 N(1 ≤ N ≤ 1,000)과 현재 남아있는 전선의 수 W(1≤ W ≤ 10,000)가 주어진다. 두 번째 줄에는 제한 길이 M(0.0 < M < 200,000.0)가 주어진다. 다음 N개의 줄에는 1번 발전소부터 N번 발전소까지 각각의 발전소의 X좌표와 Y좌표(-100,000 ≤ xi,yi  ≤ 100,000)가 차례대로 주어진다. 다음 W개의 줄에 대해 각 줄에는 두 개의 정수가 입력되어지는데 이는 현재 남아있는 전선이 잇고 있는 두 발전소를 의미한다.

 출력
 첫 줄에 1번 발전소와 N번 발전소를 잇는데 필요한 추가 전선 길이의 최솟값을 1000배하여 출력한다. (단, 1000배하고 난 후 나머지 소수는 반올림이 아닌 버림을 한다)

 예제 입력 1
9 3
2.0
0 0
0 1
1 1
2 1
2 2
3 2
3 3
4 1
4 3
1 2
2 3
3 4
 
 예제 출력 1
 2828
 */
