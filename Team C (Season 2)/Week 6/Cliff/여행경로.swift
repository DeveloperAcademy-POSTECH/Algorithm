/*
 여행경로
 https://school.programmers.co.kr/learn/courses/30/lessons/43164
 
 문제 설명
 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

 제한사항
 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
 주어진 공항 수는 3개 이상 10,000개 이하입니다.
 tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
 주어진 항공권은 모두 사용해야 합니다.
 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
 입출력 예
 tickets    return
 [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]    ["ICN", "JFK", "HND", "IAD"]
 [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]    ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
 입출력 예 설명
 예제 #1

 ["ICN", "JFK", "HND", "IAD"] 순으로 방문할 수 있습니다.

 예제 #2

 ["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"] 순으로 방문할 수도 있지만 ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 가 알파벳 순으로 앞섭니다.

 [리뷰]
 - 테스트 케이스는 다 맞고, 첫 채점 결과 50% 정답률 (테스트 1, 2 실패 - 테스트 3, 4 성공)
 - 2는 반례 찾아 성공했지만 1은 끝까지 실패
 - 결국 다른 블로그 보고 베낌
 */


func pathOfJourney실패(_ tickets: [[String]]) -> [String] {
    // var ticketsSet = Set<[String]>()
    // tickets.forEach { ticketRow in
    //     ticketsSet.insert(ticketRow)
    // }
    // ticketsSet
    
    var pathMap: [String: [String]] = [:]
    for ticketPath in tickets {
        pathMap[ticketPath[0], default: []].append(ticketPath[1])
        pathMap[ticketPath[0], default: []].sort()
        
        // pathMap[ticketPath[1], default: []].append(ticketPath[0])
        // pathMap[ticketPath[1], default: []].sort()
    }
    pathMap
    
    var ticketsFlatMap = tickets.flatMap { $0 }
    var totalCount = ticketsFlatMap.count
    
    var currentCount = 0
    
    func dfs_recursive(_ start: String, _ graphs: [String: [String]]) -> [String] {
        var result: [String] = []
        var graphs = graphs
        var lastNode: String = "oo"
        
        func dfs(_ node: String) {
            currentCount += 1
            
            if currentCount <= totalCount {
                result.append(node)
                // if graphs[node, default: []].isEmpty {
                //     print(lastNode, "isEmpty", currentCount, totalCount, pathMap.values.allSatisfy({$0.count == 0}))
                //     print(pathMap[lastNode], pathMap[node])
                //     return
                // }
                
                if !graphs[node, default: []].isEmpty {
                    lastNode = node
                    let firstNode = graphs[node, default: []].removeFirst()
                    dfs(firstNode)
                    graphs[node, default: []].insert(node, at: 0)
                }
            }
        }
        
        dfs(start)
        return result
    }
    
    return dfs_recursive("ICN", pathMap)
}

func pathOfJourney(_ tickets: [[String]]) -> [String] {
    var answer: [String] = []
    
    var paths: [String: Array<String>] = [:]
    var visited: [String: Array<Bool>] = [:]
    
    for ticket in tickets {
        paths[ticket[0], default: .init()].append(ticket[1])
        paths[ticket[0], default: .init()].sort()
        visited[ticket[0], default: .init()].append(false)
    }
    
    print(paths, visited)
    
    func dfs(_ start: String, _ count: Int, _ list: [String], _ ticketCount: Int) {
        if count == ticketCount {
            answer.append(contentsOf: list)
            return
        }
        
        if answer.count >= ticketCount {
            return
        }
        
        guard let pathsStart = paths[start] else {
            print("pathstart is nil")
            return
        }
        
        for location in 0..<pathsStart.count {
            let isVisited = visited[start]![location]
            
            if !isVisited {
                visited[start]![location] = true
                let nextTarget = paths[start]![location]
                dfs(nextTarget, count + 1, list + [nextTarget], ticketCount)
                visited[start]![location] = false
            }
        }
    }
    
    dfs("ICN", 0, ["ICN"], tickets.count)
    return answer
}

pathOfJourney( [
    ["ICN", "JFK"],
    ["HND", "IAD"],
    ["JFK", "HND"]
] ) //  ["ICN", "JFK", "HND", "IAD"]

pathOfJourney( [
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"]
] ) // ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

pathOfJourney(
    [
        ["ICN", "JFK"],
        ["ICN", "JFK"],
        ["HND", "IAD"],
        ["JFK", "HND"],
        ["IAD", "ICN"]
    ]
)

// 반례
pathOfJourney([
    ["ICN", "JFK"],
    ["ICN", "AAD"],
    ["JFK", "ICN"]
]) // ["ICN", "JFK", "ICN", "AAD"]

pathOfJourney([
    ["ICN", "BOO"],
    ["ICN", "COO"],
    ["COO", "DOO"],
    ["DOO", "COO"],
    ["BOO", "DOO"],
    ["DOO", "BOO"],
    ["BOO", "ICN"],
    ["COO", "BOO"]
])
// ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]
