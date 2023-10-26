import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var maxNum = 0
    var minNum = 0
    
    for size in sizes {
        maxNum = max(maxNum, size.max()!)
        minNum = max(minNum, size.min()!)
    }
    return maxNum * minNum
}