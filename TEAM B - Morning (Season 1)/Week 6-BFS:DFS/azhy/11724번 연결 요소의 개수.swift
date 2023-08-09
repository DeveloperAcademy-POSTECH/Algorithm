import Foundation

let NM = readLine()!.split(separator: " ").map {Int(String($0))!}
let N = NM[0]
let M = NM[1]
var visited = [Int]()
var count = 0

var graph = Array(repeating: [Int](), count: N+1)

for _ in 0..<M {
	let inputs = readLine()!.split(separator: " ").map {Int(String($0))!}
	let u = inputs[0]
	let v = inputs[1]
	graph[u].append(v)
	graph[v].append(u)
}

for i in 1...N {
	if !visited.contains(i) {
		count += 1
		DFS(start: i)
	}
}
print(count)

func DFS(start: Int){
	
	var stack = [start]
	
	while !stack.isEmpty {
		let node = stack.removeLast()
		
		if !visited.contains(node) {
			visited.append(node)
			stack.append(contentsOf: graph[node])
		}
	}
}
