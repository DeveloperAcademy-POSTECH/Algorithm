func convertToBinaryArray(from decimal: Int, maxDigit: Int) -> [String] {
    let binaryString = String(decimal, radix: 2)
    return [String](repeating: "0", count: maxDigit - binaryString.count) + binaryString.map(String.init)
}

func secretMap(_ n: Int, _ arr1: [Int], _ arr2: [Int]) -> [String] {
    var mergedMap: [[String]] = [[String]](repeating: [String](repeating: " ", count: n), count: n)
    
    for i in 0..<n {
        let binaryOne = convertToBinaryArray(from: arr1[i], maxDigit: n)
        let binaryTwo = convertToBinaryArray(from: arr2[i], maxDigit: n)
        
        for j in 0..<n {
            if binaryOne[j] == "1" || binaryTwo[j] == "1" {
                mergedMap[i][j] = "#"
            }
        }
    }
    
    return mergedMap.map { $0.joined() }
}

secretMap(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
secretMap(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])
