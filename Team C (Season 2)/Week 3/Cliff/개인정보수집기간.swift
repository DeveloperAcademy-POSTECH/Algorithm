import Foundation

struct SimplifiedDate: Comparable {
    var year: Int
    var month: Int
    var day: Int
    
    /// 비교 연산자: 나중이 더 큰것이고, 같은 날짜도 true로 침
    static func < (lhs: SimplifiedDate, rhs: SimplifiedDate) -> Bool {
        if lhs.year < rhs.year {
            return true
        } else if lhs.year == rhs.year && lhs.month < rhs.month {
            return true
        } else if lhs.year == rhs.year && lhs.month == rhs.month {
            return lhs.day < rhs.day
        } else {
            return false
        }
    }
    
}

/// 기준 날짜로부터 몇 달이 지났을 때 언제인가?
func expiredDate(from baseDate: SimplifiedDate, expireMonth: Int) -> SimplifiedDate {
    let isDayMoveBeforeMonth = baseDate.day == 1
    // 1일이고, 1월이면 전년 12월 28일로 이동해야 함
    
    // 일
    let day: Int = isDayMoveBeforeMonth ? 28 : baseDate.day - 1
    
    // 월
    let addedMonth = baseDate.month + expireMonth
    let moddedMonth = addedMonth % 12 == 0 ? 12 : addedMonth % 12
    let finalMonth = moddedMonth == 1 && isDayMoveBeforeMonth ? 12 : (isDayMoveBeforeMonth ? moddedMonth - 1 : moddedMonth)
    print(moddedMonth, finalMonth)
    
    /// 결과가 12월 31일이므로 연도를 -1 조정할 필요가 있을 때 true
    let isNeedsubstractYear = (moddedMonth == 1 && isDayMoveBeforeMonth) || (addedMonth % 12 == 0)
    
    // 연
    let dividedAddYear = addedMonth / 12
    let finalYear = baseDate.year + (isNeedsubstractYear ? dividedAddYear - 1 : dividedAddYear)
    
    return SimplifiedDate(year: finalYear, month: finalMonth, day: day)
}

expiredDate(from: .init(year: 2019, month: 12, day: 17), expireMonth: 12) // 2020.12.16

func privacyPeriod(_ today: String, _ terms: [String], _ privacies: [String]) -> [Int] {

    /*
     주의: 이 세계관에서 한 달은 전부 28일이다.
     */

    // 1. 날짜 스트링을 연월일로 분리

    let splittedToday = today.split(separator: ".")
    let todayDate = SimplifiedDate(year: Int(splittedToday[0])!,
                                   month: Int(splittedToday[1])!,
                                   day: Int(splittedToday[2])!)

    // 2. 약관 종류별로 분류해서 사전 생성
    let termsDict: [String: Int] = terms.reduce([String: Int]()) { dict, value in
        let splitted = value.split(separator: " ")
        var dict = dict
        dict[String(splitted[0])] = Int(splitted[1])
        return dict
    }

    // print(termsDict)

    // 3. privacies 순회하면서 약관 종류가 뭔지 파악하고, 유효기간이 지났는지 여부 파악
    var result: [Int] = []
    privacies.enumerated().forEach { (index, value) in
        let splittedValue = value.split(separator: " ")
        let splittedCollectDay = splittedValue[0].split(separator: ".")
        let collectDate = SimplifiedDate(year: Int(splittedCollectDay[0])!,
                                        month: Int(splittedCollectDay[1])!,
                                        day: Int(splittedCollectDay[2])!)
        let category = splittedValue[1]
        // print(collectDate, category)

        // 2022.05.02로부터 A(6) 유효기간이 경과했다면 언제?
        // 2022.05.02에서 달을 6 더함
        let expireDate = expiredDate(from: collectDate, expireMonth: termsDict[String(category)]!)
        // print(todayDate, expireDate, todayDate > expireDate)
        if todayDate > expireDate {
            result.append(index + 1)
        }
    }


    return result
}

privacyPeriod("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
privacyPeriod("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
privacyPeriod("2020.12.17", ["A 12"], ["2010.01.01 A", "2019.12.17 A"]) // [1, 2]
