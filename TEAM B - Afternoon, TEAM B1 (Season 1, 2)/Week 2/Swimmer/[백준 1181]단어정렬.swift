import Foundation

let n = Int(readLine()!)! // 첫 줄에 주어진 숫자를 단어의 개수 n으로 입력 받는다. => Int로 타입캐스팅
var dict =  [String : Int]() // Key가 String, Value가 Int인 빈 dictionary 생성

for _ in 0..<n { // n개 줄에 걸쳐서 알파벳 소문자 단어를 입력받는다. 
    let word = readLine()! // String 타입으로 입력받기
    dict[word, default: 0] += 1 // dict 의 key 값을 word로 받고, value는 0 부터 시작해서 1 씩 증가.
}

// 단어(key)의 길이가 같을 경우 사전 순으로 오름차순 정렬
// 길이가 다를 경우 길이 순으로 정렬
var sortedDict = dict.sorted {
    $0.key.count == $1.key.count ? $0 < $1 : $0.key.count < $1.key.count
}

for i in 0..<sortedDict.count {
    print("\(sortedDict[i].key)")
}