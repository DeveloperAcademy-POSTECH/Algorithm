//
//  1753.swift
//  AlgorithmTest-ReadLine
//
//  Created by 윤범태 on 2023/12/18.
//

import Foundation

/*
 PriorityQueue: GPT가 만들어줌
 문제풀이: https://dy-coding.tistory.com/entry/%EB%B0%B1%EC%A4%80-1753%EB%B2%88-%EC%B5%9C%EB%8B%A8%EA%B2%BD%EB%A1%9C-java
 */

struct HeapNode: Comparable {
    static func < (lhs: HeapNode, rhs: HeapNode) -> Bool {
        lhs.weight < rhs.weight
    }
    
    var weight: Int
    var number: Int
}

func Q_1753() {
    let VE: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    let (V, E) = (VE[0], VE[1])
    
    let K = Int(readLine()!)! - 1
    
    var dist: [Int] = .init(repeating: .max, count: V)
    var pq = PriorityQueue<HeapNode>()
    var graph: [[HeapNode]] = .init(repeating: [], count: V)
    
    for _ in 0..<E {
        let uvw = readLine()!.split(separator: " ").map { Int(String($0))! }
        let (u, v, w) = (uvw[0], uvw[1], uvw[2])
        graph[u - 1].append(HeapNode(weight: w, number: v - 1))
    }
    
    dijkstra(K)
    
    let result = dist.map {
        $0 == .max ? "INF" : "\($0)"
    }.joined(separator: "\n")
    
    print(result)
    
    func dijkstra(_ start: Int) {
        dist[start] = 0
        pq.enqueue(HeapNode(weight: 0, number: start))
        
        while !pq.isEmpty {
            let now = pq.dequeue()!
            
            for i in 0..<graph[now.number].count {
                let nextNode = graph[now.number][i]
                
                if dist[nextNode.number] > now.weight + nextNode.weight {
                    dist[nextNode.number] = now.weight + nextNode.weight
                    pq.enqueue(HeapNode(weight: dist[nextNode.number], number: nextNode.number))
                }
            }
        }
    }
}

/*
 최단경로
 https://www.acmicpc.net/problem/1753
 
 문제
 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.

 입력
 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

 출력
 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

 예제 입력 1
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
 
 예제 출력 1
 0
 2
 3
 7
 INF
 */
