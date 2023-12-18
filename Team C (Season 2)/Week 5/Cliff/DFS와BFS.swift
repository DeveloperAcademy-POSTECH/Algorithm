//
//  1260.swift
//  AlgorithmTest-ReadLine
//
//  Created by 윤범태 on 2023/09/17.
//

import Foundation

func Q_1260_old() {
    let input1: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    
    let N = input1[0]
    let M = input1[1]
    let V = input1[2]
    
    var graphs: [[Int]] = Array(repeating: [], count: N + 1)
    for _ in 0..<M {
        let input2: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
        let node1 = input2[0]
        let node2 = input2[1]
        
        graphs[node1].append(node2)
        graphs[node2].append(node1)
        graphs[node1].sort() // BFS-오름차순 / DFS-내림차순
        graphs[node2].sort() // BFS-오름차순 / DFS-내림차순
    }
    
    // // show graph dictionary
    // print(graphs)
    
    // DFS (Depth-First Search)
    var stack: [Int] = [V]
    var dfsVisited: Set<Int> = []
    var dfsResult: String = ""
    
    while !stack.isEmpty {
        let popped = stack.removeLast()
        if !dfsVisited.contains(popped) {
            stack.append(contentsOf: graphs[popped].reversed())
            dfsVisited.insert(popped)
            dfsResult += "\(popped) "
        }
    }
    
    print(dfsResult)
    
    // BFS (Breadth-First Search)
    var queue: [Int] = [V]
    var bfsVisited: Set<Int> = []
    var bfsResult: String = ""
    
    while !queue.isEmpty {
        let dequeued = queue.removeFirst()
        if !bfsVisited.contains(dequeued) {
            bfsVisited.insert(dequeued)
            queue.append(contentsOf: graphs[dequeued])
            bfsResult += "\(dequeued) "
        }
    }
    
    print(bfsResult)
}

func Q_1260() {
    let input1: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    
    let N = input1[0]
    let M = input1[1]
    let V = input1[2]
    
    var graphs: [[Int]] = Array(repeating: [], count: N + 1)
    for _ in 0..<M {
        let input2: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
        let node1 = input2[0]
        let node2 = input2[1]
        
        graphs[node1].append(node2)
        graphs[node2].append(node1)
        graphs[node1].sort() // DFS인 경우 내림차순
        graphs[node2].sort() // DFS인 경우 내림차순
    }
    // print(graphs)
    
    // DFS (Depth-First Search)
    print(dfs_recursive(V, graphs))
    
    // BFS (Breadth-First Search)
    print(bfs(V, graphs))
}

/*
 문제
 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

 입력
 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

 출력
 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
 
 예제 입력 1
 4 5 1
 1 2
 1 3
 1 4
 2 4
 3 4
 예제 출력 1
 1 2 4 3
 1 2 3 4
 
 
 예제 입력 2
 5 5 3
 5 4
 5 2
 1 2
 3 4
 3 1
 예제 출력 2
 3 1 2 5 4
 3 1 4 2 5
 
 
 예제 입력 3
 1000 1 1000
 999 1000
 예제 출력 3
 1000 999
 1000 999
 */

