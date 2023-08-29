//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/08/16.
//

// 백준 1654 랜선 자르기 https://www.acmicpc.net/problem/1654

/*
처음에는 그냥 때려박다가 뭔가 익숙한 향기가 나서 보니 이분 탐색이었음
추후에 생각해 보면 일단 입력 값이 크기도 하고(땡스투 레츠,,,), 최대를 구하시오~ 의 느낌이라 이분 탐색이 될 수 있을 것 같다.
*/

// 필요한 값들을 입력받는다
let line = readLine()!.split(separator: " ").map { Int($0)! }
let (K, N) = (line[0], line[1])
var lengths = [Int]()

for _ in 0..<K {
    lengths.append(Int(readLine()!)!)
}

// start를 1로 지정해 주고(zeroDivisionError 대비), end를 받은 길이 중 가장 큰 값으로 지정
var start = 1
var end = lengths.max()!

/*
start, end에 따라 mid값을 구하고 count 변수를 만들어 준다.
length 배열을 돌며 mid보다 크거나 같은 길이가 있다면 가능한 개수를 count에 더해준다.
count < N: 개수가 모자라므로 mid가 더 짧아져야 한다 -> end를 mid-1로 지정한다
이외의 경우: mid가 더 길어져도 된다. 최대 길이를 구해야 하고, 문제에서 N개보다 많을 수도 있다고 하였음
start를 1로 지정해 주었으므로 최종으로 start-1 출력
*/

while start <= end {
    let mid = (start + end) / 2
    var count = 0

    for length in lengths {
        if length >= mid  { count += Int(length/mid) }
    }

    if count < N {
        end = mid - 1
    } else {
        start = mid + 1
    }
}

print(start - 1)
