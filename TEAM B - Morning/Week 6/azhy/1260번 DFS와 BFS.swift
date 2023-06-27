import Foundation

let nums = readLine()!.split(separator: " ").map {Int(String($0))!}
let n = nums[0]
let m = nums[1]
let v = nums[2]

var graph = Array(repeating: [Int](), count: n+1)

for _ in 0..<m {
	let rl = readLine()!.split(separator: " ").map {Int(String($0))!}
	let src = rl[0]
	let dest = rl[1]
	graph[src].append(dest)
	graph[dest].append(src)
}

func DFS(start: Int) {
	var visited = [Int]()
	var stack = [start]
	
	while !stack.isEmpty {
		let node = stack.popLast()!
		
		if !visited.contains(node) {
			visited.append(node)
			print(node, terminator: " ")
			stack.append(contentsOf: graph[node].sorted(by: >))
		}
	}
}

func BFS(start: Int) {
	var visited = [Int]()
	var queue = [start]
	
	while !queue.isEmpty {
		let node = queue.removeFirst()
		
		if !visited.contains(node) {
			visited.append(node)
			print(node, terminator: " ")
			queue.append(contentsOf: graph[node].sorted(by: <))
		}
	}
}

DFS(start: v)
print()
BFS(start: v)

