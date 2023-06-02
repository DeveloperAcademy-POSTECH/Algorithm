//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/05/27.
//
// 백준 1874 스택 수열 https://www.acmicpc.net/problem/1874

/*
스택을 사용하여 풀이
count 변수와 입력받은 수들을 사용하여 풀이한다.
count 변수를 사용하여 각 입력까지로 이루어진 스택을 만들고, stack의 top이 입력과 같을 시에는 pop한다.
입력과 같지 않을 시에는 수열을 만들 수 없기 때문에 NO 출력.
result 문자열을 사용하여 문자열 출력
*/

let n: Int = Int(readLine()!)!
var stack: [Int] = []
var result: String = ""
var count: Int = 1

for _ in 0..<n {
    let num: Int = Int(readLine()!)!
    
    while (count <= num) {
        stack.append(count)
        result += "+\n"
        count += 1
    }
    
    if stack.last! == num {
        result += "-\n"
        _ = stack.popLast()!
    } else {
        print("NO")
        result = ""
        break
    }
}

print(result)
