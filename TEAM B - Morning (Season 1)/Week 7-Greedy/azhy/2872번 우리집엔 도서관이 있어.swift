import Foundation

let N = Int(readLine()!)!
var arr = [Int]()

for _ in 0..<N {
	arr.append(Int(readLine()!)!)
}

var temp = arr.max()
var count = 0

for val in arr.reversed() {
	if val == temp {
		temp! -= 1
	} else {
		count += 1
	}
	
}
print(count)
