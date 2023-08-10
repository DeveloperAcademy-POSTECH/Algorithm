import Foundation

let T = Int(readLine()!)!

for _ in 0..<T {
	var result = 0
	let _ = Int(readLine()!)!
	var arr = readLine()!.split(separator: " ").map {Int(String($0))!}
	var maxChk = arr.last!
	
	for val in arr.reversed() {
		if val >= maxChk {
			maxChk = val
		} else {
			result += (maxChk - val)
		}
	}

	print(result)
}
