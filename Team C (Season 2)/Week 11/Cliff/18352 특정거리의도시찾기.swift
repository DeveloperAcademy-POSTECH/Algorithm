//
//  18352.swift
//  AlgorithmTest-ReadLine
//
//  Created by 윤범태 on 2023/12/18.
//

import Foundation

// 출처: https://beenii.tistory.com/143 [끄적이는 개발노트:티스토리]
class PriorityQueue_<T> {
    private var heap: [T] = []
    private let comparing: (_ o1: T,_ o2: T) -> Bool
    
    init(_ comparing: @escaping (_ o1: T,_ o2: T) -> Bool) {
        self.comparing = comparing
    }
    
    func size() -> Int { heap.count }
    
    func isEmpty() -> Bool { heap.isEmpty }
    
    func clear() { heap.removeAll() }
    
    func peek() -> T? { heap.first }
    
    func push(_ value: T) {
        heap.append(value)
        if heap.count == 1 { return }
        var valueIndex = heap.count - 1
        var parentIndex = (valueIndex-1) / 2
        while !comparing(heap[parentIndex], heap[valueIndex]) {
            heap.swapAt(valueIndex, parentIndex)
            valueIndex = parentIndex
            parentIndex = (valueIndex-1) / 2
            if valueIndex == 0 { break }
        }
    }
    
    func pop() -> T? {
        if heap.count == 0 { return nil }
        if heap.count == 1 { return heap.removeFirst() }
        
        func isChildEmpty(_ value: Int,_ left: Int,_ right: Int) -> Bool {
            if heap.count <= left { return true }
            if heap.count > right { return false }
            if comparing(heap[value], heap[left]) { return true }
            heap.swapAt(value, left)
            return true
        }
        
        heap.swapAt(0, heap.count-1)
        let answer = heap.removeLast()
        
        var valueIndex = 0
        var leftIndex = valueIndex * 2 + 1
        var rightIndex = valueIndex * 2 + 2
        
        if isChildEmpty(valueIndex, leftIndex, rightIndex) { return answer }
        
        while !comparing(heap[valueIndex], heap[leftIndex]) || !comparing(heap[valueIndex], heap[rightIndex]) {
            let index = comparing(heap[leftIndex], heap[rightIndex]) ? leftIndex : rightIndex
            heap.swapAt(valueIndex, index)
            valueIndex = index
            leftIndex = valueIndex * 2 + 1
            rightIndex = valueIndex * 2 + 2
            
            if isChildEmpty(valueIndex, leftIndex, rightIndex) { break }
        }
        return answer
    }
}

func Q_18352다익스트라시간초과() {
    let input1: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    let (N, M, K, X) = (input1[0], input1[1], input1[2], input1[3])
    
    var graph: [[(Int, Int)]] = .init(repeating: [], count: N + 1)
    var distance: [Int] = .init(repeating: .max, count: N + 1)
    
    // 그래프 만들기
    for _ in 0..<M {
        let input2:  [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
        let (a, b) = (input2[0], input2[1])
        graph[a].append((b, 1))
    }
    
    func dijkstra(_ start: Int) {
        let prQ = PriorityQueue_<(Int, Int)> { $0 > $1 }
        prQ.push((0, start))
        distance[start] = 0
        
        while !prQ.isEmpty() {
            let (dist, now) = prQ.pop()!
            
            if distance[now] < dist {
                continue
            }
            
            for pair in graph[now] {
                let cost = dist + pair.1
                if cost < distance[pair.0] {
                    distance[pair.0] = cost
                    prQ.push((cost, pair.0))
                }
            }
        }
    }
    
    dijkstra(X)
    var answer: [Int] = []
    
    for i in 1...N {
        if distance[i] == K {
            answer.append(i)
        }
    }
    
    if answer.isEmpty {
        print(-1)
    } else {
        answer.forEach { print($0, terminator: "\n") }
    }
}

func Q_18352_BFS시간초과() {
    let input1: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    let (N, M, K, X) = (input1[0], input1[1], input1[2], input1[3])
    
    var graph: [[Int]] = .init(repeating: [], count: N + 1)
    var distance: [Int] = .init(repeating: .max, count: N + 1)
    // var visited: [Bool] = .init(repeating: false, count: N + 1)
    var visited: Set<Int> = []
    
    // 그래프 만들기
    for _ in 0..<M {
        let input2:  [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
        let (a, b) = (input2[0], input2[1])
        graph[a].append(b)
    }
    
    func bfs(_ start: Int) {
        var answer: [Int] = []
        var q = [start]
        visited.insert(start)
        distance[start] = 0
        
        while !q.isEmpty {
            let now = q.removeFirst()
            for i in graph[now] {
                if !visited.contains(i) {
                    visited.insert(i)
                    q.append(i)
                    distance[i] = distance[now] + 1
                    if distance[i] == K {
                        answer.append(i)
                    }
                }
            }
        }
        
        if answer.isEmpty {
            print(-1)
        } else {
            answer.sorted().forEach { print($0) }
        }
    }
    
    bfs(X)
}

func Q_18352() {
    // ChatGPT가 풀어준거
    struct Queue<T> {
        private class Node {
            var value: T
            var next: Node?

            init(_ value: T) {
                self.value = value
            }
        }

        private var head: Node?
        private var tail: Node?

        mutating func enqueue(_ element: T) {
            let newNode = Node(element)
            if head == nil {
                head = newNode
                tail = newNode
            } else {
                tail?.next = newNode
                tail = newNode
            }
        }

        mutating func dequeue() -> T? {
            let value = head?.value
            head = head?.next
            if head == nil {
                tail = nil
            }
            return value
        }

        var isEmpty: Bool {
            return head == nil
        }
    }

    func findCitiesWithDistanceK(_ N: Int, _ M: Int, _ K: Int, _ X: Int, roads: [(Int, Int)]) {
        var graph: [[Int]] = .init(repeating: [], count: N + 1)
        var distance: [Int] = .init(repeating: -1, count: N + 1)
        var visited: [Bool] = .init(repeating: false, count: N + 1)

        for road in roads {
            let (a, b) = road
            graph[a].append(b)
        }

        var q = Queue<Int>()
        q.enqueue(X)
        visited[X] = true
        distance[X] = 0

        while !q.isEmpty {
            let now = q.dequeue()!

            for next in graph[now] {
                if !visited[next] {
                    visited[next] = true
                    q.enqueue(next)
                    distance[next] = distance[now] + 1
                }
            }
        }

        var answer: [Int] = []
        for city in 1...N {
            if distance[city] == K {
                answer.append(city)
            }
        }

        if answer.isEmpty {
            print(-1)
        } else {
            answer.forEach { print($0) }
        }
    }

    let input: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
    let (N, M, K, X) = (input[0], input[1], input[2], input[3])
    let roads: [(Int, Int)] = (0..<M).map { _ in
        let input: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
        return (input[0], input[1])
    }
    
    findCitiesWithDistanceK(N, M, K, X, roads: roads)
}

/*
 특정 거리의 도시 찾기
 https://www.acmicpc.net/problem/18352
 
 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.

 이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

 예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.

 1 --> 2
 |   / |
 V  /  V
 3 <   4

 이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.  2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.

 입력
 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.

 출력
 X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.

 이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.

 예제 입력 1
4 4 2 1
1 2
1 3
2 3
2 4
 예제 출력 1
 4
 
 예제 입력 2
4 3 2 1
1 2
1 3
1 4
 예제 출력 2
 -1
 
 예제 입력 3
4 4 1 1
1 2
1 3
2 3
2 4
 예제 출력 3
 2
 3
 */
