import Foundation

func personalityType(_ survey: [String], _ choices: [Int]) -> String {
    // 1. 타입 점수 저장용 사전 생성
    let typeStrings = "RCJATFMN"
    var typeScoresDict = typeStrings.reduce([String: Int]()) { dict, character in
        var dict = dict
        dict[String(character)] = 0
        return dict
    }
    
    // 2. survey, choices를 순회하며 맞는 타입에 점수 추가
    for i in 0..<survey.count {
        let types = survey[i].map(String.init)
        let disagreeType = types[0]
        let agreeType = types[1]
        
        switch choices[i] {
        case 1, 2, 3:
            typeScoresDict[disagreeType]! += 4 - choices[i]
        case 5, 6, 7:
            typeScoresDict[agreeType]! += choices[i] - 4
        default:
            break
        }
    }
    
    print(typeScoresDict)
    
    // 3. 결과 출력
    var result: String = ""
    for typePair in ["RT", "CF", "JM", "AN"] {
        let types = typePair.map(String.init)
        // 왼쪽이 크거나 동점(사전순)
        if typeScoresDict[types[0]]! >= typeScoresDict[types[1]]! {
            result += types[0]
        } else {
            result += types[1]
        }
    }
    
    return result
}

personalityType(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
personalityType(["TR", "RT", "TR"], [7, 1, 3])
