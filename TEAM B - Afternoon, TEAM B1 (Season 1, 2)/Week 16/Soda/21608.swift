//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/09/03.
//

// 백준 21608 상어 초등학교 https://www.acmicpc.net/problem/21608
// 인접한 칸 찾기면 이것도 bfs 쓸 수 있을 것 같다 ..? 까지는 생각이 되었는데, 끝까지 구현하지는 못했다.


struct Student { // 번호와 선호하는 학생 번호를 저장하기 위한 구조체
    var num: Int
    var prefers: [Int]
}

let N = Int(readLine()!)!
var classroom = Array(repeating: Array(repeating: 0, count: N), count: N)
var students = [Student]()

// 인접한 자리 탐색을 위한 dx, dy 배열
let dx = [-1, 0, 1, 0]
let dy = [0, 1, 0, -1]

for _ in 0..<N*N { // 입력 받기
    let line = readLine()!.split(separator: " ").map { Int($0)! }
    students.append(Student(num: line[0], prefers: Array(line[1...4])))
}

for student in students {
    var available = [(Int, Int, Int, Int)]() // 가능한 자리의 수

    for i in 0..<N {
        for j in 0..<N {
            if classroom[i][j] == 0 { // 빈자리라면

                var prefer = 0 // 좋아하는 학생 수를 체크할 변수
                var empty = 0 // 빈자리를 체크할 변수

                for k in 0..<4 { // 인접한 자리 체크
                    let nx = i + dx[k]
                    let ny = j + dy[k]

                    if nx >= 0 && ny >= 0 && nx < N && ny < N { // classroom 범위 안에 있을 때
                        if student.prefers.contains(classroom[nx][ny]) { // 인접한 자리에 선호하는 학생 숫자가 있다면
                            prefer += 1
                        }

                        if classroom[nx][ny] == 0 { // 인접한 자리가 빈자리라면
                            empty += 1
                        }
                    }
                }

                available.append((i, j, prefer, empty))
            }
        }
    }
    let sortedArray = available.sorted { // 우선 순위대로 sort해 준다. prefer, empty는 클수록, 행, 열은 작을수록 배열의 앞으로 감
        if $0.2 != $1.2 {
            return $0.2 > $1.2
        } else if $0.3 != $1.3 {
            return $0.3 > $1.3
        } else if $0.0 != $1.0 {
            return $0.0 < $1.0
        } else {
            return $0.1 < $1.1
        }
    }
    classroom[sortedArray[0].0][sortedArray[0].1] = student.num // 정렬해 준 배열의 첫번째 값들을 이용하여 실제 자리 배치를 한다.
}

// 만족도를 구하기 위해 students 배열을 sort해 준다. -> 인접한 자리를 탐색하기 쉽게 정렬해 준 것임
students.sort { $0.num < $1.num }
let scores = [0, 1, 10, 100, 1000]
var answer = 0

for i in 0..<N {
    for j in 0..<N {
        var prefers = 0

        for k in 0..<4 {
            let nx = i + dx[k]
            let ny = j + dy[k]

            if nx >= 0 && ny >= 0 && nx < N && ny < N { // 해당 자리에 있는 번호의 학생이 좋아하는 학생들 중에, 인접한 자리의 학생 숫자가 포함된다면, prefer + 1
                if students[classroom[i][j]-1].prefers.contains(classroom[nx][ny]) {
                    prefers += 1
                }
            }
        }
        answer += scores[prefers]
    }
}

print(answer)
