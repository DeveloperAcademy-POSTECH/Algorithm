import Foundation

func dequeue(_ array: inout [Int]) -> Int? {
    guard !array.isEmpty else {
        return nil
    }

    let first = array[0]
    array = Array(array.dropFirst())

    return first
}

func process(_ priorities: [Int], _ location: Int) -> Int {
    var queue = priorities
    var location = location
    
    var answer = 0
    
    while !queue.isEmpty {
        let max = queue.max()!
        guard let first = dequeue(&queue) else {
            return 0
        }
        location -= 1
        
        if first != max {
            queue.append(first)
            if location < 0 {
                location = queue.count - 1 // 로케이션 리셋
            }
        } else {
            answer += 1
            if location < 0 {
                break
            }
        }
    }
    
    return answer
}

process([2, 1, 3, 2], 2)
process([1, 1, 9, 1, 1, 1], 0)