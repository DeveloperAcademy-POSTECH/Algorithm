import Foundation

let n = Int(readLine()!)!
let m = Int(readLine()!)!

var graph = Array(repeating: [Int](), count: n+1)

for _ in 0..<m {
	let nums = readLine()!.split(separator: " ").map {Int(String($0))!}
	let first = nums[0]
	let second = nums[1]
	graph[first].append(second)
	graph[second].append(first)
}

func DFS(start: Int) -> Int {
	var visited = [Int]()
	var stack = [start]
	
	var count = 0
	
//	print(graph)
	
	while !stack.isEmpty {
		let node = stack.popLast()!
		if !visited.contains(node) {
			visited.append(node)
			count += 1
			stack.append(contentsOf: graph[node])
		}
	}
	
	return count-1
}

print(DFS(start: 1))
