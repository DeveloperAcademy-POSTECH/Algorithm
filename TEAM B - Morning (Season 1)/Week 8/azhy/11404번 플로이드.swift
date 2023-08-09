import Foundation

let n = Int(readLine()!)!

var values = [[Int?]](repeating: [Int?](repeating: nil, count: n+1), count: n+1)

for i in 1...n {
	values[i][i] = 0
}

print(values)
print()

for _ in 0..<Int(readLine()!)! {
	let d = readLine()!.split(separator: " ").map {Int(String($0))!}
	values[d[0]][d[1]] = min(values[d[0]][d[1]] ?? Int.max, d[2])
}

print(values)
print()

for k in 1...n {
	for s in 1...n {
		for e in 1...n  {
			guard k != s else { continue }
			if let startToK = values[s][k], let kToEnd = values[k][e] {
				values[s][e] = min(values[s][e] ?? Int.max, startToK + kToEnd)
			}
		}
	}
}

values.dropFirst().map { $0.dropFirst() }.forEach {
	print($0.map {String($0 ?? 0)}.joined(separator: " "))
}
