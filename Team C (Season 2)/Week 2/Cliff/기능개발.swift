import Foundation

func developFeature(_ progresses: [Int], _ speeds: [Int]) -> [Int] {
    if progresses.count <= 1 {
        return [progresses.count]
    }
    
    var remainDays: [Int] = []
    
    for i in 0..<progresses.count {
        let remainDay = Int(ceil(Double(100 - progresses[i]) / Double(speeds[i])))
        remainDays.append(remainDay)
    }
    
    var result: [Int] = []
    var distNum = 1
    var baseValue = 0
    
    for i in 0..<remainDays.count {
        if i == 0 {
            baseValue = remainDays[i]
            continue
        }
        
        if baseValue >= remainDays[i] {
            distNum += 1
            
            if i >= remainDays.count - 1 {
                result.append(distNum)
                // 더 이상 진행되지 않음
            }
        } else {
            result.append(distNum)
            
            if i < remainDays.count - 1 {
                distNum = 1
                baseValue = remainDays[i]
            } else {
                result.append(1)
            }
        }
    }
    
    return result
}

developFeature([93, 30, 55], [1, 30, 5])
developFeature([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
developFeature([96, 99, 98, 97], [1, 1, 1, 1]) // [4]
developFeature([0, 3, 0, 0, 10], [5, 96, 20, 50, 1]) // [4, 1]
developFeature([93], [1]) // [1]
developFeature([93, 30, 55, 30], [1, 30, 5, 30]) // [2, 2]