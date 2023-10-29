import Foundation

func moigosa(_ answers: [Int]) -> [Int] {
    var scores = [0, 0, 0]
    var patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]
    
    for (index, answer) in answers.enumerated() {
        for (pIndex, pattern) in patterns.enumerated() {
            if pattern[index % pattern.count] == answer {
                scores[pIndex] += 1
            }
        }
    }
    
    let maxScore = scores.max()
    
    return scores.enumerated().compactMap { (index, score) in
        maxScore == score ? index + 1 : nil
    }
}

let supo1 = [1,2,3,4,5]
let supo2 = [1,3,2,4,2]

moigosa(supo1)
moigosa(supo2)