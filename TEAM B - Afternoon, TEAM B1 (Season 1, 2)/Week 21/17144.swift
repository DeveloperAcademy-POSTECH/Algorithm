//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/10/09.
//
// 백준 17144 미세먼지 안녕! https://www.acmicpc.net/problem/17144

let line = readLine()!.split(separator: " ").map { Int($0)! }
let (R, C, T) =  (line[0], line[1], line[2])
var matrix = Array(repeating: Array(repeating: 0, count: C), count: R)
var dustLocations = [[Int]]()

// 입력받기
for x in 0..<R {
    matrix[x] = readLine()!.split(separator: " ").map { Int($0)! }
}

// 공기 청정기 좌표 구하기
var airCleaner = [[Int]]()
for x in 0..<R {
    for y in 0..<C {
        if matrix[x][y] == -1 {
            airCleaner.append([x, y])
        }
    }
}

var up = (airCleaner[0][0], airCleaner[0][1])
var down = (airCleaner[1][0], airCleaner[1][1])

// 인접 방향 탐색 위한 좌표 설정
let dx = [0, -1, 0, 1]
let dy = [-1, 0, 1, 0]

// 확산시키기
func spreadDust() {
    let tmp = matrix // 동시에 확산시키기 위해 배열 복사

    for x in 0..<R {
        for y in 0..<C {
            if tmp[x][y] != 0 && tmp[x][y] != -1 { // 미세먼지가 없거나 공기청정기가 아닐 때는 확산시키기
                let dust = tmp[x][y]

                if dust < 5 { // 5보다 작을 때는 확산 불가
                    continue
                } else {
                    var count = 0

                    for k in 0..<4 { // 인접 방향 탐색
                        let nx = x + dx[k]
                        let ny = y + dy[k]

                        if 0..<R ~= nx && 0..<C ~= ny && tmp[nx][ny] != -1 { // 인접칸이 존재하고, 그칸이 공기청정기가 아닐 경우
                            matrix[nx][ny] += (dust / 5) // 몫만큼 주변 칸에 확산
                            count += 1
                        }
                    }
                    matrix[x][y] -= (dust / 5) * count // (r, c)에 남은 미세먼지 계산
                }
            }
        }
    }

}

// 위쪽 공기청정기 작동
func operateUpAirCleaner() {
    let x = up.0
    let y = up.1

    for nx in stride(from: x-1, through: 1, by: -1) {
        matrix[nx][y] = matrix[nx-1][y]
    }

    for ny in stride(from: 0, through: C-2, by: +1) {
        matrix[0][ny] = matrix[0][ny+1]
    }

    for nx in stride(from: 0, through: x-1, by: +1) {
        matrix[nx][C-1] = matrix[nx+1][C-1]
    }

    for ny in stride(from: C-1, through: 2, by: -1) {
        matrix[x][ny] = matrix[x][ny-1]
    }

    matrix[x][y+1] = 0
}

// 아래쪽 공기청정기 작동
func operateDownAirCleaner() {
    let x = down.0
    let y = down.1

    for nx in stride(from: x+1, through: R-2, by: +1) {
        matrix[nx][y] = matrix[nx+1][y]
    }

    for ny in stride(from: 0, through: C-2, by: +1) {
        matrix[R-1][ny] = matrix[R-1][ny+1]
    }

    for nx in stride(from: R-1, through: x+1, by: -1) {
        matrix[nx][C-1] = matrix[nx-1][C-1]
    }

    for ny in stride(from: C-1, through: 2, by: -1) {
        matrix[x][ny] = matrix[x][ny-1]
    }

    matrix[x][y+1] = 0
}

for _ in 0..<T { // T초 동안 반복
    spreadDust()
    operateUpAirCleaner()
    operateDownAirCleaner()
}

print(matrix.flatMap { $0 }.filter { $0 > 0 }.reduce(0, +))
