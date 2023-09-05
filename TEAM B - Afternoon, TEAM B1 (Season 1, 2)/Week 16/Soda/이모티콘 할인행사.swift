//
//  main.swift
//  Algorithm
//
//  Created by 김민 on 2023/09/06.
//

// 프로그래머스 이모티콘 할인행사 https://school.programmers.co.kr/learn/courses/30/lessons/150368

import Foundation

let discount = [10, 20, 30, 40] // 할인율을 저장할 배열

func solution(_ users:[[Int]], _ emoticons:[Int]) -> [Int] {
    var discountCases = [[Int]]()
    var arr = Array(repeating: 0, count: emoticons.count)

    func dfs(_ depth: Int) { // dfs로 할인이 가능한 모든 조합을 만든다
        if depth == emoticons.count {
            discountCases.append(arr)
            return
        }

        for i in 0..<discount.count {
            arr[depth] = discount[i]
            dfs(depth+1)
        }
    }

    dfs(0)

    var answer = [0, 0]
    for (index, discountCase) in discountCases.enumerated() { // 가능한 할인 조합들을 순회함
        var membershipCount = 0 // 이모티콘 플러스 가입자 수를 저장할 변수
        var salesAmount = 0 // 판매액을 저장할 변수

        for user in users {
            var total = 0

            for j in 0..<discountCase.count {
                if user[0] <= discountCase[j] { // 할인율이 유저의 비울보다 크거나 같을 때
                    // testcase 13, 15, 18 ... 에서 자꾸 오류가 나서 찾아봤더니 부동 소수점 에러엿삼. 그래서 나눗셈을 곱셈으로 변경해줬음
                    // https://school.programmers.co.kr/questions/42440
                    // let price = Int((Double(100 - discountCases[index][j]) / 100.0) * Double(emoticons[j]))
                    let price = Int(Double(emoticons[j]) * Double(100 - discountCases[index][j]) * 0.01)
                    total += price
                }

                if total >= user[1] { // 유저의 가격보다 크다면 임티플 가입
                    membershipCount += 1
                    break
                }

                if j == discountCase.count - 1 { // 이모티콘을 다 사도 유저의 가격보다 작다면 판매액에 더하기
                    salesAmount += total
                }
            }
        }
        if answer[0] < membershipCount { // 이모티콘 플러스 가입자 수가 우선 순위가 높음
            answer = [membershipCount, salesAmount]
        } else if (answer[0] == membershipCount) && (salesAmount > answer[1]) {
            // 이모티콘 플러스 가입자 수가 같으면 이모티콘 판매액이 최대일 때
            answer[1] = salesAmount
        }
    }

    return answer
}
