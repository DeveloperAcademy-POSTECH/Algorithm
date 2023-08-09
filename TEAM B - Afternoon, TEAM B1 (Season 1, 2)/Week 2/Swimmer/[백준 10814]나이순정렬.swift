import Foundation

struct member{ // member구조체를 선언하고 name, age, order를 선언
    var name: String
    var age: Int
    var order: Int
}

let n = Int(readLine()!)! // member의 수 입력받기.

var memArr: [member] = [] //member 구조체들을 저장하기위한 memArr배열을 선언

for i in 0..<n {
    let a = readLine()!.split(separator: " ").map { s in
        String(s)
    }
    let mem = member(name: a[1], age: Int(a[0])!, order: i)
    memArr.append(mem) //memArr배열에 member구조체들을 추가
}

//memArr배열을 조건에 맞게 정렬
memArr.sort { a, b in
    a.age == b.age ? a.order < b.order : a.age < b.age
}

for j in 0..<n { //memArr에 저장된 각 배열의 원소의 나이와 이름을 출력
    print("\(memArr[j].age) \(memArr[j].name)")
}