//
//  DFS_BFS.swift
//  AlgorithmTest-ReadLine
//
//  Created by 윤범태 on 2023/09/18.
//

import Foundation

/*
 그래프 예제 1
 
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
 
 5 5 3
 5 4
 5 2
 1 2
 3 4
 3 1
 
 [[], [2, 3], [1, 5], [1, 4], [3, 5], [2, 4]]
 
3 1 2 5 4
3 1 4 2 5
 */

func bfs(_ start: Int, _ graphs: [[Int]]) -> String {
    var queue: [Int] = [start]
    var visited: Set<Int> = []
    var result: String = ""
    
    while !queue.isEmpty {
        let dequeued = queue.removeFirst()
        if !visited.contains(dequeued) {
            visited.insert(dequeued)
            queue.append(contentsOf: graphs[dequeued])
            result += "\(dequeued) "
        }
    }
    
    return result
}

func dfs(_ start: Int, _ graphs: [[Int]]) -> String {
    var stack: [Int] = [start]
    var visited: Set<Int> = []
    var result: String = ""
    
    while !stack.isEmpty {
        let popped = stack.removeLast()
        if !visited.contains(popped) {
            stack.append(contentsOf: graphs[popped].reversed())
            visited.insert(popped)
            result += "\(popped) "
        }
    }
    
    return result
}

func dfs_recursive(_ start: Int, _ graphs: [[Int]]) -> String {
    var visited: Set<Int> = []
    var result: String = ""
    
    func dfs(_ node: Int) {
        if !visited.contains(node) {
            result += "\(node) "
            visited.insert(node)
            
            for neighbor in graphs[node] {
                dfs(neighbor)
            }
        }
    }
    
    dfs(start)
    return result
}

