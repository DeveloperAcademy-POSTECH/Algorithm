/*
 리뷰
 - 1차 수정: 테스트케이스 반례를 직접 추가해서 정확도 25% -> 83%로 올림
 */
func gymSuit(_ n: Int, _ lost: [Int], _ reserve: [Int]) -> Int {
    // 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
    // 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며,
    // 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
    var realLost = lost.filter { !reserve.contains($0) }
    var realReserve = reserve.filter { !lost.contains($0) }
    let confirmedStudentCount = n - realLost.count

    var additionalStudent = 0.0

    for loser in realLost {
        let leftStudent = loser - 1
        let rightStudent = loser + 1
        
        var probability = 0.0
        
        // 전체 학생수 30명이므로 O(n) 사용
        if leftStudent > 0 && realReserve.contains(leftStudent) {
            probability += 0.5
        }
        
        if rightStudent <= n && realReserve.contains(rightStudent) {
            probability += 0.5
        }
        
        additionalStudent += probability
    }
    
    // 1차: Int() => Int(ceil())
    return confirmedStudentCount + Int(ceil(additionalStudent))
}

func gymSuit2(_ n: Int, _ lost: [Int], _ reserve: [Int]) -> Int {
    // 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
    // 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며,
    // 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
    var realLost = lost.filter { !reserve.contains($0) }
    var realReserve = reserve.filter { !lost.contains($0) }
    let confirmedStudentCount = n - realLost.count
    var borrowedList: Set<Int> = []
    
    for lender in realReserve {
        var leftStudent = lender - 1
        var rightStudent = lender + 1
        
        // 왼쪽에 옷 빌려주기
        if leftStudent > 0 && realLost.contains(leftStudent) {
            borrowedList.insert(leftStudent)
        } else if rightStudent <= n && realLost.contains(rightStudent) {
            borrowedList.insert(rightStudent)
        }
    }
    
    return confirmedStudentCount + borrowedList.count
}

gymSuit(5, [2, 4], [1, 3, 5]) // 5
gymSuit(5, [2, 4], [3]) // 4
gymSuit(3, [3], [1]) // 2

gymSuit(4, [3], [2, 4]) // 4
gymSuit(6, [2, 4, 6], [5]) // 4
gymSuit(5, [5], [2, 3]) // 4
gymSuit(5, [1], [4, 5]) // 4
gymSuit(2, [1], [2]) // 2 인데 1 나옴 -> 고침
gymSuit(2, [2], [1]) // 2

gymSuit(3, [1], [3]) // 2
gymSuit(3, [2], [3]) // 3
gymSuit(3, [1, 2], [3]) // 2
gymSuit(3, [1, 3], [2]) // 2
gymSuit(3, [2, 3], [1]) // 2

gymSuit(4, [2, 3, 4], [1]) // 2
gymSuit(4, [1, 4], [2, 3]) // 4 인데 3 나옴 -> 고침
gymSuit(4, [2, 3], [1, 4]) // 4 인데 3 나옴 -> 고침
gymSuit(4, [2, 4], [3]) // 3

gymSuit(5, [1, 3], [2, 5]) // 4
gymSuit(5, [2, 4], [1, 3, 4, 5]) // 5
gymSuit(5, [3, 4], [4, 3]) // 5
gymSuit(5, [4, 5], [3, 4]) // 4

