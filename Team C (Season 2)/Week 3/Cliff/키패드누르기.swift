import Foundation

func distance(_ pos1: (Int, Int), _ pos2: (Int, Int)) -> Int {
    // 두 점 (x1, y1), (x2, y2)의 맨해튼 거리 = |x1 - x2| + | y1 - y2 |
    return abs(pos1.0 - pos2.0) + abs(pos1.1 - pos2.1)
}

distance((0, 1), (1, 1)) // 1
distance((2, 0), (1, 1)) // 2

func pressKeypad(_ numbers: [Int], _ hand: String) -> String {
    var isRightHand = hand == "right"
    var leftHandPosition: Int = 10
    var rightHandPosition: Int = 12
    var result: String = ""
    
    // zero-based
    var positions: [(Int, Int)] = [
        (1, 3),
        (0, 0), (1, 0), (2, 0),
        (0, 1), (1, 1), (2, 1),
        (0, 2), (1, 2), (2, 2),
        (0, 3), (1, 3), (2, 3),
    ]
    
    for number in numbers {
        switch number {
        case 1, 4, 7:
            result += "L"
            leftHandPosition = number
        case 3, 6, 9:
            result += "R"
            rightHandPosition = number
        default:
            // 맨해튼 거리
            var distanceFromLeft = distance(positions[leftHandPosition], positions[number])
            var distanceFromRight = distance(positions[rightHandPosition], positions[number])
            // print(number, leftHandPosition, rightHandPosition, positions[leftHandPosition], positions[rightHandPosition], positions[number], distanceFromLeft, distanceFromRight)
            
            if distanceFromLeft > distanceFromRight {
                result += "R"
                rightHandPosition = number
            }
            else if distanceFromLeft < distanceFromRight {
                result += "L"
                leftHandPosition = number
            }
            else {
                // 거리가 같은 경우
                result += isRightHand ? "R" : "L"
                if isRightHand {
                    rightHandPosition = number
                } else {
                    leftHandPosition = number
                }
            }
        }
    }
    
    return result
}

pressKeypad([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") // LRLLLRLLRRL
pressKeypad([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") // LRLLRRLLLRR
pressKeypad([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") // LLRLLRLLRL
