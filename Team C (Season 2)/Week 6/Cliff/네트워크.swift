/*
 문제 설명
 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

 제한사항
 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
 i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
 computer[i][i]는 항상 1입니다.
 입출력 예
 n    computers    return
 3    [[1, 1, 0], [1, 1, 0], [0, 0, 1]]    2
 3    [[1, 1, 0], [1, 1, 1], [0, 1, 1]]    1
 
 [리뷰]
 - 처음에는 백준 유기농벌레와 똑같은 유형인줄 알았으나 다름
 - 백준 바이러스 문제와 유사
 - 시간 오래 걸렸으나 자력으로 풀음
 */

/// https://school.programmers.co.kr/learn/courses/30/lessons/43162
func network(_ n: Int, _ computers: [[Int]]) -> Int {
    // 그래프 만들기
    var graphs: [[Int]] = Array(repeating: [], count: n + 1)
    for i in 0..<n {
        for j in 0..<n {
            if computers[i][j] == 1 {
                graphs[i + 1].append(j + 1)
                graphs[i + 1].sort(by: >)
            }
        }
    }
    
    var result = 0
    var visited: Set<Int> = []
    
    func dfs(_ node: Int) {
        if !visited.contains(node) {
            visited.insert(node)
            
            for neighbor in graphs[node] {
                dfs(neighbor)
            }
        }
    }
    
    // 방문한 적이 없는 경우 count를 1 올리고 dfs
    for start in 1...n {
        if !visited.contains(start) {
            result += 1
            dfs(start)
        }
    }
    
    return result
}

network(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) // 2
network(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) // 1

network(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]) // 3
network(2, [[1, 0], [0, 1]]) // 2
network(2, [[1, 1], [1, 1]]) // 1
network(1, [[1]]) // 1
network(4, [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0], [0, 0, 0, 1]]) // 4

network(4, [[1, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [1, 0, 0, 1]]) // 2
network(4, [[1, 0, 1, 1], [0, 1, 1, 0], [1, 1, 1, 0], [1, 0, 0, 1]]) // 1
