//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/10/09.
//
// 백준 2615 오목 https://www.acmicpc.net/problem/2615

// 1. 오답 풀이
//var matrix = Array(repeating: Array(repeating: 0, count: 19), count: 19)
//
//// 입력받기
//for i in 0..<19 {
//    matrix[i] = readLine()!.split(separator: " ").map { Int($0)! }
//}
//
//// 가로줄 탐색
//func searchRow(x: Int, y: Int, color: Int) -> Bool {
//    for i in 0..<5 {
//        if !(0..<19 ~= (y + i)) || color != matrix[x][y+i] {
//            return false
//        }
//    }
//
//    // 연속 조건을 만족할 때
//    if (x == 0) && (y == 0) {
//        if (matrix[x][y+5]) == color {
//            return false
//        }
//    } else if (y == 0) {
//        if (matrix[x][y+5]) == color {
//            return false
//        }
//    } else {
//        if (y + 5) < 19 { // 마지막 다음 바둑알이 범위 안에 있으면 색깔이 같은지 체크
//            if (matrix[x][y+5]) == color || (matrix[x][y-1]) == color {
//                return false
//            }
//        }
//    }
//
//    return true
//}
//
//// 세로줄 탐색
//func searchColumn(x: Int, y: Int, color: Int) -> Bool {
//    for i in 0..<5 {
//        if !(0..<19 ~= (x + i)) || color != matrix[x+i][y] {
//            return false
//        }
//    }
//
//    // 연속 조건을 만족할 때
//    if (y == 0) && (x == 0) {
//        if (matrix[x+5][y]) == color {
//            return false
//        }
//    } else if (x == 0) {
//        if (matrix[x+5][y]) == color {
//            return false
//        }
//    } else {
//        if (x + 5) < 19 { // 마지막 다음 바둑알이 범위 안에 있으면 색깔이 같은지 체크
//            if (matrix[x+5][y]) == color || (matrix[x-1][y]) == color {
//                print(x, y, matrix[x+5][y], matrix[x-1][y], color)
//                return false
//            }
//        }
//    }
//    return true
//}
//
//// 대각선 탐색
//func searchDiagonal(x: Int, y: Int, color: Int) -> Bool {
//    for i in 0..<5 {
//        if !(0..<19 ~= (x + i)) || !(0..<19 ~= (y + i)) || color != matrix[x+i][y+i] {
//            return false
//        }
//    }
//
//    // 연속 조건을 만족할 때
//    if (x == 0) || (y == 0) { // 첫 번재 바둑알이 0행 or 0열애 있을 경우
//        if (matrix[x+5][y+5]) == color {
//            return false
//        }
//    } else {
//        if (x + 5) < 19 && (y + 5) < 19 { // 마지막 다음 바둑알이 범위 안에 있으면 색깔이 같은지 체크
//            if (matrix[x+5][y+5]) == color || (matrix[x-1][y-1]) == color {
//                return false
//            }
//        }
//    }
//
//    // 마지막 다음 바둑알이 없거나, 색깔이 다르다면 true 반환
//    return true
//}
//
//var answer = [[Int]]()
//
//for i in 0..<19 {
//    for j in 0..<19 {
//        let color = matrix[i][j]
//
//        if color != 0 { // 바둑알이 놓여 있을 경우 검색하기
//            let rowResult = searchRow(x: i, y: j, color: color)
//            let colResult = searchColumn(x: i, y: j, color: color)
//            let diagonalResult = searchDiagonal(x: i, y: j, color: color)
//
//            if rowResult || colResult || diagonalResult {
//                print(rowResult, colResult, diagonalResult)
//                answer.append([color, i+1, j+1])
//            }
//        }
//    }
//}
//
//print(answer)
//
//// 가장 왼쪽에 있으려면 열이 가장 작아야 함, 열이 같다면 행이 가장 작아야 함
//if answer.isEmpty {
//    print("0")
//} else {
//    answer.sort { $0[2] < $1[2] }
//        print(answer[0][0])
//        print(answer[0][1], answer[0][2])
//}

// 2. 정답 풀이
var matrix = Array(repeating: Array(repeating: 0, count: 19), count: 19)

// 입력받기
for i in 0..<19 {
    matrix[i] = readLine()!.split(separator: " ").map { Int($0)! }
}

// 연속된 바둑알 중 가장 왼쪽에 있는 바둑알의 좌표를 찾아야 하므로 4방향만 진행 → ↓ ↘ ↗
var dx = [0, 1, 1, -1]
var dy = [1, 0, 1, 1]
var answer = [[Int]]()

// 모든 바둑알 순회
for i in 0..<19 {
    for j in 0..<19 {
        if matrix[i][j] != 0 { // 바둑알이 놓여 있을 경우 검색하기
            let color = matrix[i][j]

            for k in 0..<4 { // → ↓ ↘ ↗ 방향 탐색
                var nx = i + dx[k]
                var ny = j + dy[k]

                var cnt = 1 // 자신 카운트

                while 0..<19 ~= nx && 0..<19 ~= ny && matrix[nx][ny] == color {
                    cnt += 1

                    // 바둑알이 5개 연속이 됐다면
                    if cnt == 5 {
                        // 첫 바둑알 이전 바둑알의 색이 같은지 체크
                        if 0..<19 ~= (i - dx[k]) && 0..<19 ~= (j - dy[k]) && matrix[i-dx[k]][j-dy[k]] == color {
                            break
                        }
                         // 마지막 바둑알 이후 바둑알의 색이 같은지 체크
                        if 0..<19 ~= (nx + dx[k]) && 0..<19 ~= (ny + dy[k]) && matrix[nx+dx[k]][ny+dy[k]] == color {
                            break
                        }

                        answer.append([color, i+1, j+1])
                    }

                    // 같은 방향으로 nx, ny를 갱신하여 연속적인지 검색
                    nx += dx[k]
                    ny += dy[k]
                }
            }
        }
    }
}


if answer.isEmpty {
    print("0")
} else {
    print(answer[0][0])
    print(answer[0][1], answer[0][2])
}
