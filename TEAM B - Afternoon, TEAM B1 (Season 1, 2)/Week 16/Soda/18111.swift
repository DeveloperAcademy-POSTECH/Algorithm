//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/09/04.
//
// 백준 18111 마인크래프트 https://www.acmicpc.net/problem/18111

/*
떠오르는 풀이가 없어서 일단 그냥 풀었다.
계속 틀려서 알고리즘 풀이를 봤더니 브루트포스였슴.

+ 계속 틀렸던 이유?
답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오. 조건을 고려하지 않았음ㅁ
1 3 68
0 0 1
반례를 통해 알게 됐다
*/

let line = readLine()!.split(separator: " ").map { Int($0)! }
let (N, M, B) = (line[0], line[1], line[2])

var matrix = [[Int]]()

var minHeight = 256
var maxHeight = 0

for _ in 0..<N {
    matrix.append(readLine()!.split(separator: " ").map { Int($0)! })
}

// 2차원 배열이지만, 1차원 배열로 풀이를 해도 지장은 없다
let flatMatrix = matrix.flatMap { $0 }

// 해당 집터의 땅 높이의 최소, 최대 구하기
for i in 0..<N {
    let minTmp = matrix[i].min()!
    let maxTmp = matrix[i].max()!
    minHeight = min(minHeight, minTmp)
    maxHeight = max(maxHeight, maxTmp)
}

var answer = [[Int]]()

// 최소 ~ 최대 사이값들을 돌며 전부 탐색해 보기? !
for height in minHeight...maxHeight {
    var blocks = B
    var time = 0

    // 1차원 배열을 순회
    for i in 0..<flatMatrix.count {
        if flatMatrix[i] > height { // 기준보다 높을 때
            blocks += (flatMatrix[i] - height) // 블럭을 기준보다 높은 크기만큼 더해줌
            time += 2 * (flatMatrix[i] - height) // 해당 방법의 시간은 2초. 더해 준다
        } else if flatMatrix[i] < height { // 기준보다 낮을 때
            blocks -= (height - flatMatrix[i]) // 블럭을 기준보다 낮은 크기만큼 빼준다 (인벤토리에 있는 블럭으로부터 가져오기 때문)
            time += (height - flatMatrix[i]) // 해당 방법의 시간은 1초이다.
        } else { // 같을 때는 처리를 하지 않는다
            continue
        }
    }

    if blocks < 0 { // 블럭은 음수일 수 없으므로, 이때의 기준 순회는 continue로 넘긴다
        continue
    }

    answer.append([time, height]) // [시간, 기준]을 append
}

// answer 배열을 정렬한다. 시간은 최소가 되도록 하되, 시간이 최소인 경우가 여러 개라면 땅의 높이가 가장 높아야 한다.
answer = answer.sorted {
    if $0[0] == $1[0] {
        return $0[1] > $1[1]
    } else {
        return $0[0] < $1[0]
    }
}

print(answer[0].map { String($0) }.joined(separator: " "))
