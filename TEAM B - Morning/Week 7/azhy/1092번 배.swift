import Foundation

let count = Int(readLine()!)!
var crain = readLine()!.split(separator: " ").map{ Int($0)! }
let boxCount = Int(readLine()!)!
var box = readLine()!.split(separator: " ").map{ Int($0)! }
var time = 0

crain.sort{ $0 > $1}
box.sort{ $0 > $1}

while !crain.isEmpty && crain[crain.endIndex - 1] < box[box.endIndex - 1] {
	crain.removeLast()
}

if crain.count == 0 || crain[0] < box[0] {
	print(-1)
} else {
	while !box.isEmpty {
		for i in 0..<crain.count {
			var idx = 0
			while idx < box.count && crain[i] < box[idx] {
				idx += 1
			}
			if idx < box.count {
				box.remove(at: idx)
			}
		}
		time += 1
	}
	print(time)
}
