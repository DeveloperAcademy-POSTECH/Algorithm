func receiveReport(_ id_list: [String], _ report: [String], _ k: Int) -> [Int] {
    var reporterDict: [String: [String]] = [:]
    var reporteeDict: [String: Int] = [:]
    
    for reportPair in report {
        let splitted = reportPair.split(separator: " ")
        let reporter = String(splitted[0])
        let reportee = String(splitted[1])
        
        // 신고 한 리스트: 한 유저가 같은 유저를 여러 번 신고한 경우는 신고 횟수 1회로 처리
        if reporterDict[reporter] == nil {
            reporterDict[reporter, default: []].append(reportee)
            reporteeDict[reportee, default: 0] += 1
        } else if let reportees = reporterDict[reporter], !reportees.contains(reportee) {
            reporterDict[reporter, default: []].append(reportee)
            reporteeDict[reportee, default: 0] += 1
        } // 신고 당한 리스트: 한 사람이 여러번 신고하였다면 카운트하지 않음
    }
    
    // 메일 전송 횟수
    var result: [Int] = [Int](repeating: 0, count: id_list.count)
    for (index, id) in id_list.enumerated() {
        guard let reportees = reporterDict[id] else {
            continue
        }
        
        for reportee in reportees {
            if reporteeDict[reportee]! >= k {
                result[index] += 1
            }
        }
    }
    
    return result
}

receiveReport(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
receiveReport(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
