import Foundation

let dx = [0, 0, 1, -1]
let dy = [1, -1, 0, 0]

let t = Int(readLine()!)!

for _ in 0..<t {
	let input = readLine()!.split(separator: " ").map {Int(String($0))!}
	let M = input[0]
	let N = input[1]
	let K = input[2]
	
	var map = Array(repeating: Array(repeating: 0, count: N), count: M)
	
	for _ in 0..<K {
		let xy = readLine()!.split(separator: " ").map {Int(String($0))!}
		let x = xy[0]
		let y = xy[1]
		map[x][y] = 1
	}
	
	var answer = 0
	
	for i in 0..<M {
		for j in 0..<N {
			if map[i][j] == 1 {
				map[i][j] = 0
				answer += 1
				var stack = [(i, j)]
				
				while !stack.isEmpty {
					let node = stack.popLast()!
					
					for i in 0..<dx.count {
						let nextX = node.0 + dx[i]
						let nextY = node.1 + dy[i]
						
						if nextX < 0 || nextY < 0 || nextX >= M || nextY >= N {
							continue
						} else {
							if map[nextX][nextY] == 1{
								map[nextX][nextY] = 0
								stack.append((nextX, nextY))
							}
						}
					}
				}
			}
		}
	}
	print(answer)
}
